# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportparken', '0005_sportparkobjectgeometry_ondergrond'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportparkgeometry',
            name='verhuurprijs',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='sportparkobjectgeometry',
            name='verhuurprijs',
            field=models.FloatField(null=True),
        ),
    ]
