# Generated by Django 2.0 on 2017-12-27 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20171227_2329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expensetype',
            options={},
        ),
        migrations.RemoveField(
            model_name='expensetype',
            name='label',
        ),
    ]
