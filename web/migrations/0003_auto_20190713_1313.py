# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-13 13:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20190713_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='student',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='subject',
        ),
        migrations.DeleteModel(
            name='Mark',
        ),
    ]