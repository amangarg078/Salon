# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-01 22:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0007_photo_is_cover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='salon_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='salon.SalonStore'),
        ),
    ]