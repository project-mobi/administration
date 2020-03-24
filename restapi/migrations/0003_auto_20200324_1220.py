# Generated by Django 3.0.4 on 2020-03-24 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_auto_20200324_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='provider',
            field=models.ForeignKey(default='173014ee-5fdf-445a-984f-8398b79dc8e3', on_delete=django.db.models.deletion.CASCADE, to='restapi.Provider'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machine',
            name='provider',
            field=models.ForeignKey(default='173014ee-5fdf-445a-984f-8398b79dc8e3', on_delete=django.db.models.deletion.CASCADE, to='restapi.Provider'),
            preserve_default=False,
        ),
    ]
