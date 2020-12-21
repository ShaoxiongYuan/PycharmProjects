import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant(5.0)

with tf.compat.v1.Session() as sess:
    print(sess.run(a))
    print('name', a.name)
    print('dtype', a.dtype)
    print('shape', a.shape)
    print('graph', a.graph)
    print('op', a.op)
