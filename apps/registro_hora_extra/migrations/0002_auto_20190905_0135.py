# Generated by Django 2.2.4 on 2019-09-05 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrohoraextra',
            name='motivo',
            field=models.CharField(max_length=100, verbose_name='Registro de Hora Extra'),
        ),
    ]
