# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionDetail',
            fields=[
                ('admission_id', models.AutoField(primary_key=True, serialize=False)),
                ('roll_number', models.CharField(max_length=32, unique=True)),
                ('status_of_request', models.IntegerField()),
                ('validated_by', models.CharField(max_length=32)),
            ],
        ),
    ]
