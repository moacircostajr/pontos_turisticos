# Generated by Django 3.2.8 on 2021-10-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracao', '0001_initial'),
        ('ponto_turistico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracao',
            field=models.ManyToManyField(to='atracao.Atracao'),
        ),
    ]
