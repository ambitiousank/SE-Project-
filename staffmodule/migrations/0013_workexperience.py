# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffmodule', '0012_delete_workexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('roll_number', models.CharField(max_length=32)),
                ('last_organisation', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('job_description', models.CharField(max_length=100)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
