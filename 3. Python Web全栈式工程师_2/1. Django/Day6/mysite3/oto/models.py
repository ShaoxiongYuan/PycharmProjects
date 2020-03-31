from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=11, verbose_name="作家名称")

    def __str__(self):
        return '作者名字：%s' % self.name


class Wife(models.Model):
    name = models.CharField(verbose_name="妻子名称", max_length=11)
    author = models.OneToOneField(Author)

    def __str__(self):
        return '妻子名字：%s' % self.name
