# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='answer',
            field=models.CharField(blank=True, default=None, max_length=17),
        ),
    ]
