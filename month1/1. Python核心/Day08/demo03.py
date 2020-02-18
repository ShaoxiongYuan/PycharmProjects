"""
函数参数
    实际参数
"""


def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


# 1.位置实参：位置
func01(1, 2, 3)

# 2.序列实参：拆
list1 = ["a", "b", "c"]
func01(*list1)
# 只传入key，没意义
dict1 = {1: "a", 2: "b", 3: "c"}
func01(*dict1)

func01(*"孙悟空")

# 3.关键字实参：名字
func01(p2=2, p1=1, p3=3)

# 4.字典实参：拆
dict2 = {"p3": "c", "p1": 1, "p2": "b"}
func01(**dict2)
