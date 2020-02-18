shang_pin_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

ding_dan = []


def print_shangpin():
    for key, value in shang_pin_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


def decide_commodity(id):
    if id in shang_pin_info:
        return
    else:
        print("该商品不存在")


def total_money():
    zong_jia = 0
    for item in ding_dan:
        shang_pin = shang_pin_info[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (shang_pin["name"], shang_pin["price"], item["count"]))
        zong_jia += shang_pin["price"] * item["count"]
        return zong_jia


def change(total_price, paid):
    return_money = float(paid) - float(total_price)
    if return_money < 0:
        print("金额不足")
    else:
        print(f"应找回{return_money}元。")
        ding_dan.clear()


def gou_wu():
    while True:
        num = int(input("1键购买，2键结算，3键退出"))
        if num == 1:
            print_shangpin()
            while True:
                cid = int(input("请输入商品编号："))
                decide_commodity(cid)
                if cid in shang_pin_info:
                    break
            count = int(input("请输入购买数量："))
            ding_dan.append({"cid": cid, "count": count})
            print("添加到购物车。")
        elif num == 2:
            zong_jia = total_money()
            while True:
                qian = float(input(f"总价{zong_jia}元，请输入金额："))
                change(zong_jia, qian)
                if ding_dan == []:
                    break
        elif num == 3:
            break


gou_wu()
