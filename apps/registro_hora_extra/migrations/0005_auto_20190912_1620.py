# Generated by Django 2.2.4 on 2019-09-12 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0004_registrohoraextra_horas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrohoraextra',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionario.Funcionario'),
        ),
    ]
