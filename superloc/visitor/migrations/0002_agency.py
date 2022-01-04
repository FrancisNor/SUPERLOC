# Generated by Django 3.2.9 on 2022-01-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('address_line_1', models.CharField(max_length=100)),
                ('address_line_2', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Agence',
                'ordering': ['name'],
            },
        ),
    ]