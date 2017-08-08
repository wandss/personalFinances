# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_auto_20170629_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacoes',
            name='nome',
            field=models.ForeignKey(to='cadastro.TipoDespesa'),
        ),
        migrations.AlterField(
            model_name='transacoes',
            name='tipo',
            field=models.CharField(max_length=2, choices=[('cr\xe9dito', '+'), ('d\xe9bito', '-')]),
        ),
    ]
