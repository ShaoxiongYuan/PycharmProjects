import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant(5.0)
b = tf.constant(1.0)

c = tf.add(a, b)

graph = tf.compat.v1.get_default_graph()

print(graph)

with tf.compat.v1.Session() as sess:
    print(sess.run(c))
    print(a.graph)
    print(c.graph)
    print(sess.graph)
