from django.db import models
from userinfo.models import *
from stocks.models import *


# Create your models here.
BOS_CHOICES = (
    (0, 'Buy'),
    (1, 'Sell'),
)


class SelfStock(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name='用户')
    stock = models.ForeignKey(Stock, verbose_name='股票')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'SelfStock'
        verbose_name = '自选股'
        verbose_name_plural = verbose_name


class BOSStock(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name='用户')
    stock = models.ForeignKey(Stock, verbose_name='股票')
    role = models.IntegerField(choices=BOS_CHOICES, default=0, verbose_name='角色')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='买卖价格')
    amount = models.IntegerField(verbose_name="买卖数量")
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='挂单日期')

    def __str__(self):
        return self.user.username

    def get_datetime(self):
        datetime = self.datetime.strftime('%Y-%m-%d %H:%M:%S')
        return datetime

    def get_role(self):
        if self.role == 0:
            return u'买入'
        else:
            return u'卖出'

    class Meta:
        db_table = 'BOSStock'
        verbose_name = '买卖挂单'
        verbose_name_plural = verbose_name
        ordering = ['-datetime']


class DealStock(models.Model):
    suser = models.ForeignKey(UserInfo, related_name='suser', verbose_name='卖家')
    buser = models.ForeignKey(UserInfo, related_name='buser', verbose_name='买家')
    price = models.DecimalField(max_digits=8, decimal_places=2,verbose_name='成交价格')
    amount = models.IntegerField(verbose_name='成交数量')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='成交日期')
    stock = models.CharField(max_length=400, verbose_name='股票信息')

    def get_datetime(self):
        datetime = self.datetime.strftime('%Y-%m-%d %H:%M:%S')
        return datetime

    class Meta:
        db_table = 'DealStock'
        verbose_name = '买卖成交'
        verbose_name_plural = verbose_name
        ordering = ['-datetime']
