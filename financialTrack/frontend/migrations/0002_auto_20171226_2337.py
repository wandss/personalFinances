# Generated by Django 2.0 on 2017-12-26 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('icon', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='NavBar',
        ),
    ]
