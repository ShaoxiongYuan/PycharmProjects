from django.db import models

from goods.models import SKU
from tools.abstract_models import BaseModel
from user.models import UserProfile

# Create your models here.
STATUS = (
    (1, '待付款'),
    (2, '待发货'),
    (3, '待收货'),
    (4, '订单完成')
)


class OrderInfo(BaseModel):
    order_id = models.CharField(max_length=64, primary_key=True, verbose_name='订单号')
    user = models.ForeignKey(UserProfile)
    total_count = models.IntegerField(default=1, verbose_name='商品总数')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品总金额')
    freight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='运费')
    pay_method = models.SmallIntegerField(default=1, verbose_name='支付方式')

    # 订单地址
    receiver = models.CharField(max_length=10, verbose_name='收件人')
    address = models.CharField(max_length=100, verbose_name='收获地址')
    receiver_mobile = models.CharField(verbose_name='收件人联系电话', max_length=11)
    tag = models.CharField(verbose_name='标签', max_length=10)

    status = models.SmallIntegerField(verbose_name='订单状态', choices=STATUS)

    class Meta:
        db_table = 'order_order_info'

    def __str__(self):
        return self.order_id


class OrderGoods(BaseModel):
    order_info = models.ForeignKey(OrderInfo)
    sku = models.ForeignKey(SKU)
    count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_order_goods'

    def __str__(self):
        return '%s_%s' % (self.count, self.price)
