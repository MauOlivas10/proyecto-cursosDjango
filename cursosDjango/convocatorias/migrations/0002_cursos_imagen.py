# Generated by Django 4.0.5 on 2022-06-30 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocatorias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía'),
        ),
    ]
