import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

plhd = tf.compat.v1.placeholder(tf.float32, [2, 3])
plhd2 = tf.compat.v1.placeholder(tf.float32, [None, 3])

with tf.compat.v1.Session() as sess:
    d = [[1, 2, 3],
         [4, 5, 6]]
    print(sess.run(plhd, feed_dict={plhd: d}))
    print(sess.run(plhd2, feed_dict={plhd2: d}))
