# Generated by Django 4.0.3 on 2022-11-24 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0002_remove_contacto_trabajo_contacto_localidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='servicio',
            field=models.IntegerField(),
        ),
    ]
