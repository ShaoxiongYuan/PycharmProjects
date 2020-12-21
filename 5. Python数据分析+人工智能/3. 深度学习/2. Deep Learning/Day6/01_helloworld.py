import paddle.fluid as fluid

# 定义两个常量
x = fluid.layers.fill_constant(shape=[1], dtype='int64', value=5)
y = fluid.layers.fill_constant(shape=[1], dtype='int64', value=1)

z = x + y

place = fluid.CUDAPlace(0)
exe = fluid.Executor(place)
result = exe.run(fluid.default_main_program(), fetch_list=[z])
print(result)
