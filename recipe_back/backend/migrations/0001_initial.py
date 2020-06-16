# Generated by Django 3.0.3 on 2020-06-16 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cadastrado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256, unique=True)),
                ('slug', models.SlugField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cadastrado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.TextField(db_index=True, max_length=128)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='')),
                ('descricao', models.TextField(blank=True, max_length=1024, null=True)),
                ('tempo_preparo', models.CharField(max_length=128)),
                ('porcoes', models.CharField(max_length=2)),
                ('ingredientes', models.TextField(max_length=1024)),
                ('slug', models.SlugField(max_length=128)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='backend.Autor')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='backend.Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cadastrado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(db_index=True, max_length=128)),
                ('sexo', models.CharField(blank=True, max_length=1, null=True)),
                ('cpf', models.CharField(blank=True, max_length=14, null=True, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('endereco', models.TextField(blank=True, max_length=512, null=True)),
                ('cep', models.CharField(blank=True, max_length=10, null=True)),
                ('estado_uf', models.CharField(blank=True, max_length=2, null=True)),
                ('cidade', models.CharField(blank=True, max_length=64, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='autor',
            name='perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Perfil'),
        ),
    ]
