import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.compat.v1.disable_eager_execution()

a = tf.constant(5.0)
b = tf.constant(1.0)
c = tf.add(a, b)

with tf.compat.v1.Session() as sess:
    print(sess.run(c))
