# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-08 20:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coin_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holdings',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
