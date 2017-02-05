# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-31 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import salon.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=salon.models.user_directory_path)),
                ('is_cover_photo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SalonStore',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('address_1', models.TextField()),
                ('address_2', models.TextField()),
                ('address_3', models.TextField()),
                ('state', models.CharField(choices=[('KA', 'Karnataka'), ('AP', 'Andhra Pradesh'), ('KL', 'Kerala'), ('TN', 'Tamil Nadu'), ('MH', 'Maharashtra'), ('UP', 'Uttar Pradesh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('RJ', 'Rajasthan'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('TG', 'Telangana'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chattisgarh'), ('HR', 'Haryana'), ('JH', 'Jharkhand'), ('MP', 'Madhya Pradesh'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Orissa'), ('PB', 'Punjab'), ('SK', 'Sikkim'), ('TR', 'Tripura'), ('UA', 'Uttarakhand'), ('WB', 'West Bengal'), ('AN', 'Andaman and Nicobar'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('LD', 'Lakshadweep'), ('PY', 'Pondicherry')], default='DL', max_length=128)),
                ('country', models.TextField(default='India')),
                ('contact_number', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='salon_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.SalonStore'),
        ),
    ]