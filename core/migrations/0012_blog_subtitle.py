# Generated by Django 3.0.7 on 2020-07-03 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_blog_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='subtitle',
            field=models.CharField(blank=True, max_length=150, verbose_name='Subtitulo'),
        ),
    ]
