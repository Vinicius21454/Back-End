# Generated by Django 5.2.1 on 2025-05-16 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('capacidade', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='autorizacoes',
            field=models.CharField(choices=[('G', 'Gestor'), ('C', 'Comum')], default='C', max_length=1),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reserva', models.DateField()),
                ('horario_inicio', models.TimeField()),
                ('horario_fim', models.TimeField()),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Funcionarios.disciplina')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Funcionarios.salas')),
            ],
        ),
    ]
