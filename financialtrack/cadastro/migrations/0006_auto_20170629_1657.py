# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_auto_20170629_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacoes',
            name='tipo',
            field=models.CharField(max_length=2, choices=[('cr\xe9dito', 'Cr\xe9dito'), ('d\xe9bito', 'D\xe9bito')]),
        ),
    ]
