# Generated by Django 2.0 on 2017-12-27 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_auto_20171227_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navmenu',
            name='link',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
