import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.compat.v1.disable_eager_execution()

a = tf.constant(5.0)
b = tf.constant(1.0)
c = tf.add(a, b)

graph2 = tf.Graph()
with graph2.as_default():
    d = tf.constant(11.0)

with tf.compat.v1.Session(graph=graph2) as sess:
    # print(sess.run(c))
    print(sess.run(d))
