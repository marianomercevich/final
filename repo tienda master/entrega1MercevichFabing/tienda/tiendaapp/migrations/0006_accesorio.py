# Generated by Django 4.0.5 on 2022-07-16 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaapp', '0005_indumentaria'),
    ]

    operations = [
        migrations.CreateModel(
            name='accesorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30, verbose_name='Marca')),
                ('tipo', models.CharField(max_length=30, verbose_name='Tipo')),
                ('talle', models.CharField(max_length=6, verbose_name='Tipo')),
                ('precio', models.FloatField(verbose_name='Precio $')),
            ],
        ),
    ]