# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-24 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffmodule', '0033_auto_20160424_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissiondetail',
            name='validated_by',
            field=models.CharField(default='ok', max_length=32),
        ),
        migrations.AlterField(
            model_name='admissiondetail',
            name='validation_comments',
            field=models.CharField(blank=True, default='NA', max_length=400),
        ),
    ]
