# -*- coding:utf-8 -*-
__author__ = 'Tony Qu'
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import F
# from stdnum import luhn

import logging
from .models import *
import json

# Create your views here.
## This example upgrade by Tony Qu in 2018
## It includes some basic function about search a car or
## a part of car in some known_car
## PLEASE NOTE: 
## If you have trouble installing it, try any of the other demos
## that don't require it instead.

auth_check = 'MarcelArhut'

# 登录
def login_(request):

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if not username:
            return HttpResponse(json.dumps({"result":False, "data":"", "error":"用户名密码不能为空"}))
        # 使用django提供的验证方法，传入用户名和密码，会返回一个user对象
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # user.backend = 'django.contrib.auth.backends.ModelBackend'  # 指定默认的登录验证方式
            login(request, user)
            print("##########",request.user)
            url = request.COOKIES.get('source_url', '')
            return HttpResponse(json.dumps({"result": True, "data": {"url":url, "username":username}, "error": ""}))
        else:
            return HttpResponse(json.dumps({"result":False, "data":"", "error":"用户名或密码错误"}))
    if request.method == 'GET':
        return HttpResponse(json.dumps({"result":True, "data":"", "error":""}))


# 注册
def register_(request):
    if request.method == 'POST':
        new_user = UserInfo()
        new_user.username = request.POST.get('username', '')
        if not new_user.username:
            return HttpResponse(json.dumps({"result":False, "data":"", "error":"用户名密码不能为空"}))
        try:
            olduser = UserInfo.objects.filter(username=new_user.username)
            if olduser:
                return HttpResponse(json.dumps({"result":False, "data":"", "error":"该用户名已经存在"}))
        except ObjectDoesNotExist as e:
            logging.warning(e)
        if request.POST.get('pwd') != request.POST.get('cpwd'):
            return HttpResponse(json.dumps({"result": False, "data": "", "error": "两次输入的密码不一致"}))
        new_user.password = make_password(request.POST.get('pwd'), auth_check, 'pbkdf2_sha1')
        try:
            new_user.save()
            Fund.objects.create(user=new_user, money=0, frozen_money=0)
        except ObjectDoesNotExist as e:
            logging.warning(e)
        return HttpResponse(json.dumps({"result":True, "data":"注册成功", "error":""}))
    if request.method == 'GET':
        return HttpResponse(json.dumps({"result":True, "data":"", "error":""}))


# 注销
def logout_(request):
    logout(request)
    return HttpResponse(json.dumps({"result":True, "data":"成功退出", "error":""}))


# 充值
# @login_required
def charge(request):
    if request.method == 'POST':
        user = request.user
        money = request.POST.get('money')
        charpwd = request.POST.get('charpwd')
        bank = Bank.objects.filter(user=user).first()
        print(bank)
        if bank:
            chpwd = check_password(charpwd, bank.tradepwd)
            if chpwd:
                Fund.objects.filter(user=user).update(money=F('money') + money)
                return HttpResponse(json.dumps({"result": True, "data": "充值成功", "error": ""}))
            else:
                return HttpResponse(json.dumps({"result": False, "data": "", "error": "密码错误"}))
        else:
            return HttpResponse(json.dumps({"result": False, "data": "", "error": "未绑定银行卡"}))


# 银行卡绑定
# @login_required
def bankbg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        bank = request.POST.get('bank')
        bankno = request.POST.get('bankno')
        tradepwd = make_password(request.POST.get('paypwd'), None, 'pbkdf2_sha1')
        user = request.user
        if user:
            Bank.objects.create(user=user, username=username, bank=bank, bankNo=bankno, tradepwd=tradepwd)
            return HttpResponse(json.dumps({"result": True, "data": "绑定成功", "error": ""}))
        else:
            return HttpResponse(json.dumps({"result": False, "data": "", "error": "用户不存在"}))


# 个人信息展示
def info(request):
    user = request.user
    fund = Fund.objects.filter(user=user).first()
    hold = Hold.objects.filter(user=user).first()
    money = str(fund.money)
    frozenmoney = str(fund.frozen_money)
    samount = str(hold.amount)
    sfrozen = str(hold.frozen)
    print(sfrozen)
    data = {}
    data['money'] = money
    data['frozenmoney'] = frozenmoney
    data['samount'] = samount
    data['sfrozen'] = sfrozen
    return HttpResponse(json.dumps({"result": True, "data": data, "error": ""}))


# 修改密码
# @login_required
def change_pwd(request):
    if request.method == 'POST':
        username = request.user.username
        print(request.user)
        oldpassword = request.POST.get('oldpassword')
        newpassword = request.POST.get('newpassword')
        conpassword = request.POST.get('conpassword')
        user = authenticate(username=username, password=oldpassword)
        if user:
            if newpassword and conpassword:
                if newpassword == conpassword:
                    password = make_password(newpassword, auth_check, 'pbkdf2_sha1')
                    UserInfo.objects.filter(username=user.username).update(password=password)
                    logout(request)
                    return HttpResponse(json.dumps({"result": True, "data": "修改成功", "error": ""}))
                else:
                    return HttpResponse(json.dumps({"result": False, "data": "", "error": "两次密码不一致"}))
            else:
                return HttpResponse(json.dumps({"result": False, "data": "", "error": "新密码不允许为空"}))
        else:
            return HttpResponse(json.dumps({"result": False, "data": "", "error": "旧密码错误"}))
    if request.method == 'GET':
        return HttpResponse(json.dumps({"result": True, "data": "", "error": ""}))



