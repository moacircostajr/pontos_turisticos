# Generated by Django 3.2.8 on 2021-10-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='latitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='longitude',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]