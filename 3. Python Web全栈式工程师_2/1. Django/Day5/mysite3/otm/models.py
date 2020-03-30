from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField('名称', max_length=50, unique=True)

    def __str__(self):
        return '出版社：%s' % self.name


class Book(models.Model):
    title = models.CharField('书名', max_length=50)
    publisher = models.ForeignKey(Publisher)

    def __str__(self):
        return '书名：%s' % self.title
