import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets


class FashionMnist:
    out_features1 = 12
    out_features2 = 24
    con_neurons = 512

    def __init__(self, path):
        self.sess = tf.compat.v1.Session()
        self.data = read_data_sets(path, one_hot=True)

    def init_weight_variable(self, shape):
        initial = tf.random.truncated_normal(shape, stddev=0.1)
        return tf.Variable(initial)

    def init_bias_variable(self, shape):
        initial = tf.constant(1.0, shape=shape)
        return tf.Variable(initial)

    def conv2d(self, x, w):
        return tf.nn.conv2d(input=x,
                            filters=w,
                            strides=[1, 1, 1, 1],
                            padding="SAME")

    def max_pool_2x2(self, x):
        return tf.nn.max_pool2d(input=x,
                                ksize=[1, 2, 2, 1],
                                strides=[1, 2, 2, 1],
                                padding="SAME")

    def create_conv_pool_layer(self, input,
                               input_features, out_features):
        filter = self.init_weight_variable([5, 5,
                                            input_features,
                                            out_features])

        b_conv = self.init_bias_variable([out_features])

        h_conv = tf.nn.relu(self.conv2d(input, filter) + b_conv)

        h_pool = self.max_pool_2x2(h_conv)

        return h_pool

    def create_fc_layer(self, h_pool_flat,
                        input_features, con_neurons):

        w_fc = self.init_weight_variable([input_features,
                                          con_neurons])

        b_fc = self.init_bias_variable([con_neurons])

        h_fc1 = tf.nn.relu(tf.matmul(h_pool_flat, w_fc) + b_fc)
        return h_fc1

    def build(self):
        self.x = tf.compat.v1.placeholder(tf.float32, shape=[None, 784])
        x_image = tf.reshape(self.x, [-1, 28, 28, 1])
        self.y_ = tf.compat.v1.placeholder(tf.float32, shape=[None, 10])

        h_pool1 = self.create_conv_pool_layer(x_image,
                                              1,
                                              self.out_features1)

        h_pool2 = self.create_conv_pool_layer(h_pool1,
                                              self.out_features1,
                                              self.out_features2)

        h_pool2_flat_features = 7 * 7 * self.out_features2
        h_pool2_flat = tf.reshape(h_pool2,
                                  [-1, h_pool2_flat_features])
        h_fc = self.create_fc_layer(h_pool2_flat,
                                    h_pool2_flat_features,
                                    self.con_neurons)

        self.keep_prob = tf.compat.v1.placeholder("float")
        h_fc1_drop = tf.nn.dropout(h_fc, 1 - (self.keep_prob))

        w_fc = self.init_weight_variable([self.con_neurons, 10])
        b_fc = self.init_bias_variable([10])
        y_conv = tf.matmul(h_fc1_drop, w_fc) + b_fc

        correct_prediction = tf.equal(tf.argmax(input=y_conv, axis=1),
                                      tf.argmax(input=self.y_, axis=1))

        self.accuracy = tf.reduce_mean(input_tensor=tf.cast(correct_prediction, tf.float32))

        loss_func = tf.nn.softmax_cross_entropy_with_logits(labels=tf.stop_gradient(self.y_),
                                                            logits=y_conv)
        cross_entropy = tf.reduce_mean(input_tensor=loss_func)

        optimizer = tf.compat.v1.train.AdamOptimizer(0.001)
        self.train_step = optimizer.minimize(cross_entropy)

    def train(self):
        self.sess.run(tf.compat.v1.global_variables_initializer())
        merged = tf.compat.v1.summary.merge_all()

        batch_size = 100
        print("beging training...")

        for i in range(10):
            total_batch = int(self.data.train.num_examples / batch_size)

            for j in range(total_batch):
                batch = self.data.train.next_batch(batch_size)
                params = {self.x: batch[0], self.y_: batch[1],
                          self.keep_prob: 0.5}

                t, acc = self.sess.run([self.train_step, self.accuracy],
                                       params)
                if j % 100 == 0:
                    print("epoch: %d, pass: %d, acc: %f" % (i, j, acc))

    def eval(self, x, y, keep_prob):
        params = {self.x: x, self.y_: y, self.keep_prob: 1.0}
        test_acc = self.sess.run(self.accuracy, params)
        print('Test accuracy %f' % test_acc)
        return test_acc

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
