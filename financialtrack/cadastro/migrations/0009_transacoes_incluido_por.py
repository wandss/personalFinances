# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0008_transacoes_estabelecimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacoes',
            name='incluido_por',
            field=models.CharField(default='wand', max_length=500),
            preserve_default=False,
        ),
    ]
