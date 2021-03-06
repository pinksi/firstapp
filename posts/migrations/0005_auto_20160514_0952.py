# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 09:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_upload_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='types',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='posts.Types'),
            preserve_default=False,
        ),
    ]
