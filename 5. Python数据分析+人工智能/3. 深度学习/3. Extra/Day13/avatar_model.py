import os
import math
import numpy as np
import tensorflow as tf
from datetime import datetime
from avatar import Avatar


class AvatarModel:
    def __init__(self):
        self.avatar = Avatar()
        self.img_shape = self.avatar.img_shape
        self.batch_shape = self.avatar.batch_shape
        self.batch_size = self.avatar.batch_size
        self.chunk_size = self.avatar.chunk_size
        self.noise_img_size = 100
        self.gf_size = 64
        self.df_size = 64
        self.epoch_size = 200
        self.learning_rate = 0.0002
        self.beta1 = 0.5
        self.sample_size = 64

    @staticmethod
    def conv_out_size_same(size, stride):
        return int(math.ceil(float(size) / float(stride)))

    @staticmethod
    def linear(images, output_size, stddev=0.02, bias_start=0.0, name='Linear'):
        """
        执行线性计算
        :param images:
        :param output_size:
        :param stddev:
        :param bias_start:
        :param name:
        :return:
        """
        shape = images.get_shape().as_list()

        with tf.variable_scope(name):
            w = tf.get_variable("w", [shape[1], output_size], tf.float32,
                                tf.random_normal_initializer(stddev=stddev))
            b = tf.get_variable("b", [output_size],
                                initializer=tf.constant_initializer(bias_start))
            return tf.matmul(images, w) + b, w, b

    @staticmethod
    def batch_normalizer(x, epsilon=1e-5, momentum=0.9, train=True, name='batch_norm'):
        """
        批量归一化
        :param x:
        :param epsilon:
        :param momentum:
        :param train:
        :param name:
        :return:
        """
        with tf.variable_scope(name):
            return tf.contrib.layers.batch_norm(x, decay=momentum, updates_collections=None,
                                                epsilon=epsilon, scale=True, is_training=train)

    @staticmethod
    def conv2d(images, output_dim, stddev=0.02, name="conv2d"):
        """
        卷积层
        :param images:
        :param output_dim:
        :param stddev:
        :param name:
        :return:
        """
        with tf.variable_scope(name):
            filter_shape = [5, 5, images.get_shape()[-1], output_dim]
            strides_shape = [1, 2, 2, 1]

            w = tf.get_variable('w', filter_shape, initializer=tf.truncated_normal_initializer(stddev=stddev))
            b = tf.get_variable('b', [output_dim], initializer=tf.constant_initializer(0.0))

            conv = tf.nn.conv2d(images, w, strides=strides_shape, padding='SAME')
            conv = tf.reshape(tf.nn.bias_add(conv, b), conv.get_shape())
            return conv

    @staticmethod
    def deconv2d(images, output_shape, stddev=0.02, name='deconv2d'):
        """
        反卷积
        :param images:
        :param output_shape:
        :param stddev:
        :param name:
        :return:
        """
        with tf.variable_scope(name):
            filter_shape = [5, 5, output_shape[-1], images.get_shape()[-1]]
            strides_shape = [1, 2, 2, 1]

            w = tf.get_variable('w', filter_shape, initializer=tf.random_normal_initializer(stddev=stddev))
            b = tf.get_variable('biases', [output_shape[-1]], initializer=tf.constant_initializer(0.0))

            deconv = tf.nn.conv2d_transpose(images, w, output_shape=output_shape, strides=strides_shape)
            deconv = tf.nn.bias_add(deconv, b)
            return deconv, w, b

    @staticmethod
    def lrelu(x, leak=0.2):
        return tf.maximum(x, leak * x)

    def generator(self, noise_imgs, train=True):
        """
        生成器
        :param noise_imgs:
        :param train:
        :return:
        """
        with tf.variable_scope('generator'):
            s_h, s_w, _ = self.img_shape
            s_h2, s_w2 = self.conv_out_size_same(s_h, 2), self.conv_out_size_same(s_w, 2)
            s_h4, s_w4 = self.conv_out_size_same(s_h2, 2), self.conv_out_size_same(s_w2, 2)
            s_h8, s_w8 = self.conv_out_size_same(s_h4, 2), self.conv_out_size_same(s_w4, 2)
            s_h16, s_w16 = self.conv_out_size_same(s_h8, 2), self.conv_out_size_same(s_w8, 2)

            # layer 0
            z, h0_w, h0_b = self.linear(noise_imgs, self.gf_size * 8 * s_h16 * s_w16)
            h0 = tf.reshape(z, [-1, s_h16, s_w16, self.gf_size * 8])
            h0 = self.batch_normalizer(h0, train=train, name='g_bn0')
            h0 = tf.nn.relu(h0)

            # layer 1
            h1, h1_w, h1_b = self.deconv2d(h0, [self.batch_size, s_h8, s_w8, self.gf_size * 4], name='g_h1')
            h1 = self.batch_normalizer(h1, train=train, name='g_bn1')
            h1 = tf.nn.relu(h1)

            # layer 2
            h2, h2_w, h2_b = self.deconv2d(h1, [self.batch_size, s_h4, s_w4, self.gf_size * 2], name='g_h2')
            h2 = self.batch_normalizer(h2, train=train, name='g_bn2')
            h2 = tf.nn.relu(h2)

            # layer 3
            h3, h3_w, h3_b = self.deconv2d(h2, [self.batch_size, s_h2, s_w2, self.gf_size * 1], name='g_h3')
            h3 = self.batch_normalizer(h3, train=train, name='g_bn3')
            h3 = tf.nn.relu(h3)

            # layer 4
            h4, h4_w, h4_b = self.deconv2d(h3, self.batch_shape, name='g_h4')
            return tf.nn.tanh(h4)

    def discriminator(self, real_imgs, reuse=False):
        """
        判别器
        :param real_imgs:
        :param reuse:
        :return:
        """
        with tf.variable_scope('discriminator', reuse=reuse):
            # layer 0
            # 卷积操作
            h0 = self.conv2d(real_imgs, self.df_size, name='d_h0_conv')
            # 激活函数
            h0 = self.lrelu(h0)

            # layer 1
            h1 = self.conv2d(h0, self.df_size * 2, name='d_h1_conv')
            h1 = self.batch_normalizer(h1, name='d_bn1')
            h1 = self.lrelu(h1)

            # layer 2
            h2 = self.conv2d(h1, self.df_size * 4, name='d_h2_conv')
            h2 = self.batch_normalizer(h2, name='d_bn2')
            h2 = self.lrelu(h2)

            # layer 3
            h3 = self.conv2d(h2, self.df_size * 8, name='d_h3_conv')
            h3 = self.batch_normalizer(h3, name='d_bn3')
            h3 = self.lrelu(h3)

            # layer 4
            h4, _, _ = self.linear(tf.reshape(h3, [self.batch_size, -1]), 1, name='d_h4_lin')

            return tf.nn.sigmoid(h4), h4

    @staticmethod
    def loss_graph(real_logits, fake_logits):
        """
        定义损失函数
        :param real_logits:
        :param fake_logits:
        :return:
        """
        gen_loss = tf.reduce_mean(
            tf.nn.sigmoid_cross_entropy_with_logits(logits=fake_logits, labels=tf.ones_like(fake_logits)))

        fake_loss = tf.reduce_mean(
            tf.nn.sigmoid_cross_entropy_with_logits(logits=fake_logits, labels=tf.zeros_like(fake_logits)))

        real_loss = tf.reduce_mean(
            tf.nn.sigmoid_cross_entropy_with_logits(logits=real_logits, labels=tf.ones_like(real_logits)))

        dis_loss = tf.add(fake_loss, real_loss)
        return gen_loss, fake_loss, real_loss, dis_loss

    @staticmethod
    def optimizer_graph(gen_loss, dis_loss, learning_rate, beta1):
        """
        定义优化器
        :param gen_loss:
        :param dis_loss:
        :param learning_rate:
        :param beta1:
        :return:
        """
        train_vars = tf.trainable_variables()
        gen_vars = [var for var in train_vars if var.name.startswith('generator')]
        dis_vars = [var for var in train_vars if var.name.startswith('discriminator')]

        gen_optimizer = tf.train.AdamOptimizer(
            learning_rate=learning_rate, beta1=beta1
        ).minimize(gen_loss, var_list=gen_vars)

        dis_optimizer = tf.train.AdamOptimizer(
            learning_rate=learning_rate, beta1=beta1
        ).minimize(dis_loss, var_list=dis_vars)

        return gen_optimizer, dis_optimizer

    def train(self):
        real_imgs = tf.placeholder(tf.float32, self.batch_shape, name='real_images')
        noise_imgs = tf.placeholder(tf.float32, [None, self.noise_img_size], name='noise_images')

        # 生成器图片
        fake_imgs = self.generator(noise_imgs)

        # 判别器
        real_outputs, real_logits = self.discriminator(real_imgs)
        fake_outputs, fake_logits = self.discriminator(fake_imgs, reuse=True)

        # 损失
        gen_loss, fake_loss, real_loss, dis_loss = self.loss_graph(real_logits, fake_logits)
        
        # 优化
        gen_optimizer, dis_optimizer = self.optimizer_graph(gen_loss, dis_loss, self.learning_rate, self.beta1)

        # 开始训练
        saver = tf.train.Saver()
        step = 0

        gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.8)

        with tf.Session(config=tf.ConfigProto(gpu_options=gpu_options)) as sess:
            sess.run(tf.global_variables_initializer())
            for epoch in range(self.epoch_size):
                batches = self.avatar.batches()
                for batch_imgs in batches:
                    # generator的输入噪声
                    noises = np.random.uniform(-1, 1, size=(self.batch_size, self.noise_img_size)).astype(np.float32)
                    # 优化
                    _ = sess.run(dis_optimizer, feed_dict={real_imgs: batch_imgs, noise_imgs: noises})
                    _ = sess.run(gen_optimizer, feed_dict={noise_imgs: noises})
                    _ = sess.run(gen_optimizer, feed_dict={noise_imgs: noises})
                    step += 1
                    print(datetime.now().strftime('%c'), epoch, step)
                    
                # 每一轮结束计算loss
                loss_dis = sess.run(dis_loss, feed_dict={real_imgs: batch_imgs, noise_imgs: noises})
                loss_real = sess.run(real_loss, feed_dict={real_imgs: batch_imgs, noise_imgs: noises})
                loss_fake = sess.run(fake_loss, feed_dict={real_imgs: batch_imgs, noise_imgs: noises})
                loss_gen = sess.run(gen_loss, feed_dict={noise_imgs: noises})

                print(datetime.now().strftime('%c'), ' epoch:', epoch, ' step:', step, ' loss_dis:', loss_dis,
                      ' loss_real:', loss_real, ' loss_fake:', loss_fake, ' loss_gen:', loss_gen)

            model_path = os.getcwd() + os.sep + "avatar.model"
            saver.save(sess, model_path, global_step=step)

    def gen(self):
        # 生成图片
        noise_imgs = tf.placeholder(tf.float32, [None, self.noise_img_size], name='noise_imgs')
        sample_imgs = self.generator(noise_imgs, train=False)
        saver = tf.train.Saver()
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            saver.restore(sess, tf.train.latest_checkpoint('.'))
            sample_noise = np.random.uniform(-1, 1, size=(self.sample_size, self.noise_img_size))
            samples = sess.run(sample_imgs, feed_dict={noise_imgs: sample_noise})
        for num in range(len(samples)):
            self.avatar.save_img(samples[num], 'samples' + os.sep + str(num) + '.jpg')
