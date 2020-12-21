import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.compat.v1.disable_eager_execution()

a = tf.constant([1, 2, 3, 4, 5])
var = tf.Variable(tf.random.normal([2, 3], name='var'))
init_op = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session() as sess:
    sess.run(init_op)
    print(sess.run([a, var]))
