from django.contrib import admin
from .models import *


# Register your models here.
class PublisherManager(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Publisher, PublisherManager)


class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'publisher_id']
    list_filter = ['publisher']


admin.site.register(Book, BookManager)
