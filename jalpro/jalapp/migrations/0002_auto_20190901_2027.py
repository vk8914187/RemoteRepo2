# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-01 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jalapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesdata',
            name='course_trainer_exp',
            field=models.IntegerField(),
        ),
    ]