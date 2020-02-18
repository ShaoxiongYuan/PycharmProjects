dict1 = {"北京": {"景点": ["故宫", "天安门", "天坛"], "美食": ["豆汁", "焦圈", "烤鸭"]},
         "天津": {"景点": ["天津之眼", "瓷房子"], "美食": ["狗不理包子", "大麻花", "煎饼"]}}

for item in dict1["北京"]["美食"]:
    print(item)

for item in dict1["天津"]["景点"]:
    print(item)

for k in dict1:
    print(k)

for v in dict1.values():
    for i in v["景点"]:
        print(i)

dict1["北京"]["美食"].append("炸酱面")
print(dict1)