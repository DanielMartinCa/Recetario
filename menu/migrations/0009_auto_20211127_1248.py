# Generated by Django 3.2.9 on 2021-11-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_auto_20211127_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='image',
            field=models.ImageField(blank=True, height_field='200px', null=True, upload_to='menu/static/img/', width_field='200px'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='image',
            field=models.ImageField(blank=True, height_field='200px', null=True, upload_to='menu/static/img/', width_field='200px'),
        ),
    ]