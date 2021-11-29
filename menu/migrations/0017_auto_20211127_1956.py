# Generated by Django 3.2.9 on 2021-11-27 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0016_auto_20211127_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImgIngre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('imagen', models.FileField(blank=True, upload_to='imagenes/ingredientes')),
            ],
        ),
        migrations.CreateModel(
            name='ImgReceta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('imagen', models.FileField(blank=True, upload_to='imagenes/recetas')),
            ],
        ),
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
            name='imagen',
            field=models.ManyToManyField(blank=True, to='menu.ImgIngre'),
        ),
        migrations.AddField(
            model_name='receta',
            name='imagen',
            field=models.ManyToManyField(blank=True, to='menu.ImgReceta'),
        ),
    ]
