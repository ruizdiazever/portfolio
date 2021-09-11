# Generated by Django 3.2.4 on 2021-09-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_projects_screen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/card', verbose_name='Card image'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='screen',
            field=models.ImageField(blank=True, null=True, upload_to='projects/modal', verbose_name='Modal image'),
        ),
    ]