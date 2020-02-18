price = input("商品价格：")
amount = input("购买数量：")
paid = input("支付金额：")
return_money = float(paid) - float(amount) * float(price)
if return_money < 0:
    not_enough = float(price) * float(amount) - float(paid)
    print(f"钱不够，还差{not_enough}元。")
else:
    print(f"应找回{return_money}元。")
