# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20170629_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacoes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=100)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('valor', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Transa\xe7\xf5es',
            },
        ),
        migrations.AlterModelOptions(
            name='tipodespesa',
            options={'verbose_name_plural': 'Tipos de Depesas'},
        ),
        migrations.AddField(
            model_name='transacoes',
            name='tipo',
            field=models.ForeignKey(to='cadastro.TipoDespesa'),
        ),
    ]
