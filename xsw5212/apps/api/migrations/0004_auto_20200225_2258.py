# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-25 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200225_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='qq',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.CharField(default='', max_length=32),
        ),
    ]