# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-05 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20180405_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.FileField(default='/media/background3.jpg', null=True, upload_to='employees'),
        ),
    ]