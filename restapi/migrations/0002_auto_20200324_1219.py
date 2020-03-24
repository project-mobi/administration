# Generated by Django 3.0.4 on 2020-03-24 12:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='machine',
            options={'ordering': ['created']},
        ),
        migrations.RemoveField(
            model_name='machine',
            name='provider',
        ),
        migrations.AddField(
            model_name='location',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(default='testlocation', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='short_name',
            field=models.CharField(default='TES1', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machine',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]