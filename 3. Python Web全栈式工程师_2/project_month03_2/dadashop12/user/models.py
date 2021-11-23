from django.db import models


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=11, verbose_name='用户名', unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    is_active = models.BooleanField(default=False, verbose_name='激活状态')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_user_profile'

    def __str__(self):
        return '%s_%s' % (self.id, self.username)


class Address(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    receiver = models.CharField(verbose_name='收件人名', max_length=11)
    address = models.CharField(verbose_name='用户地址', max_length=100)
    is_default = models.BooleanField(verbose_name='是否为默认地址', default=False)
    is_active = models.BooleanField(verbose_name='是否活跃', default=True)
    postcode = models.CharField(verbose_name='邮编', max_length=7)
    receiver_mobile = models.CharField(verbose_name='收件人电话', max_length=11)
    tag = models.CharField(verbose_name='标签', max_length=10)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class WeiboProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, null=True)
    wuid = models.CharField(verbose_name='微博uid', max_length=10, unique=True)
    access_token = models.CharField(verbose_name='权限令牌', max_length=32)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_weibo_profile'

    def __str__(self):
        return self.wuid
