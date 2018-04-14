# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-13 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_subscription', '0009_subscribepaper_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribepaper',
            name='vendor',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='myvendor', to='Vendor.Vendor', verbose_name='Vendor'),
        ),
    ]
