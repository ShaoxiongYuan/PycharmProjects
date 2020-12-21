import tensorflow as tf

tf.compat.v1.disable_eager_execution()

# 第一步：产生样本数据
x = tf.random.normal([100, 1], mean=1.75, stddev=0.5, name='x_data')
y_true = tf.matmul(x, [[2.0]]) + 5

# 第二步：定义线性模型，执行预测
w = tf.random.normal([1, 1], name='w')
weight = tf.Variable(w, trainable=True)
bias = tf.Variable(0.0, name='b', trainable=True)
y_predict = tf.matmul(x, weight) + bias

# 第三步：构建损失函数
loss = tf.reduce_mean(input_tensor=tf.square(y_true - y_predict))
train_op = tf.compat.v1.train.GradientDescentOptimizer(0.1).minimize(loss)

# 第四步：执行训练（梯度下降优化器）
tf.compat.v1.summary.scalar('losses', loss)

with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    fw = tf.compat.v1.summary.FileWriter('../summary', graph=sess.graph)
    for i in range(400):
        sess.run(train_op)
        summary = sess.run(tf.compat.v1.summary.merge_all())
        fw.add_summary(summary, i)
        print(i, ': w:', weight[0][0].eval(), 'b:', bias.eval(), 'loss:', loss.eval())
