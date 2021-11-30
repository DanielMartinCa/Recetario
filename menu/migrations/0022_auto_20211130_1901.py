# Generated by Django 3.2.9 on 2021-11-30 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0021_auto_20211130_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alergia',
            name='alergeno',
        ),
        migrations.AlterField(
            model_name='alergia',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre de la alérgia'),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='alergeno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.alergia', verbose_name='Alergia'),
        ),
    ]
