# Generated by Django 3.0.3 on 2020-06-16 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200616_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='perfil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Perfil'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Autor'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='ingredientes',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='receita',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Tipo'),
        ),
    ]
