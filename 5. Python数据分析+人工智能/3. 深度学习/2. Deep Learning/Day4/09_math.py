import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.compat.v1.disable_eager_execution()

x = tf.constant([[1, 2],
                 [3, 4]], dtype=tf.float32)
y = tf.constant([[4, 3],
                 [3, 2]], dtype=tf.float32)

x_add_y = tf.add(x, y)
x_mul_y = tf.matmul(x, y)
log_x = tf.math.log(x)
x_sum = tf.reduce_sum(input_tensor=x, axis=1)

data = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=tf.float32)
segment_idx = tf.constant([0, 0, 0, 1, 1, 2, 2, 2, 2, 2], dtype=tf.int32)
x_seg_sum = tf.math.segment_sum(data, segment_idx)

with tf.compat.v1.Session() as sess:
    print(sess.run(x_add_y))
    print(sess.run(x_mul_y))
    print(log_x.eval())
    print(x_sum.eval())
    print(x_seg_sum.eval())
