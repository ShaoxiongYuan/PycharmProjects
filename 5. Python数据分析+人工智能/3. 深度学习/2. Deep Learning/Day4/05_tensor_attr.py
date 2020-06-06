import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant(5.0)

with tf.compat.v1.Session() as sess:
    print(sess.run(a))
    print('name', a.name)  # name属性
    print('dtype', a.dtype)  # dtype属性
    print('shape', a.shape)  # shape属性
    print('graph', a.graph)  # graph属性
    print('op', a.op)  # op属性
