from PIL import Image
import paddle
import paddle.fluid as fluid
import numpy as np
import os
from multiprocessing import cpu_count
import matplotlib.pyplot as plt

# 定义一组变量
name_dict = {"apple": 0, "banana": 1, "grape": 2, "orange": 3, "pear": 4}  # 水果名称和数组对应字典
data_root_path = "../data/fruits/"  # 数据样本所在目录
test_file_path = data_root_path + "test_vgg.txt"  # 测试集文件路径
train_file_path = data_root_path + "train_vgg.txt"  # 训练集文件路径
name_data_list = {}  # 记录每个类别的图片路径


# 将文件路径存入临时字典
def save_train_test_file(path, name):
    if name not in name_data_list:  # 当前水果没有在字典中，新增
        img_list = []
        img_list.append(path)  # 将图片添加到列表
        name_data_list[name] = img_list  # 将“名称-图片列表”键值对插入字典
    else:  # 当前水果已经在字典中，添加到相应的列表
        name_data_list[name].append(path)


# 遍历所有子目录，读取出所有图片文件，并插入字典、保存到测试集、训练集
dirs = os.listdir(data_root_path)
for d in dirs:
    full_path = data_root_path + d  # 目录名称 + 子目录名称

    if os.path.isdir(full_path):  # 目录
        imgs = os.listdir(full_path)  # 列出子目录中的文件
        for img in imgs:
            save_train_test_file(full_path + "/" + img,  # 图片文件完整路径
                                 d)  # 子目录名称（类别名称）
    else:  # 文件
        pass

# 将字典中的内容保存文件中
with open(test_file_path, "w") as f1:  # 清空测试集文件
    pass
with open(train_file_path, "w") as f2:  # 清空训练集文件
    pass

# 遍历字典，将内容写入文件
for name, img_list in name_data_list.items():
    i = 0
    num = len(img_list)  # 每个类别图片数量
    print("%s: %d张图像" % (name, num))

    for img in img_list:  # 遍历每个列表，将图片路径存入文件
        if i % 10 == 0:  # 每10张写一张到测试集
            with open(test_file_path, "a") as f:
                line = "%s\t%d\n" % (img, name_dict[name])
                f.write(line)  # 写入文件
        else:  # 其它写入训练集
            with open(train_file_path, "a") as f:
                line = "%s\t%d\n" % (img, name_dict[name])
                f.write(line)  # 写入文件
        i += 1

print("数据预处理完成.")


# train_mapper函数：对传入的图片路径进行读取，返回图像数据（多通道矩阵）、标签
def train_mapper(sample):
    img, label = sample  # 将sample中值赋给img, label

    if not os.path.exists(img):
        print(img, "图片文件不存在")

    # 读取图片文件
    img = paddle.dataset.image.load_image(img)  # 读取图片
    # 对图像进行简单变换：修剪、设置大小，输出(3, 100, 100)张量
    img = paddle.dataset.image.simple_transform(im=img,  # 原图像数据
                                                resize_size=100,
                                                crop_size=100,
                                                is_color=True, is_train=True)
    # 对图像数据进行归一化处理，像素的值全部计算压缩到0~1之间
    img = img.astype("float32") / 255.0
    return img, label  # 返回图像数据、标签


# 读取训练集文件，将路径、标签作为参数调用train_mapper函数
def train_r(train_list, buffered_size=1024):
    def reader():
        with open(train_list, "r") as f:  # 打开训练集
            lines = [line.strip() for line in f]  # 读取出所有样本行

            for line in lines:
                # 去掉每行的换行符，并根据tab字符进行拆分，得到两个字段
                img_path, lab = line.replace("\n", "").split("\t")
                yield img_path, int(lab)

    # xmap_readers高阶函数，作用是将reader产生的数据穿个train_mapper函数进行下一步处理
    return paddle.reader.xmap_readers(train_mapper,  # 二次处理函数
                                      reader,  # 原始reader
                                      cpu_count(),  # 线程数(和cpu数量一致)
                                      buffered_size)  # 缓冲区大小


BATCH_SIZE = 32  # 批次大小

# 定义reader
train_reader = train_r(train_list=train_file_path)  # train_file_path为训练集文件路径
random_train_reader = paddle.reader.shuffle(reader=train_reader,  # 原始reader
                                            buf_size=1300)  # 缓冲区大小
batch_train_reader = paddle.batch(random_train_reader,
                                  batch_size=BATCH_SIZE)  # 批量读取器
# 定义变量
image = fluid.layers.data(name="image", shape=[3, 100, 100], dtype="float32")
label = fluid.layers.data(name="label", shape=[1], dtype="int64")


