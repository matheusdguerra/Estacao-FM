# Generated by Django 4.0.3 on 2022-03-16 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entidade', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
                ('localidade', models.CharField(max_length=50)),
                ('frequencia', models.CharField(max_length=50)),
            ],
        ),
    ]
