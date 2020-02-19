import os

pid = os.fork()

if pid < 0:
    print("进程创建失败")
elif pid == 0:
    print("新的进程")
else:
    print("原来的进程")

print("实验结束")
