# Generated by Django 3.0.7 on 2020-06-29 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_certification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, verbose_name='Titulo')),
                ('image', models.ImageField(blank=True, null=True, upload_to='certifications', verbose_name='Imagen')),
                ('link', models.URLField(blank=True, null=True)),
                ('ordering', models.FloatField(default=0, verbose_name='Orden')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
        ),
        migrations.DeleteModel(
            name='Certification',
        ),
    ]
