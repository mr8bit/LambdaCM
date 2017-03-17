# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20170315_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='sub_name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='name',
            field=models.CharField(choices=[('mdi-github-circle', 'GitHub'), ('mdi-twitter', 'Twitter'), ('mdi-gmail', 'Mail'), ('mdi-vk', 'VK'), ('mdi-facebook', 'Facebook')], max_length=300, verbose_name='Название социальной сети'),
        ),
    ]
