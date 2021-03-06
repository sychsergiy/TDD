# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 06:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solos', '0004_solo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solo',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.Album'),
        ),
        migrations.AlterField(
            model_name='solo',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.Track'),
        ),
    ]
