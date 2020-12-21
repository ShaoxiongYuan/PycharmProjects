import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

pld = tf.compat.v1.placeholder(tf.float32, [None, 3])
print(pld)
pld.set_shape([4, 3])
print(pld)

new_pld = tf.reshape(pld, [3, 4])
print(new_pld)
new_pld = tf.reshape(pld, [2, 6])
print(new_pld)
