# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karaoke', '0003_auto_20161228_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
