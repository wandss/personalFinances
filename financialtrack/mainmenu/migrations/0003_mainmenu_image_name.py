# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainmenu', '0002_auto_20170703_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainmenu',
            name='image_name',
            field=models.CharField(default='money.jpg', max_length=50),
            preserve_default=False,
        ),
    ]
