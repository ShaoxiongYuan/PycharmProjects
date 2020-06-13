"""
新闻分类
"""

####################预处理########################
import os

data_root = '../data/news_classify/'
data_file = 'news_classify_data.txt'
test_file = 'test_list.txt'
train_file = 'train_list.txt'
dict_file = 'dict_txt.txt'

data_file_path = data_root + data_file
dict_file_path = data_root + dict_file
test_file_path = data_root + test_file
train_file_path = data_root + train_file


# 生成字典
def create_dict():
    dict_set = set()
    with open(data_file_path, encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        # 取出标题部分
        title = line.split('_!_')[-1].replace('\n', '')
        for w in title:  # 取出每个字
            dict_set.add(w)

    # 遍历集合，产生编码
    dict_list = []
    i = 0
    for s in dict_set:
        dict_list.append([s, i])
        i += 1

    dict_txt = dict(dict_list)

    end_dict = {'<unk>': i}
    dict_txt.update(end_dict)

    with open(dict_file_path, 'w', encoding='utf-8') as f:
        f.write(str(dict_txt))

    print('字典生成完成。')


def line_encoding(title, dict_txt, label):
    new_line = ''
    for w in title:
        if w in dict_txt:
            code = str(dict_txt[w])
        else:
            code = str(dict_txt['<unk>'])
        new_line += code + ','

    new_line = new_line[:-1]  # 去除最后一个多余逗号
    new_line = new_line + '\t' + label + '\n'
    return new_line


def create_data_list():
    with open(test_file_path, 'w') as f:
        pass
    with open(test_file_path, 'w') as f:
        pass

    # 从字典文件中读取内容
    with open(dict_file_path, encoding='utf-8') as f:
        dict_txt = eval(f.readlines()[0])

    with open(data_file_path, encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    for line in lines:
        words = line.replace('\n', '').split('_!_')
        label = words[1]
        title = words[3]
        new_line = line_encoding(title, dict_txt, label)

        if i % 10 == 0:
            with open(test_file_path, 'a', encoding='utf-8') as f:
                f.write(new_line)
        else:
            with open(train_file_path, 'a', encoding='utf-8') as f:
                f.write(new_line)

        i += 1
    print('生成测试集，训练集结束！')


create_dict()
create_data_list()

####################模型搭建，训练#####################
from multiprocessing import cpu_count
import numpy as np
import paddle
import paddle.fluid as fluid


def get_dict_len(dict_path):
    with open(dict_path, encoding='utf-8') as f:
        line = eval(f.readlines()[0])
    return len(line.keys())


def data_mapper(sample):
    data, label = sample  # 将sample元组拆分到两个变量
    # 拆分句子，将每个编码转换为数字, 并存入一个列表中
    val = [int(w) for w in data.split(",")]
    return val, int(label)  # 返回整数列表，标签(转换成整数)


def train_reader(train_file_path):
    def reader():
        with open(train_file_path, 'r') as f:
            lines = f.readlines()
            np.random.shuffle(lines)

            for line in lines:
                data, label = line.split('\t')
                yield data, label

    return paddle.reader.xmap_readers(data_mapper, reader, cpu_count(), buffer_size=1024)


def test_reader(test_file_path):
    def reader():
        with open(test_file_path, 'r') as f:
            lines = f.readlines()

            for line in lines:
                data, label = line.split('\t')
                yield data, label

    return paddle.reader.xmap_readers(data_mapper, reader, cpu_count(), buffer_size=1024)


def CNN_net(data, dict_dim, class_dim=10, emb_dim=128, hid_dim=128, hid_dim2=98):
    """
    定义网络
    :param data: 原始文本数据
    :param dict_dim: 词典大小
    :param class_dim: 分类数量
    :param emb_dim: 词嵌入计算参数
    :param hid_dim: 第一组卷积核大小
    :param hid_dim2: 第二组卷积核大小
    :return:
    """

    # 词嵌入层
    emb = fluid.layers.embedding(input=data, size=[dict_dim, emb_dim])

    conv1 = fluid.nets.sequence_conv_pool(input=emb, num_filters=hid_dim, filter_size=3, act='tanh', pool_type='sqrt')
    conv2 = fluid.nets.sequence_conv_pool(input=emb, num_filters=hid_dim2, filter_size=4, act='tanh', pool_type='sqrt')

    # 输出层
    output = fluid.layers.fc(input=[conv1, conv2], size=class_dim, act='softmax')
    return output


# 定义张量
words = fluid.layers.data(name='words', shape=[1], dtype='int64', lod_level=1)
label = fluid.layers.data(name='label', shape=[1], dtype='int64')
dict_dim = get_dict_len(dict_file_path)

# 创建神经网络
model = CNN_net(words, dict_dim)

# cost
cost = fluid.layers.cross_entropy(input=model, label=label)
avg_cost = fluid.layers.mean(cost)
acc = fluid.layers.accuracy(input=model, label=label)

# 克隆test_program用于评估
test_program = fluid.default_main_program().clone(for_test=True)

optimizer = fluid.optimizer.AdagradOptimizer(0.001)
optimizer.minimize(avg_cost)

# 定义执行器
place = fluid.CPUPlace()
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())

# reader准备数据
tr_reader = train_reader(train_file_path)
batch_train_reader = paddle.batch(tr_reader, batch_size=128)

ts_reader = test_reader(test_file_path)
batch_test_reader = paddle.batch(ts_reader, batch_size=128)

feeder = fluid.DataFeeder(place=place, feed_list=[words, label])

for pass_id in range(5):
    for batch_id, data in enumerate(batch_train_reader()):
        train_cost, train_acc = exe.run(feed=feeder.feed(data), fetch_list=[avg_cost, acc])

        # 每100次打印一笔
        if batch_id % 100 == 0:
            print('pass_id: %d, batch_id: %d, cost: %f, acc: %f' % (pass_id, batch_id, train_cost[0], train_acc[0]))

    # 每轮训练完对模型评估
    test_costs_list = []
    test_accs_list = []

    for batch_id, data in enumerate(batch_test_reader()):
        test_cost, test_acc = exe.run(program=test_program, feed=feeder.feed(data), fetch_list=[avg_cost, acc])
        test_costs_list.append(test_cost[0])
        test_accs_list.append(test_acc[0])
        # 计算平均损失值和准确率
    avg_test_cost = sum(test_costs_list) / len(test_costs_list)
    avg_test_acc = sum(test_accs_list) / len(test_accs_list)
    print("pass_id:%d, test_cost:%f, test_acc:%f" % (pass_id, avg_test_cost, avg_test_acc))

# 保存模型
model_save_dir = "../model/news_classify/"
if not os.path.exists(model_save_dir):
    os.makedirs(model_save_dir)
fluid.io.save_inference_model(model_save_dir,  # 模型保存路径
                              feeded_var_names=[words.name],  # 使用模型时需传入的参数
                              target_vars=[model],  # 预测结果
                              executor=exe)  # 执行器
print("模型保存完成.")


#############################预测##############################
def get_data(sentence):
    with open(dict_file_path, encoding='utf-8') as f:
        dict_txt = eval(f.readlines()[0])

    keys = dict_txt.keys()
    ret = []
    for s in sentence:
        if s not in keys:
            s = '<unk>'
        ret.append(int(dict_txt[s]))
    return ret


# 创建执行器
place = fluid.CPUPlace()
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())

