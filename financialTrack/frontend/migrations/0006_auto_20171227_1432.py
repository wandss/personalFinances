# Generated by Django 2.0 on 2017-12-27 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_auto_20171227_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenu',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='title', to='frontend.NavMenu'),
        ),
    ]
