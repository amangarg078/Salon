# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-03 00:29
from __future__ import unicode_literals

from django.db import migrations, models
import salon.models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0011_auto_20170203_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=salon.models.user_directory_path),
        ),
    ]
