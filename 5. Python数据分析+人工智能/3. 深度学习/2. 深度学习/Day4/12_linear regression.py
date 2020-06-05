import tensorflow as tf

# 第一步：产生样本数据
x = tf.random_normal([100, 1], mean=1.75, stddev=0.5, name='x_data')
y_true = tf.matmul(x, [[2.0]]) + 5

# 第二步：定义线性模型，执行预测
w = tf.random_normal([1, 1], name='w')
weight = tf.Variable(w, trainable=True)
bias = tf.Variable(0.0, name='b', trainable=True)  # 训练过程中是否可以被优化
y_predict = tf.matmul(x, weight) + bias

# 第三步：构建损失函数
loss = tf.reduce_mean(tf.square(y_true - y_predict))
train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# 第四步：执行训练（梯度下降优化器）
tf.summary.scalar('losses', loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    fw = tf.summary.FileWriter('../summary', graph=sess.graph)
    for i in range(400):
        sess.run(train_op)
        summary = sess.run(tf.summary.merge_all())
        fw.add_summary(summary, i)
        print(i, ': w:', weight[0][0].eval(), 'b:', bias.eval(), 'loss:', loss.eval())
