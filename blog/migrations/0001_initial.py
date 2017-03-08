# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 14:29
from __future__ import unicode_literals

import ckeditor.fields
import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields
import meta.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('sub_title', models.CharField(max_length=300, verbose_name='Слоган')),
                ('short_description', ckeditor.fields.RichTextField(verbose_name='Короткое описание')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Статья')),
                ('datetime_create', models.DateTimeField(auto_now_add=True)),
                ('datetime_updated', models.DateTimeField(auto_now=True)),
                ('main_image', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Image')),
                ('post_in_vk', models.BooleanField(default=False, verbose_name='Постить в вк?')),
                ('post_in_twitter', models.BooleanField(default=False, verbose_name='Постить в твиттер?')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name_plural': 'Посты',
                'verbose_name': 'Пост',
            },
            bases=(meta.models.ModelMeta, models.Model),
        ),
        migrations.CreateModel(
            name='SEO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soe_description', models.TextField(verbose_name='Seo Описание')),
                ('key_words', models.TextField(verbose_name='Ключ слова')),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='blog.Article')),
            ],
            options={
                'verbose_name_plural': 'SEO',
                'verbose_name': 'SEO',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Тэги',
                'verbose_name': 'Тэг',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='Тэги'),
        ),
    ]
