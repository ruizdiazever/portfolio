# Generated by Django 3.0.5 on 2020-05-01 16:21

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Nombre')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Descripcion')),
            ],
        ),
    ]
