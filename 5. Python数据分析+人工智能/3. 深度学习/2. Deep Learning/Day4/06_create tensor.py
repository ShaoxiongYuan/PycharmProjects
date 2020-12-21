import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

tensor_zeros = tf.zeros(shape=[2, 3], dtype='float32')
tensor_ones = tf.ones(shape=[3, 4], dtype='float32')
tensor_nd = tf.random.normal(shape=[10], mean=1.7, stddev=0.2, dtype='float32')
tensor_zeros_like = tf.zeros_like(tensor_ones)

with tf.compat.v1.Session() as sess:
    print(tensor_zeros.eval())
    print(tensor_ones.eval())
    print(tensor_nd.eval())
    print(tensor_zeros_like.eval())

