from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField("书名", max_length=50, default='', unique=True)
    pub = models.CharField("出版社", max_length=200, default='')
    price = models.DecimalField("定价", max_digits=7, decimal_places=2, default=0.0)
    market_price = models.DecimalField("零售价", max_digits=7, decimal_places=2, default=0.0)
    is_active = models.BooleanField("是否活跃", default=True)

    def __str__(self):
        return "书名: %s, 出版社: %s, 定价: %s, 零售价: %s" % (self.title, self.pub, self.price, self.market_price)


class Author(models.Model):
    name = models.CharField("姓名", max_length=50, default='')
    age = models.IntegerField("年龄", default=1)
    email = models.EmailField("邮箱", null=True)

    def __str__(self):
        return "姓名: %s, 年龄: %s, 邮箱: %s" % (self.name, self.age, self.email)
