# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 22:19
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internet_available', models.BooleanField(verbose_name='Есть доступ к интернету')),
                ('take_computer', models.BooleanField(verbose_name='Брать компьютер')),
                ('site', models.URLField(verbose_name='Сайт мероприятия')),
                ('value', models.CharField(max_length=300, verbose_name='Стоимость')),
            ],
            options={
                'ordering': ('-event',),
                'verbose_name_plural': 'Дополнительная информация',
                'verbose_name': 'Дополнительная информация',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('start', models.DateTimeField(verbose_name='Начало')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='Окончание')),
                ('allow_comments', models.BooleanField(default=True, verbose_name='Открыть коменты?')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Статья')),
                ('featured_image', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Главное изображение')),
                ('profile_image', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Изображение профиля')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'ordering': ('-start',),
                'verbose_name_plural': 'Мероприятия',
                'verbose_name': 'Мероприятие',
            },
        ),
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500, verbose_name='Адресс')),
                ('name', models.CharField(blank=True, max_length=300, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Местоположения',
                'verbose_name': 'Местоположение',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventLocation', verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.Tag', verbose_name='Тэги'),
        ),
        migrations.AddField(
            model_name='additioninfo',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='event.Event'),
        ),
    ]
