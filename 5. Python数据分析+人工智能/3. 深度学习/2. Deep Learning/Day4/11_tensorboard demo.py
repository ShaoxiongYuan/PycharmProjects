import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.compat.v1.disable_eager_execution()

a = tf.constant([1, 2, 3, 4, 5])
var = tf.Variable(tf.random.normal([2, 3]), name='var')
b = tf.constant(3.0, name='a')
c = tf.constant(4.0, name='b')
d = tf.add(b, c)

with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    fw = tf.compat.v1.summary.FileWriter('../summary/', graph=sess.graph)
    print(sess.run([a, var, d]))
