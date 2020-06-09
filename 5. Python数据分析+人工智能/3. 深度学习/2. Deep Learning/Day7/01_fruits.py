"""
水果分类案例

1. 预处理
2. CNN训练，模型保存
3. 模型加载，预测
"""

########################### 数据预处理 #############################
import os

name_dict = {'apple': 0, 'banana': 1, 'grape': 2, 'orange': 3, 'pear': 4}
data_root_path = '../data/fruits/'
test_file_path = data_root_path + 'test.txt'
train_file_path = data_root_path + 'train.txt'
name_data_list = {}  # 记录每个类别有哪些图片


def save_train_test_file(path, name):
    if name not in name_data_list:
        img_list = [path]
        name_data_list[name] = img_list
    else:
        name_data_list[name].append(path)


dirs = os.listdir(data_root_path)
for d in dirs:
    full_path = data_root_path + d
    if os.path.isdir(full_path):  # 如果是目录
        imgs = os.listdir(full_path)
        for img in imgs:
            save_train_test_file(full_path + '/' + img, d)
    else:  # 如果是文件
        pass

with open(test_file_path, 'w') as f1:
    pass

with open(train_file_path, 'w') as f2:
    pass

for name, img_list in name_data_list.items():
    i = 0
    num = len(img_list)  # 获取每个类别图像数量
    print('%s: %d张' % (name, num))

    for img in img_list:
        if i % 10 == 0:
            with open(test_file_path, 'a') as f:
                line = '%s\t%d\n' % (img, name_dict[name])
                f.write(line)
        else:
            with open(train_file_path, 'a') as f:
                line = '%s\t%d\n' % (img, name_dict[name])
                f.write(line)
        i += 1

print('预处理完成。')

########################### 模型搭建 #############################
import paddle
import paddle.fluid as fluid
import os
from multiprocessing import cpu_count
import matplotlib.pyplot as plt


def train_mapper(sample):
    """
    传入样本，读取图片，设置大小，归一化
    :param sample: 文本样本，元组，格式为（图片路径，类别）
    :return: 返回经过归一化处理的图片数据
    """
    img_path, label = sample
    if not os.path.exists(img_path):
        print('图片不存在：', img_path)

    # 图片读取
    img = paddle.dataset.image.load_image(img_path)
    # 设置固定大小
    img = paddle.dataset.image.simple_transform(im=img,
                                                resize_size=100,
                                                crop_size=100,
                                                is_color=True,
                                                is_train=True)

    # 归一化
    img = img.astype('float32') / 255.0
    return img, label


def train_r(train_list, buffered_size=1024):
    def reader():
        with open(train_list) as f:
            lines = [line.strip() for line in f]

            for line in lines:
                line = line.replace('\n', '')
                img_path, lab = line.split('\t')
                yield img_path, int(lab)

    return paddle.reader.xmap_readers(train_mapper, reader, cpu_count(), buffered_size)


# 数据准备
BATCH_SIZE = 32
train_reader = train_r(train_list=train_file_path)
random_train_reader = paddle.reader.shuffle(reader=train_reader, buf_size=1300)
batch_train_reader = paddle.batch(random_train_reader, batch_size=BATCH_SIZE)

image = fluid.layers.data(name='image', shape=[3, 100, 100], dtype='float32')
label = fluid.layers.data(name='label', shape=[1], dtype='int64')


# 搭建CNN
def convolution_neural_network(image, type_size):
    """

    :param image:输入图像
    :param type_size: 输出值的个数
    :return:
    """
    # 第一组卷积池化
    conv_pool_1 = fluid.nets.simple_img_conv_pool(input=image, filter_size=3, num_filters=32, pool_size=2,
                                                  pool_stride=2, act='relu')
    # 丢弃
    drop = fluid.layers.dropout(x=conv_pool_1, dropout_prob=0.5)

    # 第二组卷积池化
    conv_pool_2 = fluid.nets.simple_img_conv_pool(input=drop, filter_size=3, num_filters=64, pool_size=2,
                                                  pool_stride=2, act='relu')
    # 丢弃
    drop = fluid.layers.dropout(x=conv_pool_2, dropout_prob=0.5)

    # 第三组卷积池化
    conv_pool_3 = fluid.nets.simple_img_conv_pool(input=drop, filter_size=3, num_filters=64, pool_size=2,
                                                  pool_stride=2, act='relu')
    # 丢弃
    drop = fluid.layers.dropout(x=conv_pool_3, dropout_prob=0.5)

    # 全连接层
    fc = fluid.layers.fc(input=drop, size=512, act='relu')
    # 丢弃
    drop = fluid.layers.dropout(x=fc, dropout_prob=0.5)

    predict = fluid.layers.fc(input=drop, size=type_size, act='softmax')
    return predict


predict = convolution_neural_network(image=image, type_size=5)

# 损失函数：交叉熵
cost = fluid.layers.cross_entropy(input=predict, label=label)
avg_cost = fluid.layers.mean(cost)

accuracy = fluid.layers.accuracy(input=predict, label=label)

optimizer = fluid.optimizer.AdamOptimizer(learning_rate=0.001)
optimizer.minimize(avg_cost)

place = fluid.CPUPlace()
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())

# feeder
feeder = fluid.DataFeeder(feed_list=[image, label], place=place)

costs = []  # 损失函数
accs = []  # 准确率
times = 0
batches = []

# 开始训练
for pass_id in range(200):
    train_cost = 0
    for batch_id, data in enumerate(batch_train_reader()):
        times += 1
        train_cost, train_acc = exe.run(program=fluid.default_main_program(), feed=feeder.feed(data),
                                        fetch_list=[avg_cost, accuracy])
        if batch_id % 20 == 0:
            print('pass_id:%d, step:%d, cost:%f, acc:%.5f' % (pass_id, batch_id, train_cost[0], train_acc[0]))
            accs.append(train_acc[0])
            costs.append(train_cost[0])
            batches.append(times)

model_save_dir = '../model/fruits'
if not os.path.exists(model_save_dir):
    os.makedirs(model_save_dir)
fluid.io.save_inference_model(dirname=model_save_dir,
                              feeded_var_names=['image'],
                              target_vars=[predict],
                              executor=exe)
print("训练保存模型完成!")

# 训练过程可视化
plt.figure('training', facecolor='lightgray')
plt.title("training", fontsize=24)
plt.xlabel("iter", fontsize=20)
plt.ylabel("cost/acc", fontsize=20)
plt.plot(batches, costs, color='red', label="Training Cost")
plt.plot(batches, accs, color='green', label="Training Acc")
plt.legend()
plt.grid()
plt.show()
plt.savefig("train.png")

#######################测试########################
from PIL import Image
import numpy as np


def load_image(path):
    img = paddle.dataset.image.load_and_transform(path, 100, 100, False).astype('float32')
    img = img / 255.0
    return img


# 定义执行器
place = fluid.CPUPlace()
infer_exe = fluid.Executor(place)

infer_imgs = []
test_img = 'apple_1.png'
infer_imgs.append(load_image(test_img))
infer_imgs = np.array(infer_imgs)

# 加载模型
infer_program, feed_target_names, fetch_targets = fluid.io.load_inference_model(model_save_dir, infer_exe)
results = infer_exe.run(infer_program, feed={feed_target_names[0]: infer_imgs}, fetch_list=fetch_targets)
print(results)

# 转换成好读的字符串
result = np.argmax(results[0])
for k, v in name_dict.items():
    if result == v:
        print('预测结果：', k)

img = Image.open(test_img)
plt.imshow(img)
plt.show()
