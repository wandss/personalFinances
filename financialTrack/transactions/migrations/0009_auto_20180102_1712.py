# Generated by Django 2.0 on 2018-01-02 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_auto_20171229_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensetype',
            name='label',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
