# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 14:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20160522_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='upload_image',
        ),
    ]