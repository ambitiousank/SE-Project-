# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffmodule', '0014_programapplied'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetail',
            name='category_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='current_address_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='pan_card',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='residential_address_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='gender',
            field=models.IntegerField(),
        ),
    ]
