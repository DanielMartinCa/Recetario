# Generated by Django 3.2.9 on 2021-11-27 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0015_auto_20211127_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu/static/img'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu/static/img'),
        ),
    ]
