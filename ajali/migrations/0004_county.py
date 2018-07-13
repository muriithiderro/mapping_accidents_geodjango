# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-04 06:19
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajali', '0003_auto_20180702_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField()),
                ('area', models.FloatField()),
                ('perimeter', models.FloatField()),
                ('county3_field', models.FloatField()),
                ('county3_id', models.FloatField()),
                ('county', models.CharField(max_length=20)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
