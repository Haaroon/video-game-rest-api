# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videogames', '0005_remove_videogame_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videogame',
            name='genre',
        ),
        migrations.AddField(
            model_name='genre',
            name='games',
            field=models.ManyToManyField(to='videogames.VideoGame'),
        ),
    ]