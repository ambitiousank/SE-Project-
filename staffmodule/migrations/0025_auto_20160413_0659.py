# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffmodule', '0024_auto_20160413_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressdetails',
            name='state',
            field=models.IntegerField(choices=[(0, 'Select'), (1, 'Andhra Pradesh'), (2, 'Arunachal Pradesh'), (3, 'Assam'), (4, 'Bihar'), (5, 'Chattisgarh'), (6, 'Karnataka')], default=0),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='category_id',
            field=models.IntegerField(choices=[(0, 'Select'), (1, 'Gen'), (2, 'SC/ST'), (3, 'OBC')], default=0),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Select'), (1, 'Male'), (2, 'Female'), (3, 'Others')], default=0),
        ),
        migrations.AlterField(
            model_name='postapplied',
            name='post',
            field=models.IntegerField(choices=[(0, 'Select'), (1, 'Software Engineer'), (2, 'Data Analyst'), (3, 'Software Developer'), (4, 'IT')], default=0),
        ),
        migrations.AlterField(
            model_name='programapplied',
            name='course_id',
            field=models.IntegerField(choices=[(0, 'Select'), (1, 'IT'), (2, 'ESD')], default=0),
        ),
        migrations.AlterField(
            model_name='programapplied',
            name='exam_name_id',
            field=models.IntegerField(choices=[(0, 'Select'), (1, 'GATE'), (2, 'GRE'), (3, 'JEE')], default=0),
        ),
        migrations.AlterField(
            model_name='programapplied',
            name='exam_subject_id',
            field=models.IntegerField(choices=[(0, 'Select'), (1, 'CS/IT'), (2, 'ECE')], default=0),
        ),
        migrations.AlterField(
            model_name='programapplied',
            name='program_id',
            field=models.IntegerField(choices=[(0, 'Select'), (1, 'M.Tech'), (2, 'Integrated M.Tech'), (3, 'M.Sc Digital Society'), (4, 'MS'), (5, 'PHD')], default=0),
        ),
    ]
