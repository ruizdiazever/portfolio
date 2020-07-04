# Generated by Django 3.0.7 on 2020-06-29 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200503_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='certifications', verbose_name='Imagen')),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]