dict1 = {"qtx": ["编码", "看书", "跑步", "音乐"], "lzmly": ["刷抖音", "看电影", "吃"]}

for i in dict1["qtx"]:
    print(i)

for k in dict1:
    print(k)

for k in dict1:
    for i in dict1[k]:
        print(i)
