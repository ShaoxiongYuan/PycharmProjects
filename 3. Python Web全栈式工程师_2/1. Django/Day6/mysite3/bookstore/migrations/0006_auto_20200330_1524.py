# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-30 07:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('bookstore', '0005_book_is_active'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
    ]
