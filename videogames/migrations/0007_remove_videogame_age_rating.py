# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 18:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videogames', '0006_auto_20160321_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videogame',
            name='age_rating',
        ),
    ]
