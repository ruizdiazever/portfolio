# Generated by Django 3.0.7 on 2020-07-03 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200628_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=150, verbose_name='Titulo'),
        ),
    ]