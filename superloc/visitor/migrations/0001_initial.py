# Generated by Django 3.2.9 on 2021-12-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1, unique=True)),
                ('label', models.CharField(default='default', max_length=30)),
                ('sample', models.CharField(default='default', max_length=30)),
                ('image', models.ImageField(default='static/visitor/images', max_length=300, upload_to='static/visitor/images')),
                ('description', models.TextField(null=True)),
                ('nb_seats', models.IntegerField(default=5)),
                ('nb_luggage', models.IntegerField(default=0)),
                ('nb_doors', models.IntegerField(default=5)),
                ('gear', models.CharField(choices=[('M', 'Manuelle'), ('A', 'Automatique'), ('MA', 'Manuelle ou Automatique')], default='MA', max_length=2)),
                ('energy', models.CharField(choices=[('G', 'Essence'), ('D', 'Diesel'), ('GD', 'Essence ou Diesel'), ('E', 'Electrique'), ('H', 'Hybride')], default='GD', max_length=2)),
                ('climate_control', models.BooleanField(default=True)),
                ('winter', models.BooleanField(default=False)),
                ('pre_pay', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('equivalent', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Categorie',
                'ordering': ['code'],
            },
        ),
    ]
