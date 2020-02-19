dict1 = {}
while True:
    name = input("请输入商品名称：")
    if name == "":
        break
    price = input("请输入商品价格：")
    dict1[name] = price
for k, v in dict1.items():
    print(f"{k}的价格是{v}元。")
if "游戏机" in dict1:
    print(dict1["游戏机"])
