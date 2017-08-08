# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainmenu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Menu',
            new_name='MainMenu',
        ),
    ]
