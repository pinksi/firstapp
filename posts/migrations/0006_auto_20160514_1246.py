# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20160514_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='types',
            name='types_title',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
