# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 06:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solos', '0005_auto_20171011_0621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solo',
            name='album',
        ),
    ]
