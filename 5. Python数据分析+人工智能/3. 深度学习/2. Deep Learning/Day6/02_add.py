import paddle.fluid as fluid
import numpy

# 创建x, y两个1行1列，类型为float32的变量(张量)
x = fluid.layers.data(name="x", shape=[1], dtype="float32")
y = fluid.layers.data(name="y", shape=[1], dtype="float32")
result = fluid.layers.elementwise_add(x, y)  # 两个张量按元素相加
place = fluid.CPUPlace()  # 指定在CPU上执行
exe = fluid.Executor(place)  # 创建执行器
# exe.run(fluid.default_startup_program())  # 初始化网络
# a = numpy.array([int(input("x:"))]) #输入x, 并转换为数组
# b = numpy.array([int(input("y:"))]) #输入y, 并转换为数组
# a = numpy.array([1, 2, 3]) # 输入x, 并转换为数组
# b = numpy.array([4, 5, 6]) # 输入y, 并转换为数组
a = numpy.array([[1, 1, 1], [2, 2, 2]])  # 输入x, 并转换为数组
b = numpy.array([[3, 3, 3], [4, 4, 4]])  # 输入y, 并转换为数组
params = {"x": a, "y": b}
outs = exe.run(fluid.default_main_program(),  # 默认程序上执行
               feed=params,  # 喂入参数
               fetch_list=[result])  # 获取结果
for i in outs:
    print(i)
