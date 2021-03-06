# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 17:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='-unknown-', max_length=100)),
                ('description', models.CharField(default='No description', max_length=1000)),
                ('brief', models.CharField(default='No brief', max_length=200)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('developer', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='videogames.Developer')),
                ('genre', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='videogames.Genre')),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='videogames', to=settings.AUTH_USER_MODEL)),
                ('platform', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='videogames.Platform')),
                ('publisher', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='videogames.Publisher')),
                ('rating', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='videogames.Rating')),
            ],
            options={
                'ordering': ('release_date',),
            },
        ),
    ]
