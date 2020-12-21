import tensorflow as tf

hello = tf.constant('Hello world!')
sess = tf.compat.v1.Session()
print(sess.run(hello))