print('加载模型')
infer_program, feeded_var_names, target_var = fluid.io.load_inference_model(dirname=model_save_dir, executor=exe)

texts = []
data1 = get_data("在获得诺贝尔文学奖7年之后，莫言15日晚间在山西汾阳贾家庄如是说")
data2 = get_data("综合'今日美国'、《世界日报》等当地媒体报道，芝加哥河滨警察局表示")
data3 = get_data("中国队无缘2020年世界杯")
data4 = get_data("中国人民银行今日发布通知，降低准备金率，预计释放4000亿流动性")
data5 = get_data("10月20日,第六届世界互联网大会正式开幕")
data6 = get_data("同一户型，为什么高层比低层要贵那么多？")
data7 = get_data("揭秘A股周涨5%资金动向：追捧2类股，抛售600亿香饽饽")
data8 = get_data("宋慧乔陷入感染危机，前夫宋仲基不戴口罩露面，身处国外神态轻松")
data9 = get_data("此盆栽花很好养，花美似牡丹，三季开花，南北都能养，很值得栽培")  # 不属于任何一个类别
texts.append(data1)
texts.append(data2)
texts.append(data3)
texts.append(data4)
texts.append(data5)
texts.append(data6)
texts.append(data7)
texts.append(data8)
texts.append(data9)

# 获取每个句子词数量
base_shape = [[len(c) for c in texts]]
# 生成数据
tensor_words = fluid.create_lod_tensor(texts, base_shape, place)
# 执行预测
result = exe.run(program=infer_program,
                 feed={feeded_var_names[0]: tensor_words},  # 待预测的数据
                 fetch_list=target_var)

names = ["文化", "娱乐", "体育", "财经", "房产", "汽车", "教育", "科技", "国际", "证券"]
for i in range(len(texts)):
    lab = np.argsort(result)[0][i][-1]
    print('预测结果：%d，名称：%s，概率：%f' % (lab, names[lab], result[0][i][lab]))
