# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-14 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0004_vendor_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='email_id',
            field=models.EmailField(default='check@check.com', max_length=254),
            preserve_default=False,
        ),
    ]
