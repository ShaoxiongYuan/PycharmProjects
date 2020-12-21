import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


x = tf.random.normal([100, 1], mean=1.75, stddev=0.5, name='x_data')
y_true = tf.matmul(x, [[2.0]]) + 5


w = tf.random.normal([1, 1], name='w')
weight = tf.Variable(w, trainable=True)
bias = tf.Variable(0.0, name='b', trainable=True)  
y_predict = tf.matmul(x, weight) + bias


loss = tf.reduce_mean(input_tensor=tf.square(y_true - y_predict))
train_op = tf.compat.v1.train.GradientDescentOptimizer(0.1).minimize(loss)


tf.compat.v1.summary.scalar('losses', loss)
saver = tf.compat.v1.train.Saver()

with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    fw = tf.compat.v1.summary.FileWriter('../summary', graph=sess.graph)

    
    if os.path.exists('../model/linear_model/checkpoint'):
        saver.restore(sess, '../model/linear_model/')
    for i in range(200):
        sess.run(train_op)
        summary = sess.run(tf.compat.v1.summary.merge_all())
        fw.add_summary(summary, i)
        print(i, ': w:', weight[0][0].eval(), 'b:', bias.eval(), 'loss:', loss.eval())

    
    saver.save(sess, '../model/linear_model/')
