# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-02 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0024_auto_20170802_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransacoesRepetidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pk_list', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='transacoes',
            name='repeat_ids',
        ),
    ]
