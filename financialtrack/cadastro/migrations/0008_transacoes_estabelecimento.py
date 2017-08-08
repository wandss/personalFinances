# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0007_auto_20170629_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacoes',
            name='estabelecimento',
            field=models.CharField(default=datetime.datetime(2017, 6, 29, 20, 13, 18, 898000, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
