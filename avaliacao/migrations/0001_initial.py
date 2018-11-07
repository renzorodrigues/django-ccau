# Generated by Django 2.1.3 on 2018-11-07 01:20

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demanda', models.CharField(choices=[('IT', 'Instituição'), ('FM', 'Família'), ('PR', 'Próprio')], max_length=2, verbose_name='Demanda')),
                ('queixa', models.CharField(max_length=100, verbose_name='Queixa')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('data_criacao', models.DateTimeField(auto_now=True, verbose_name='Data de Criação')),
                ('atendido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Atendido')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]