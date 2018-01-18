# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-17 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryContract',
            fields=[
                ('dlvcontract_id', models.AutoField(primary_key=True, serialize=False)),
                ('dlvcontract_consumer', models.CharField(max_length=64)),
                ('dlvcontract_date_receive', models.DateField()),
                ('dlvcontract_time_receive', models.TimeField()),
                ('dlvcontract_delivery_date', models.DateField()),
                ('dlvcontract_delivery_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Freight',
            fields=[
                ('freight_id', models.AutoField(primary_key=True, serialize=False)),
                ('freight_description', models.CharField(max_length=40)),
                ('freight_comment', models.TextField(blank=True, max_length=150)),
                ('freight_category', models.CharField(max_length=30)),
                ('freight_length', models.FloatField(blank=True)),
                ('freight_width', models.FloatField(blank=True)),
                ('freight_height', models.FloatField(blank=True)),
                ('freight_weight', models.FloatField()),
                ('freight_first_date', models.DateField()),
                ('freight_latest_date', models.DateField()),
                ('freight_address_start', models.CharField(max_length=255)),
                ('freight_address_finish', models.CharField(max_length=255)),
            ],
        ),
    ]
