# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_auto_20170629_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transacoes',
            old_name='descricao',
            new_name='nome',
        ),
        migrations.AddField(
            model_name='transacoes',
            name='informacoes',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
