# Generated by Django 2.0 on 2017-12-27 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('dt_creation', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['label'],
            },
        ),
    ]
