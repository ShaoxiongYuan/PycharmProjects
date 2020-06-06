"""
使用神经网络实现手写体识别
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import pylab

# 读取数据，定义变量
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
x = tf.placeholder(tf.float32, [None, 784])  # N个样本，784特征
y = tf.placeholder(tf.float32, [None, 10])  # N个样本，10个概率

w = tf.Variable(tf.random_normal([784, 10]))
b = tf.Variable(tf.zeros([10]))

# 构建模型，损失函数，优化器
pred_y = tf.nn.softmax(tf.matmul(x, w) + b)
cross_entropy = -tf.reduce_sum(y * tf.log(pred_y), reduction_indices=1)
cost = tf.reduce_mean(cross_entropy)
optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

# 执行训练，模型评估
training_epochs = 200
batch_size = 100
saver = tf.train.Saver()
model_path = '../model/mnist/mnist_model.ckpt'

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # 循环训练
    for epoch in range(training_epochs):
        avg_cost = 0.0
        total_batch = int(mnist.train.num_examples / batch_size)

        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            params = {x: batch_xs, y: batch_ys}
            o, c = sess.run([optimizer, cost], feed_dict=params)
            avg_cost += (c / total_batch)
        print("epoch: %d, cost=%.9f" % (epoch + 1, avg_cost))
    print('Finished!')

    # 模型评估
    correct_pred = tf.equal(tf.argmax(pred_y, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    print('accuracy:', accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))

    save_path = saver.save(sess, model_path)
    print('Model Path:', save_path)

# 执行预测
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver.restore(sess, model_path)
    batch_xs, batch_ys = mnist.test.next_batch(2)
    output = tf.argmax(pred_y, 1)

    output_val, predv = sess.run([output, pred_y], feed_dict={x: batch_xs})

    print("预测结论:\n", output_val, "\n")
    print("实际结果:\n", batch_ys, "\n")
    print("预测概率:\n", predv, "\n")

    # 显示图片
    im = batch_xs[0]  # 第1个测试样本数据
    im = im.reshape(-1, 28)
    pylab.imshow(im)
    pylab.show()
    im = batch_xs[1]  # 第2个测试样本数据
    im = im.reshape(-1, 28)
    pylab.imshow(im)
    pylab.show()
