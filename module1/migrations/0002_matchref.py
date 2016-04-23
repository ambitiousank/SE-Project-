# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-23 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchRef',
            fields=[
                ('match_id', models.AutoField(primary_key=True, serialize=False)),
                ('roll_no', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
