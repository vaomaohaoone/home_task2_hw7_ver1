# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 01:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoadMap',
            fields=[
                ('rd_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('in_progress', 'in_progress'), ('ready', 'ready')], default='in_progress', max_length=11)),
                ('estimate', models.DateField(default=django.utils.timezone.now)),
                ('my_id', models.AutoField(primary_key=True, serialize=False)),
                ('road_map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='myapp.RoadMap')),
            ],
            options={
                'ordering': ['title', 'state', 'estimate'],
            },
        ),
    ]