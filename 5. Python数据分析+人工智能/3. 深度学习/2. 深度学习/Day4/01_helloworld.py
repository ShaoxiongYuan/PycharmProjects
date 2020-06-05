import tensorflow as tf

hello = tf.constant('Hello world!')
sess = tf.Session()
print(sess.run(hello))
