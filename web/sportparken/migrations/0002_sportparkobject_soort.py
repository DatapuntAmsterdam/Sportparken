# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportparken', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Soort',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('soort', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='sportparkobject',
            name='omschrijving',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='sportparkobject',
            name='soort',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='soort_set', to='sportparken.Soort'),
        ),
    ]
