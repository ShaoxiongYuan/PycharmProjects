import paddle.fluid as fluid
import numpy as np
import matplotlib.pyplot as plt

train_data = np.array([[0.5], [0.6], [0.8], [1.1],
                       [1.4]]).astype('float32')
y_true = np.array([[5.0], [5.5], [6.0], [6.8],
                   [6.8]]).astype('float32')
# 定义数据数据类型
x = fluid.layers.data(name="x", shape=[1], dtype="float32")
y = fluid.layers.data(name="y", shape=[1], dtype="float32")
# 通过全连接网络进行预测
y_predict = fluid.layers.fc(input=x, size=1, act=None)
# 添加损失函数
cost = fluid.layers.square_error_cost(input=y_predict, label=y)
avg_cost = fluid.layers.mean(cost)  # 求均方差
# 定义优化方法
optimizer = fluid.optimizer.SGD(learning_rate=0.01)
optimizer.minimize(avg_cost)  # 指定最小化均方差值
# 搭建网络
place = fluid.CPUPlace()  # 指定在CPU执行
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())  # 初始化系统参数
# 开始训练, 迭代200次
costs = []
iters = []
values = []
params = {"x": train_data, "y": y_true}
for i in range(200):
    outs = exe.run(feed=params, fetch_list=[y_predict.name,
                                            avg_cost.name])
    iters.append(i)  # 迭代次数
    costs.append(outs[1][0])  # 损失值


# 线性模型可视化
tmp = np.random.rand(10, 1)
tmp = tmp * 2
tmp.sort(axis=0)
print(tmp)
x_test = np.array(tmp).astype("float32")
params = {'x': x_test, 'y': x_test}
y_out = exe.run(feed=params, fetch_list=[y_predict.name])
y_test = y_out[0]

# 损失函数可视化
plt.figure("Training")
plt.title("Training Cost", fontsize=24)
plt.xlabel("Iter", fontsize=14)
plt.ylabel("Cost", fontsize=14)
plt.plot(iters, costs, color="red", label="Training Cost")
plt.grid()

# 线性模型可视化
plt.figure("Inference")
plt.title("Linear Regression", fontsize=24)
plt.plot(x_test, y_test, color="red", label="inference")
plt.scatter(train_data, y_true)
plt.legend()
plt.grid()
plt.show()
