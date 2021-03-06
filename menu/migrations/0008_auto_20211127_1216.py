# Generated by Django 3.2.9 on 2021-11-27 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_alter_receta_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alergia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la alergia')),
            ],
            options={
                'verbose_name': 'Persona',
            },
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu/static/img/'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu/static/img/'),
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.AddField(
            model_name='alergia',
            name='alergeno',
            field=models.ManyToManyField(to='menu.Ingrediente', verbose_name='Alergias del comensal'),
        ),
        migrations.AddField(
            model_name='alergia',
            name='plato',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.receta', verbose_name='Plato favorito'),
        ),
    ]
