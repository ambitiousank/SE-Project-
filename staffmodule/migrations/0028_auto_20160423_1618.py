# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-23 10:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staffmodule', '0027_auto_20160423_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postapplied',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staffmodule.PostRef'),
        ),
    ]
