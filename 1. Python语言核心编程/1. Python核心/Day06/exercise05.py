manager = {"曹操", "刘备", "孙权"}
technician = {"曹操", "刘备", "关羽", "张飞"}
print(manager & technician)
print(manager - technician)
print(technician - manager)
print(len(manager | technician))
print("张飞" in manager)
