# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 21:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videogames', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('rating', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1)),
                ('heading', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('body', models.CharField(default=' ', max_length=300)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('username', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='videogame',
            options={},
        ),
        migrations.RemoveField(
            model_name='developer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='id',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='id',
        ),
        migrations.RemoveField(
            model_name='videogame',
            name='id',
        ),
        migrations.RemoveField(
            model_name='videogame',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='videogame',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='videogame',
            name='release_date',
        ),
        migrations.AddField(
            model_name='developer',
            name='headquarters',
            field=models.CharField(default='london', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='developer',
            name='market',
            field=models.IntegerField(choices=[(1, 'Worldwide'), (2, 'Regional'), (3, 'Country')], default=1),
        ),
        migrations.AddField(
            model_name='platform',
            name='consoleType',
            field=models.IntegerField(choices=[(1, 'Console'), (2, 'Handheld'), (3, 'Mobile'), (4, 'PC')], default=1),
        ),
        migrations.AddField(
            model_name='platform',
            name='manufactorer',
            field=models.CharField(default='Unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='developer',
            name='developer',
            field=models.CharField(max_length=150, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='platform',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videogames.Developer'),
        ),
        migrations.RemoveField(
            model_name='videogame',
            name='genre',
        ),
        migrations.AddField(
            model_name='videogame',
            name='genre',
            field=models.ManyToManyField(to='videogames.Genre'),
        ),
        migrations.RemoveField(
            model_name='videogame',
            name='platform',
        ),
        migrations.AddField(
            model_name='videogame',
            name='platform',
            field=models.ManyToManyField(to='videogames.Platform'),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='title',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.AddField(
            model_name='review',
            name='videogame',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='videogame_review', to='videogames.VideoGame'),
        ),
    ]
