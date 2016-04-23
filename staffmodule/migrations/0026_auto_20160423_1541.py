# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-23 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffmodule', '0025_auto_20160413_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetail',
            name='current_address_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='residential_address_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='photofiles',
            name='photograph_file',
            field=models.FileField(null=True, upload_to=b'/home/dragonwarrior/Django/testdjango/media'),
        ),
        migrations.AlterField(
            model_name='signaturefiles',
            name='signature_file',
            field=models.FileField(null=True, upload_to=b'/home/dragonwarrior/Django/testdjango/media'),
        ),
        migrations.AlterField(
            model_name='xthmarksheets',
            name='xth_marksheet',
            field=models.FileField(null=True, upload_to=b'/home/dragonwarrior/Django/testdjango/media'),
        ),
    ]
