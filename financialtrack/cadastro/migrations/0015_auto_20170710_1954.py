# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0014_auto_20170707_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacoes',
            name='tipo_trans',
            field=models.IntegerField(choices=[(1, 'Dédito'), (2, 'Crédito')]),
        ),
    ]
