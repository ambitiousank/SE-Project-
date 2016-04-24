# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-24 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import staffmodule.models


class Migration(migrations.Migration):

    dependencies = [
        ('staffmodule', '0031_auto_20160423_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitStatus',
            fields=[
                ('roll_number', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('submission_status', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='PhotoFiles',
        ),
        migrations.DeleteModel(
            name='SignatureFiles',
        ),
        migrations.DeleteModel(
            name='XthMarksheets',
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='category_id',
            field=models.IntegerField(choices=[(0, 'Select'), (1, 'Gen'), (2, 'SC'), (3, 'ST'), (4, 'OBC')], default=0),
        ),
        migrations.AlterField(
            model_name='postapplied',
            name='post',
            field=models.IntegerField(choices=[(0, 'Select'), (1, 'Software Engineer'), (2, 'Data Analyst'), (3, 'Software Developer'), (4, 'IT')], default=0),
        ),
        migrations.AlterField(
            model_name='uploaddetails',
            name='upload_path',
            field=models.FileField(upload_to=b'/home/dragonwarrior/Django/testdjango/media/downloads'),
        ),
        migrations.AlterField(
            model_name='uploaddetails',
            name='upload_type',
            field=models.IntegerField(verbose_name=staffmodule.models.UploadTypeRef),
        ),
    ]
