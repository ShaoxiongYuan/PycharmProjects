from django.shortcuts import render
from django.http import HttpResponse
from userinfo.models import *
from django.contrib.auth.hashers import check_password
from django.db.models import F
from django.core import serializers
from .models import *
from stocks.models import *
import json
import datetime
import decimal



def deal(user, sob, stockNo, amount, price, tradepwd, price_range):
    result = {}
    if sob == "sale":
        hold = Hold.objects.get(user=user, stock__stonumber=stockNo)  # 卖指定股持仓
        fund = Fund.objects.get(user=user)   # 卖资金
        new_amount = hold.amount - hold.frozen   # 卖持仓可用数量
        stock = Stock.objects.get(stonumber=stockNo)
        stockdetail = json.dumps(stock.model_to_dict())
        datetimes = datetime.datetime.now()
        if new_amount >= int(amount):  # 持仓是否够
            # 够 可用股票数>欲卖股票数
            hold.frozen = hold.frozen + int(amount)   # 将要卖股票进行冻结
            hold.save()
            # 查询是否有买入
            range = (decimal.Decimal(price), decimal.Decimal(price)+decimal.Decimal(price_range))
            buy_stock = BOSStock.objects.filter(stock__stonumber=stockNo,role=0,price__range=range)
            print(buy_stock)
            if len(buy_stock) <= 0:
                print("bb")
                # 无买入, 卖挂单
                bosstock = BOSStock()
                bosstock.user = user
                bosstock.stock = stock
                bosstock.role = 1
                bosstock.price = decimal.Decimal(price)
                bosstock.amount = decimal.Decimal(amount)
                bosstock.datetime = datetimes
                bosstock.save()
                result['code'] = 2
                result['msg'] = "无买入股票,全部卖出股票已挂单"
                print("rrr", result)
                return result
            else:
                print("cc")
                # 有买入, 交易
                bank = Bank.objects.get(user=user)
                if bank:
                    chpwd = check_password(tradepwd, bank.tradepwd)
                    if chpwd:
                        for st in buy_stock:
                            if int(amount) >= st.amount:
                                print("dd")
                                # 卖出股票 > 买入股票, 卖部分交易
                                amount = int(amount) - st.amount   # 卖出股票-买入股 = 要卖剩余股
                                hold.amount = hold.amount - st.amount   # 卖持仓数量更改
                                hold.frozen = hold.frozen - st.amount   # 卖持仓冻结更改
                                hold.save()
                                fund.money = fund.money + st.amount*st.price   # 卖资金增加
                                fund.save()
                                buser = Hold.objects.filter(user=st.user, stock=stock)   # 获取该股买家持仓
                                if len(buser) > 0:
                                    # 有持仓
                                    buser = Hold.objects.filter(user=st.user, stock=stock).update(amount=F('amount')+st.amount)
                                else:
                                    # 无持仓,创建持仓
                                    buser = Hold.objects.create(user=st.user, stock=stock, amount=st.amount, frozen=0)
                                DealStock.objects.create(suser=user, buser=st.user, price=st.price, amount=st.amount, datetime=datetimes, stock=stockdetail)
                                st.delete()
                            else:
                                # 卖出股票 < 买入股票, 卖全部交易
                                st.amount = st.amount - int(amount)
                                st.save()
                                hold.amount = hold.amount - int(amount)   # 卖持仓数减少
                                hold.frozen = hold.frozen - int(amount)   # 卖持仓冻结减少
                                hold.save()
                                fund.money = fund.money + int(amount) * st.price   # 卖资金增加
                                fund.save()
                                buser = Hold.objects.filter(user=st.user, stock=stock)   # 买家是否有持仓
                                if len(buser) > 0:
                                    # 有持仓, 持仓数更新
                                    buser = Hold.objects.filter(user=st.user, stock=stock).update(amount=F('amount') + int(amount))
                                else:
                                    # 无持仓, 创建买家持仓
                                    buser = Hold.objects.create(user=st.user, stock=stock, amount=int(amount), frozen=0)
                                DealStock.objects.create(suser=user, buser=st.user, price=st.price, amount=int(amount), datetime=datetimes, stock=stockdetail)
                        print(int(amount))
                        if int(amount) > 0:
                            print("ff")
                            # 挂单
                            bosstock = BOSStock()
                            bosstock.user = user
                            bosstock.stock = stock
                            bosstock.role = 1
                            bosstock.price = decimal.Decimal(price)
                            bosstock.amount = decimal.Decimal(amount)
                            bosstock.datetime = datetimes
                            bosstock.save()
                            result['code'] = 6
                            result['msg'] = "剩余股票已挂单"
                            print("rrr", result)
                            return result
                        elif int(amount) <= 0:
                            print("gg")
                            result['code'] = 1
                            result['msg'] = "股票已成交"
                            print("rrr", result)
                            return result
                    else:
                        result['code'] = 5
                        result['msg'] = "支付密码不正确"
                        print("rrr", result)
                        return result
                else:
                    result['code'] = 4
                    result['msg'] = "未绑定银行卡"
                    print("rrr", result)
                    return result
        else:
            result['code'] = 3
            result['msg'] = "所持股票数量不足"
            print("rrr", result)
            return result
    elif sob == "buy":
        fund = Fund.objects.get(user=user)  # 资金对象
        money = fund.money - decimal.Decimal(amount) * decimal.Decimal(price)  # 资金是否够
        stock = Stock.objects.get(stonumber=stockNo)
        stockdetail = json.dumps(stock.model_to_dict())
        datetimes = datetime.datetime.now()
        if int(money) > 0:  # 够
            # 冻结
            fund.frozen_money = fund.frozen_money + decimal.Decimal(amount) * decimal.Decimal(price)
            fund.save()    # 资金冻结
            range = (decimal.Decimal(price) - decimal.Decimal(price_range), decimal.Decimal(price))
            sale_stock = BOSStock.objects.filter(stock__stonumber=stockNo, role=1, price__range=range)  # 查询是否有卖挂单
            if len(sale_stock) <= 0:
                # 无卖家挂单，全部股票以买家身份挂单
                bosstock = BOSStock()
                bosstock.user = user
                bosstock.stock = stock
                bosstock.role = 0
                bosstock.price = decimal.Decimal(price)
                bosstock.amount = decimal.Decimal(amount)
                bosstock.datetime = datetimes
                bosstock.save()
                result['code'] = 5
                result['msg'] = "无卖家挂单信息,已以买家身份全部挂单"
                return result
            else:
                # 有卖家挂单,交易
                bank = Bank.objects.filter(user=user)
                if bank:
                    chpwd = check_password(tradepwd, bank[0].tradepwd)
                    if chpwd:
                        # 密码正确
                        for st in sale_stock:
                            if int(amount) > st.amount:
                                # 买入股票 > 卖出股票，部分成交
                                hold = Hold.objects.filter(user=user, stock=stock)  # 查询持仓是否有这个股
                                if len(hold) > 0:
                                    # 持仓数量增加
                                    hold.update(amount=F('amount') + st.amount)
                                else:
                                    # 否
                                    Hold.objects.create(user=user, stock=stock, amount=st.amount, frozen=0)   # 创建持仓
                                bfund = Fund.objects.get(user=user)   # 获取买家资金对象
                                bfund.money = bfund.money - st.amount * st.price   # 交易后买家总资金减少
                                bfund.frozen_money = bfund.frozen_money - (decimal.Decimal(amount)*decimal.Decimal(price)-st.amount*st.price)   # 交易后买家冻结减少
                                bfund.save()
                                sfund = Fund.objects.get(user=st.user)  # 获取卖家资金对象
                                sfund.money = sfund.money + st.amount * st.price  # 交易后卖家资金加
                                sfund.save()
                                Hold.objects.filter(user=st.user, stock=stock).update(amount=F('amount') - st.amount, frozen=0)  # 卖家持仓减少
                                DealStock.objects.create(suser=st.user, buser=user, price=st.price,
                                                                     amount=st.amount, datetime=datetimes, stock=stockdetail)
                                amount = int(amount) - st.amount   # 剩余股票数量>0,挂单
                                st.delete()
                            else:
                                print("@@@@@@@")
                                # 买入股票 < 卖出股票, 全部买入
                                hold = Hold.objects.filter(user=user, stock=stock)  # 获取买家持仓
                                if len(hold) > 0:  # 有持仓
                                    # 买持仓数量更新
                                    hold.update(amount=F("amount")+decimal.Decimal(amount))
                                else:   # 没持仓,创建持仓
                                    Hold.objects.create(user=user, stock=stock, amount=decimal.Decimal(amount), frozen=0)
                                bfund = Fund.objects.filter(user=user).first()   # 买家资金对象
                                bfund.frozen_money = bfund.frozen_money - decimal.Decimal(amount) * decimal.Decimal(price)  # 买家冻结资金减少,总资金减少
                                bfund.money = bfund.money - decimal.Decimal(amount) * decimal.Decimal(price)  # 买家冻结资金减少,总资金减少
                                bfund.save()
                                Hold.objects.filter(user=st.user, stock=stock).update(amount=F('amount') - decimal.Decimal(amount))  # 卖持仓数量更新
                                sfund = Fund.objects.get(user=st.user)
                                sfund.money = sfund.money + decimal.Decimal(amount) * decimal.Decimal(price)   # 卖资金
                                sfund.save()
                                DealStock.objects.create(suser=st.user, buser=user, price=st.price, amount=st.amount, datetime=datetimes, stock=stockdetail)
                                st.amount = st.amount - decimal.Decimal(amount)
                                st.save()
                        if int(amount) > 0:
                            # 挂单
                            print("a")
                            bosstock = BOSStock()
                            bosstock.user = user
                            bosstock.stock = stock
                            bosstock.role = 0
                            bosstock.price = price
                            bosstock.amount = amount
                            bosstock.datetime = datetimes
                            bosstock.save()
                            result['code'] = 5
                            result['msg'] = "剩余股票已挂单"
                            return result
                        elif int(amount) <= 0:
                            result['code'] = 6
                            result['msg'] = "股票已购买"
                            return result
                    else:
                        result['code'] = 9
                        result['msg'] = '支付密码不正确'
                        return result
                else:
                    result['code'] = 8
                    result['msg'] = '未绑定银行卡'
                    return result
        else:
            result['code'] = 7
            result['msg'] = "资金不足"
            return result

