# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-17 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('social', '0001_initial'),
        ('cargo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverycontract',
            name='dlvcontract_driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.UserPersonal'),
        ),
        migrations.AddField(
            model_name='deliverycontract',
            name='dlvcontract_freight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargo.Freight'),
        ),
    ]
