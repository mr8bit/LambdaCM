# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0010_auto_20170312_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='slug',
            field=models.SlugField(default=2),
            preserve_default=False,
        ),
    ]
