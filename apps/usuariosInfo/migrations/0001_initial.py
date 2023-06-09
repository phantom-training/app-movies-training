# Generated by Django 4.1.7 on 2023-04-13 21:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsuariosInfoEntity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'USUARIOS_INFO',
            },
        ),
    ]
