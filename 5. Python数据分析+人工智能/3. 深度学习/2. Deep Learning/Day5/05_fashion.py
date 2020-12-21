import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets


class FashionMnist:
    out_features1 = 12  # 第一个卷积池化层输出通道数(即第一个卷基层卷积核数量)
    out_features2 = 24  # 第二个卷积池化层输出通道数(即第二个卷基层卷积核数量)
    con_neurons = 512  # fc神经元的数量

    def __init__(self, path):
        """
        构造方法
        :param path: 数据集路径
        """
        self.sess = tf.Session()
        self.data = read_data_sets(path, one_hot=True)

    def init_weight_variable(self, shape):
        """
        根据指定形状创建权重
        :param shape: 形状
        :return: 返回经过初始化的变量
        """
        # 产生截尾正态分布数据
        initial = tf.truncated_normal(shape, stddev=0.1)
        return tf.Variable(initial)

    def init_bias_variable(self, shape):
        """
        根据指定形状创建偏置
        :param shape:形状
        :return:返回经过初始化的变量
        """
        initial = tf.constant(1.0, shape=shape)
        return tf.Variable(initial)

    def conv2d(self, x, w):
        """
        二维卷积
        :param x: 原始数据
        :param w: 卷积核
        :return: 返回卷积运算结果
        """
        return tf.nn.conv2d(x,  # 原始数据
                            w,  # 原始数据
                            strides=[1, 1, 1, 1],  # 各个方向的步长值
                            padding="SAME")  # 同维卷积

    def max_pool_2x2(self, x):
        """
        池化
        :param x:原始数据
        :return:返回池化运算结果
        """
        return tf.nn.max_pool(x,  # 原始数据
                              ksize=[1, 2, 2, 1],  # 池化区域大小
                              strides=[1, 2, 2, 1],  # 各个方向的步长值
                              padding="SAME")

    def create_conv_pool_layer(self, input,
                               input_features, out_features):
        """
        创建卷积, 激活, 池化层
        :param input: 原始数据
        :param input_features: 输入通道数量
        :param out_features: 输出通道数量
        :return: 返回卷积, 激活, 池化层计算结果
        """
        filter = self.init_weight_variable([5, 5,
                                            input_features,
                                            out_features])
        # 偏置(个数等于卷积输出特征数)
        b_conv = self.init_bias_variable([out_features])
        # 卷积 + 激活
        h_conv = tf.nn.relu(self.conv2d(input, filter) + b_conv)
        # 池化
        h_pool = self.max_pool_2x2(h_conv)

        return h_pool

    def create_fc_layer(self, h_pool_flat,
                        input_features, con_neurons):
        """
        创建全连接层
        :param h_pool_flat: 输入, 经过拉伸后的一位数据
        :param input_features: 输入特征数量
        :param con_neurons: 神经原数量, 即输出特征数量
        :return: 经过全连接层计算的结果
        """
        # 权重
        w_fc = self.init_weight_variable([input_features,
                                          con_neurons])
        # 偏置, 数量等于权重列数
        b_fc = self.init_bias_variable([con_neurons])
        # 执行 wx+b 并进行激活运算
        h_fc1 = tf.nn.relu(tf.matmul(h_pool_flat, w_fc) + b_fc)
        return h_fc1

    def build(self):
        """
        组建CNN
        :return:
        """
        self.x = tf.placeholder(tf.float32, shape=[None, 784])
        x_image = tf.reshape(self.x, [-1, 28, 28, 1])  # 28*28单通道
        self.y_ = tf.placeholder(tf.float32, shape=[None, 10])  # 标签, N行10列

        # 第一组卷积池化
        h_pool1 = self.create_conv_pool_layer(x_image,
                                              1,
                                              self.out_features1)
        # 第二组卷积池化
        h_pool2 = self.create_conv_pool_layer(h_pool1,  # 上一层输出作为输入
                                              self.out_features1,
                                              self.out_features2)
        # 全连接层
        ## 对张量进行拉伸
        h_pool2_flat_features = 7 * 7 * self.out_features2
        h_pool2_flat = tf.reshape(h_pool2,
                                  [-1, h_pool2_flat_features])
        h_fc = self.create_fc_layer(h_pool2_flat,  # 输入
                                    h_pool2_flat_features,  # 输入特征数
                                    self.con_neurons)  # 输出特征数
        # dropout
        self.keep_prob = tf.placeholder("float")  # 保持率
        h_fc1_drop = tf.nn.dropout(h_fc, self.keep_prob)
        # 输出层
        w_fc = self.init_weight_variable([self.con_neurons, 10])
        b_fc = self.init_bias_variable([10])
        y_conv = tf.matmul(h_fc1_drop, w_fc) + b_fc

        # 评价
        correct_prediction = tf.equal(tf.argmax(y_conv, 1),  # 取出预测概率中最大的值的索引
                                      tf.argmax(self.y_, 1))  # 取出真实概率中最大的值的索引
        # 将上一步得到的bool类型数组转换为浮点型，并求准确率
        self.accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        # 损失函数
        loss_func = tf.nn.softmax_cross_entropy_with_logits(labels=self.y_,  # 真实值
                                                            logits=y_conv)  # 预测值
        cross_entropy = tf.reduce_mean(loss_func)
        # 优化器
        optimizer = tf.train.AdamOptimizer(0.001)
        self.train_step = optimizer.minimize(cross_entropy)

    def train(self):
        self.sess.run(tf.global_variables_initializer())  # 初始化
        merged = tf.summary.merge_all()  # 摘要合并

        batch_size = 100
        print("beging training...")

        for i in range(10):  # 迭代训练
            total_batch = int(self.data.train.num_examples / batch_size)  # 计算批次数量

            for j in range(total_batch):
                batch = self.data.train.next_batch(batch_size)  # 获取一个批次样本
                params = {self.x: batch[0], self.y_: batch[1],  # 输入、标签
                          self.keep_prob: 0.5}  # 丢弃率

                t, acc = self.sess.run([self.train_step, self.accuracy],  # 要执行的op
                                       params)  # 喂入参数
                if j % 100 == 0:
                    print("epoch: %d, pass: %d, acc: %f" % (i, j, acc))

    # 评价
    def eval(self, x, y, keep_prob):
        params = {self.x: x, self.y_: y, self.keep_prob: 1.0}
        test_acc = self.sess.run(self.accuracy, params)
        print('Test accuracy %f' % test_acc)
        return test_acc

    # 关闭会话
    def close(self):
        self.sess.close()


if __name__ == "__main__":
    mnist = FashionMnist('FASHION_MNIST_data/')
    mnist.build()
    mnist.train()

    print('\n----- Test -----')
    xs, ys = mnist.data.test.next_batch(100)
    mnist.eval(xs, ys, 0.5)
    mnist.close()
