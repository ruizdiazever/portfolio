# Generated by Django 3.2.3 on 2021-05-28 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20210528_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculum',
            name='title',
            field=models.CharField(blank=True, max_length=30, verbose_name='Titulo'),
        ),
    ]
