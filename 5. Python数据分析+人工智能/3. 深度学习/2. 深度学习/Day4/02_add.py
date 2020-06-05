import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant(5.0)
b = tf.constant(1.0)
c = tf.add(a, b)

with tf.Session() as sess:
    print(sess.run(c))
