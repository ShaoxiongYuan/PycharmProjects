# -*- coding:utf-8 -*-
__author__ = 'Tony Qu'
from django.http import HttpResponse
from django.db import DatabaseError
from userinfo.models import *
from .models import *
import logging
import json
import datetime
from .deals import *
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
## This example upgrade by Tony Qu in 2018
## It includes some basic function about search a car or
## a part of car in some known_car
## PLEASE NOTE: 
## If you have trouble installing it, try any of the other demos
## that don't require it instead.
# 买股票
def Tobuy(request):
    if request.method == "POST":
        user = request.user
        code = request.POST.get('code')
        amount = request.POST.get('amount')
        print("@@@@", amount)
        price = request.POST.get('price')
        print("@@@@", price)
        tradepwd = request.POST.get('tradepwd')
        result = deal(user, 'buy', code, amount, price, tradepwd, settings.BUY_RANGE)
        rcode = result['code']
        print(rcode)
        resulttf = True
        data = ''
        error = ''
        if rcode == 1:
            data = result['msg']
        elif rcode == 2:
            data = result['msg']
        elif rcode == 3:
            data = result['msg']
        elif rcode == 4:
            data = result['msg']
        elif rcode == 5:
            data = result['msg']
        elif rcode == 6:
            data = result['msg']
        elif rcode == 7:
            resulttf = False
            data = result['msg']
        elif rcode == 8:
            resulttf = False
            data = result['msg']
        elif rcode == 9:
            resulttf = False
            data = result['msg']
        return HttpResponse(json.dumps({"result": resulttf, "data": data, "error": error}))
    elif request.method == "GET":
        userid = request.user.id
        try:
            fund = Fund.objects.get(user_id=userid)
            amoney = fund.money - fund.frozen_money
        except DatabaseError as e:
            logging.warning(e)
            return HttpResponse(json.dumps({"result": False, "data": "", "error": e}))
        return HttpResponse(json.dumps({"result": True, "data": amoney, "error": ''}))


# 卖股票
def Tosale(request):
    if request.method == 'POST':
        user = request.user
        code = request.POST.get('code')
        amount = request.POST.get('amount')
        price = request.POST.get('price')
        tradepwd = request.POST.get('tradepwd')
        result = deal(user, 'sale', code, amount, price, tradepwd, settings.SALE_RANGE)
        rcode = result['code']
        print(rcode)
        resulttf = True
        data = ''
        error = ''
        if rcode == 1:
            data = result['msg']
        elif rcode == 2:
            data = result['msg']
        elif rcode == 6:
            data = result['msg']
        elif rcode == 3:
            resulttf = False
            data = result['msg']
        elif rcode == 4:
            resulttf = False
            data = result['msg']
        elif rcode == 5:
            resulttf = False
            data = result['msg']
        return HttpResponse(json.dumps({"result": resulttf, "data": data, "error": error}))
    elif request.method == 'GET':
        userid = request.user.id
        try:
            amoney = UserInfo.objects.get(id=userid)
        except DatabaseError as e:
            logging.warning(e)
            return HttpResponse(json.dumps({"result": False, "data": "", "error": e}))
        return HttpResponse(json.dumps({"result": True, "data": amoney, "error": ''}))


# 委托
def trade(request):
    if request.method == 'POST':
        user = request.user
        code = request.POST.get('code')
        data = {}
        bosstocks = BOSStock.objects.filter(user=user, stock__stonumber=code)
        bosstocklist = []
        for bosstock in bosstocks:
            a = {}
            a['stock'] = bosstock.stock.stonumber
            a['stockname'] = bosstock.stock.company_name
            a['role'] = bosstock.get_role()
            a['price'] = str(bosstock.price)
            a['amount'] = bosstock.amount
            a['get_datetime'] = bosstock.get_datetime()
            bosstocklist.append(a)
        print("----", bosstocklist)
        dealstocks = DealStock.objects.filter(Q(suser=user) | Q(buser=user), stock=code)
        dealstocklist = []
        for dealstock in dealstocks:
            a = {}
            a['price'] = str(dealstock.price)
            a['amount'] = dealstock.amount
            a['datetime'] = dealstock.get_datetime()
            a['stock'] = dealstock.stock
            print(a['stock'])
            print(type(a['stock']))
            dealstocklist.append(a)
        print("-----", dealstocklist)
        data['bosstocklist'] = bosstocklist
        data['dealstocklist'] = dealstocklist
        return HttpResponse(json.dumps({"result": True, "data": data, "error": ""}))


# 挂单
def allstock(request):
    bosstockall = BOSStock.objects.all()
    print(bosstockall)
    bosstocklist = []
    for bosstock in bosstockall:
        a = {}
        a['user'] = bosstock.user.username
        a['stock'] = bosstock.stock.stonumber
        a['stockname'] = bosstock.stock.company_name
        a['role'] = bosstock.get_role()
        a['price'] = str(bosstock.price)
        a['amount'] = bosstock.amount
        a['get_datetime'] = bosstock.get_datetime()
        bosstocklist.append(a)
    print(bosstocklist)
    return HttpResponse(json.dumps({"result": True, "data": bosstocklist, "error": ""}))























