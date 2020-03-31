from .models import *
from django.contrib import admin


# Register your models here.
class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub', 'price', 'market_price']
    list_display_links = ['title']
    list_filter = ['pub']
    list_editable = ['price', 'market_price']
    search_fields = ['title']


admin.site.register(Book, BookManager)


class AuthorManager(admin.ModelAdmin):
    list_display = ['name', 'age', 'email']
    search_fields = ['name']


admin.site.register(Author, AuthorManager)
