# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-01 21:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0004_auto_20170202_0248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='salon',
            new_name='salon_id',
        ),
    ]