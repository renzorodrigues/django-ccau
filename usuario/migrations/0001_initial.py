# Generated by Django 2.1.3 on 2018-12-09 00:27

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('turma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.CreateModel(
            name='Atendido',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuario.Usuario')),
                ('matricula', models.CharField(max_length=10, unique=True, verbose_name='Matrícula')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=2, verbose_name='Sexo')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('data_matricula', models.DateField(blank=True, null=True, verbose_name='Data de Matrícula')),
            ],
            options={
                'verbose_name': 'Atendido',
                'verbose_name_plural': 'Atendidos',
            },
            bases=('usuario.usuario',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Avaliador',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuario.Usuario')),
                ('cargo', models.CharField(max_length=50, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Avaliador',
                'verbose_name_plural': 'Avaliadores',
            },
            bases=('usuario.usuario',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuario.Usuario')),
                ('nome2', models.CharField(choices=[('PA', 'Pai'), ('MA', 'Mãe'), ('RL', 'Responsável Legal')], max_length=2, verbose_name='Nome do responsável 2')),
                ('parentesco_responsavel', models.CharField(max_length=50, verbose_name='Parentesco')),
            ],
            options={
                'verbose_name': 'Responsável',
                'verbose_name_plural': 'Responsáveis',
            },
            bases=('usuario.usuario',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='atendido',
            name='responsaveis',
            field=models.ManyToManyField(to='usuario.Responsavel'),
        ),
        migrations.AddField(
            model_name='atendido',
            name='turma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='turma.Turma'),
        ),
    ]
