# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0038_question_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='ans',
            field=models.CharField(default=b'NULL', max_length=2000),
        ),
    ]