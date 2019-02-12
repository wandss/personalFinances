# Generated by Django 2.0 on 2018-01-05 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_navbydate'),
    ]

    operations = [
        migrations.AddField(
            model_name='dropdownmenu',
            name='is_navbar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='navbydate',
            name='is_navbar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='navmenu',
            name='is_navbar',
            field=models.BooleanField(default=False),
        ),
    ]
