"""
都影响
"""

list1 = [[1, 2], [3, 4]]
list2 = list1
list1[0][0] = 2
print(list2)

"""
浅拷贝
"""
list1 = [[1, [2, 3]], [[3, 4], 5], [[6, 7], 8]]
list2 = list1[:]
list1[0] = "一"
print(list2)
list1[1][0] = "二"
print(list2)
list1[2][0][1] = "六"
print(list2)

"""
深拷贝
"""
import copy

list3 = [[1, [2, 3]], [[3, 4], 5], [[6, 7], 8]]
list4 = copy.deepcopy(list3)
list3[0] = "一"
print(list4)
list3[1][0] = "二"
print(list4)
list3[2][0][0] = "三"
print(list4)
