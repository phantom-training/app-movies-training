# Generated by Django 4.1.7 on 2023-06-17 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuariosInfo', '0001_initial'),
        ('usuarios', '0002_alter_usuariosentity_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariosentity',
            name='info',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='usuariosInfo.usuariosinfoentity'),
        ),
    ]
