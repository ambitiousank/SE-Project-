# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-10 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffmodule', '0022_auto_20160410_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetail',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
