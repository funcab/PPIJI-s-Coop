# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-10-02 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20181001_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', verbose_name=b''),
            preserve_default=False,
        ),
    ]
