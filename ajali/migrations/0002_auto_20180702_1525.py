# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-02 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajali', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='car',
            name='last_name',
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.CharField(default='name', max_length=255),
        ),
    ]
