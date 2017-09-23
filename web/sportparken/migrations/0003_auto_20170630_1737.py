# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-30 17:37
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportparken', '0002_auto_20170923_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='huurder',
            name='bezoek_adres',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='huurder',
            name='post_adres',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        # migrations.AddField(
        #     model_name='sportparkobject',
        #     name='uid',
        #     field=models.CharField(max_length=20, null=True),
        # ),
    ]
