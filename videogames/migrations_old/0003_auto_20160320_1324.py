# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 13:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videogames', '0002_auto_20160319_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videogame',
            name='developers',
        ),
        migrations.RemoveField(
            model_name='videogame',
            name='platforms',
        ),
        migrations.RemoveField(
            model_name='videogame',
            name='publishers',
        ),
        migrations.RemoveField(
            model_name='videogame',
            name='rating',
        ),
    ]
