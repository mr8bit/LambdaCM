# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_project_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.BooleanField(default=False, verbose_name='Гавная новость'),
        ),
    ]