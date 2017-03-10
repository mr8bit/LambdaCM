# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_auto_20170310_0941'),
        ('blog', '0002_auto_20170309_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='seo',
            name='project',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='team.Project'),
        ),
    ]