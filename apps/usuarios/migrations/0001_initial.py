# Generated by Django 4.1.7 on 2023-06-15 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuariosInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuariosEntity',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nick', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuariosInfo.usuariosinfoentity')),
            ],
            options={
                'db_table': 'USUARIOS',
            },
        ),
    ]
