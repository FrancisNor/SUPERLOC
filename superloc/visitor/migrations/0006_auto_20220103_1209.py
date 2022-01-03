# Generated by Django 3.2.9 on 2022-01-03 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0005_remove_agency_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='email',
            field=models.CharField(default=0, max_length=30, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agency',
            name='phone',
            field=models.CharField(default=0, max_length=10, verbose_name='Téléphone'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agency',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Adresse'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Ville'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='zip_code',
            field=models.CharField(max_length=5, verbose_name='Code postal'),
        ),
        migrations.AlterField(
            model_name='category',
            name='climate_control',
            field=models.BooleanField(default=True, verbose_name='Climatisation'),
        ),
        migrations.AlterField(
            model_name='category',
            name='energy',
            field=models.CharField(choices=[('G', 'Essence'), ('D', 'Diesel'), ('GD', 'Essence ou Diesel'), ('E', 'Electrique'), ('H', 'Hybride')], default='GD', max_length=2, verbose_name='Energie'),
        ),
        migrations.AlterField(
            model_name='category',
            name='equivalent',
            field=models.TextField(null=True, verbose_name='Modèles équivalents'),
        ),
        migrations.AlterField(
            model_name='category',
            name='gear',
            field=models.CharField(choices=[('M', 'Manuelle'), ('A', 'Automatique'), ('MA', 'Manuelle ou Automatique')], default='MA', max_length=2, verbose_name='Type de boite'),
        ),
        migrations.AlterField(
            model_name='category',
            name='label',
            field=models.CharField(default='default', max_length=30, verbose_name='Nom de la catégorie'),
        ),
        migrations.AlterField(
            model_name='category',
            name='nb_doors',
            field=models.IntegerField(default=5, verbose_name='Nombre de portes'),
        ),
        migrations.AlterField(
            model_name='category',
            name='nb_luggage',
            field=models.IntegerField(default=0, verbose_name='Nombre de bagages'),
        ),
        migrations.AlterField(
            model_name='category',
            name='nb_seats',
            field=models.IntegerField(default=5, verbose_name='Nombre de places'),
        ),
        migrations.AlterField(
            model_name='category',
            name='pre_pay',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Montant du pré-paiement'),
        ),
        migrations.AlterField(
            model_name='category',
            name='sample',
            field=models.CharField(default='default', max_length=30, verbose_name='Modèle principal'),
        ),
        migrations.AlterField(
            model_name='category',
            name='winter',
            field=models.BooleanField(default=False, verbose_name='Equipé hiver'),
        ),
    ]
