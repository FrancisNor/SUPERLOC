# Generated by Django 3.2.9 on 2022-01-04 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visitor', '0011_auto_20220103_2324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'ordering': ['manufacturer', 'car_model', 'registration_number'], 'verbose_name': 'Véhicule'},
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_type', models.CharField(choices=[('PRI', 'Particulier'), ('PRO', 'Professionnel')], default='PRI', max_length=3, verbose_name='Type de client')),
                ('date_of_birth', models.DateTimeField(verbose_name='Date de naissance')),
                ('address', models.CharField(max_length=100, verbose_name='Adresse')),
                ('zipcode', models.CharField(max_length=5, verbose_name='Code postal')),
                ('city', models.CharField(max_length=50, verbose_name='Ville')),
                ('phone', models.CharField(max_length=10, verbose_name='Téléphone')),
                ('licence_scan', models.ImageField(upload_to='customer_licences', verbose_name='Copie permis de conduire')),
                ('licence_number', models.CharField(max_length=12, verbose_name='Numéro du permis de conduire')),
                ('receiveAdds', models.BooleanField(default=True, verbose_name='Accepte de recevoir de la publicité ?')),
                ('creditCardNumber', models.CharField(max_length=16, verbose_name='Numéro de carte de paiement')),
                ('creditCardValidity', models.DateTimeField(verbose_name='Fin de validité de la carte de paiement')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Client',
            },
        ),
    ]
