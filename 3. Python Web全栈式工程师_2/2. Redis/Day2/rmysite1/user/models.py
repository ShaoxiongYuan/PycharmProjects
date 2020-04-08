from django.db import models


# Create your models here.
class User(models.Model):
    nickname = models.CharField('名称', max_length=11)
    age = models.IntegerField('年龄', default=0)
