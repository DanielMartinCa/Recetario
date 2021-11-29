# Generated by Django 3.2.9 on 2021-11-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0019_auto_20211127_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingrediente',
            name='image',
        ),
        migrations.RemoveField(
            model_name='receta',
            name='image',
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='urlimage',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='receta',
            name='urlimage',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Imagen'),
        ),
    ]
