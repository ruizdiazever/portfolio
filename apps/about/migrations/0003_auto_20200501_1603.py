# Generated by Django 3.0.5 on 2020-05-01 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20200501_1601'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['created'], 'verbose_name': 'Descripcion', 'verbose_name_plural': 'Descripciones'},
        ),
    ]
