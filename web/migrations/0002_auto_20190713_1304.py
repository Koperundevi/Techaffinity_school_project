# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-13 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Marks',
            new_name='Mark',
        ),
        migrations.AlterField(
            model_name='student',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