# 创建VGG模型
def vgg_bn_drop(image, type_size):
    def conv_block(ipt, num_filter, groups, dropouts):
        # 创建Convolution2d, BatchNorm, DropOut, Pool2d组
        return fluid.nets.img_conv_group(input=ipt,  # 输入图像像，[N,C,H,W]格式
                                         pool_stride=2,  # 池化步长值
                                         pool_size=2,  # 池化区域大小
                                         conv_num_filter=[num_filter] * groups,
                                         conv_filter_size=3,
                                         conv_act="relu",
                                         conv_with_batchnorm=True,
                                         pool_type="max")

    conv1 = conv_block(image, 64, 2, [0.0, 0])  # 最后一个参数个数和组数量相对应
    conv2 = conv_block(conv1, 128, 2, [0.0, 0])
    conv3 = conv_block(conv2, 256, 3, [0.0, 0.0, 0.0])
    conv4 = conv_block(conv3, 512, 3, [0.0, 0.0, 0.0])
    conv5 = conv_block(conv4, 512, 3, [0.0, 0.0, 0.0])

    drop = fluid.layers.dropout(x=conv5, dropout_prob=0.2)  # 待调整
    fc1 = fluid.layers.fc(input=drop, size=512, act=None)

    bn = fluid.layers.batch_norm(input=fc1, act="relu")  # batch normal
    drop2 = fluid.layers.dropout(x=bn, dropout_prob=0.0)
    fc2 = fluid.layers.fc(input=drop2, size=512, act=None)
    predict = fluid.layers.fc(input=fc2, size=type_size, act="softmax")

    return predict


# 调用上面的函数创建VGG
predict = vgg_bn_drop(image=image, type_size=5)  # type_size和水果类别一致
# 损失函数
cost = fluid.layers.cross_entropy(input=predict, label=label)
avg_cost = fluid.layers.mean(cost)
# 计算准确率
accuracy = fluid.layers.accuracy(input=predict, label=label)
# 优化器
optimizer = fluid.optimizer.Adam(learning_rate=0.0001)  # 自适应梯度下降优化器
optimizer.minimize(avg_cost)

# 创建Executor
place = fluid.CPUPlace()
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())

# 定义feeder
feeder = fluid.DataFeeder(feed_list=[image, label], place=place)

costs = []  # 记录损失值
accs = []  # 记录准确率
times = 0
batches = []  # 记录批次

for pass_id in range(5):
    train_cost = 0

    for batch_id, data in enumerate(batch_train_reader()):
        times += 1

        train_cost, train_acc = exe.run(program=fluid.default_main_program(),
                                        feed=feeder.feed(data),  # 喂入一个batch数据
                                        fetch_list=[avg_cost, accuracy])  # 获取结果
        if batch_id % 20 == 0:
            print("pass_id:%d, bat_id:%d, cost:%f, acc:%f" %
                  (pass_id, batch_id, train_cost[0], train_acc[0]))
            accs.append(train_acc[0])  # 记录准确率
            costs.append(train_cost[0])  # 记录损失值
            batches.append(times)  # 记录训练批次数

# 保存模型
model_save_dir = "../model/fruits_vgg/"  # 模型保存路径
if not os.path.exists(model_save_dir):  # 如果模型路径不存在则创建
    os.makedirs(model_save_dir)
fluid.io.save_inference_model(dirname=model_save_dir,  # 保存路径
                              feeded_var_names=["image"],  # 使用模型需传入的参数
                              target_vars=[predict],  # 模型结果
                              executor=exe)  # 模型
print("模型保存完成.")

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

# 定义执行器
place = fluid.CPUPlace()
infer_exe = fluid.Executor(place)


# 加载数据
def load_img(path):
    img = paddle.dataset.image.load_and_transform(path, 100, 100, False).astype("float32")
    img = img / 255.0
    return img


infer_imgs = []  # 存放要预测图像数据
test_img = "../data/fruits/orange_1.jpg"  # 待预测图片
infer_imgs.append(load_img(test_img))  # 加载图片，并且将图片数据添加到待预测列表
infer_imgs = np.array(infer_imgs)  # 转换成数组

# 加载模型
infer_program, feed_target_names, fetch_targets = \
    fluid.io.load_inference_model(model_save_dir, infer_exe)
# 执行预测
results = infer_exe.run(infer_program,  # 执行预测program
                        feed={feed_target_names[0]: infer_imgs},  # 传入待预测图像数据
                        fetch_list=fetch_targets)  # 返回结果
print(results)

result = np.argmax(results[0])  # 取出预测结果中概率最大的元素索引值
for k, v in name_dict.items():  # 将类别由数字转换为名称
    if result == v:  # 如果预测结果等于v, 打印出名称
        print("预测结果:", k)  # 打印出名称

# 显示待预测的图片
img = Image.open(test_img)
plt.imshow(img)
plt.show()
