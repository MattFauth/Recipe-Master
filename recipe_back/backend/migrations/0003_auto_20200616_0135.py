# Generated by Django 3.0.3 on 2020-06-16 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200616_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='backend.Perfil'),
        ),
    ]
