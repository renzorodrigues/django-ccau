# Generated by Django 2.1.3 on 2018-11-19 00:12

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidade', models.CharField(choices=[('CN', 'CANAÃ'), ('SP', 'SHOPPING PARK'), ('JG', 'JARAGUÁ'), ('PN', 'PLANALTO'), ('PQ', 'PEQUIS')], max_length=2, verbose_name='Unidade')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Unidade',
                'verbose_name_plural': 'Unidades',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
