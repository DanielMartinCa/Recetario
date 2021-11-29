# Generated by Django 3.2.9 on 2021-11-27 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0018_auto_20211127_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='file',
            field=models.ImageField(height_field='alto', upload_to='imagenes/', verbose_name='imagen', width_field='ancho'),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]
