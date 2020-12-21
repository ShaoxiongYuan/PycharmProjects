import tensorflow as tf
from tensorflow.keras.datasets import mnist
import pylab

tf.compat.v1.disable_eager_execution()

mnist = mnist.load_data()

x = tf.compat.v1.placeholder(tf.float32, [None, 784])
y = tf.compat.v1.placeholder(tf.float32, [None, 10])

w = tf.Variable(tf.random.normal([784, 10]))
b = tf.Variable(tf.zeros([10]))

pred_y = tf.nn.softmax(tf.matmul(x, w) + b)
cross_entropy = -tf.reduce_sum(input_tensor=y * tf.math.log(pred_y), axis=1)
cost = tf.reduce_mean(input_tensor=cross_entropy)
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.01).minimize(cost)

training_epochs = 50
batch_size = 100
saver = tf.compat.v1.train.Saver()
model_path = '../model/mnist/mnist_model.ckpt'

with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())

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

    correct_pred = tf.equal(tf.argmax(input=pred_y, axis=1), tf.argmax(input=y, axis=1))
    accuracy = tf.reduce_mean(input_tensor=tf.cast(correct_pred, tf.float32))
    print('accuracy:', accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))

    save_path = saver.save(sess, model_path)
    print('Model Path:', save_path)

with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    saver.restore(sess, model_path)
    batch_xs, batch_ys = mnist.test.next_batch(2)
    output = tf.argmax(input=pred_y, axis=1)

    output_val, predv = sess.run([output, pred_y], feed_dict={x: batch_xs})

    print("预测结论:\n", output_val, "\n")
    print("实际结果:\n", batch_ys, "\n")
    print("预测概率:\n", predv, "\n")

    im = batch_xs[0]
    im = im.reshape(-1, 28)
    pylab.imshow(im)
    pylab.show()

    im = batch_xs[1]
    im = im.reshape(-1, 28)
    pylab.imshow(im)
    pylab.show()
