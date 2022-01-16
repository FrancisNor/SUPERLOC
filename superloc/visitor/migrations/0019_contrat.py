# Generated by Django 3.2.8 on 2022-01-16 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0018_auto_20220112_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
                ('tarif_base', models.FloatField(null=True)),
                ('taux_tva', models.FloatField(default=20)),
                ('tva', models.FloatField(null=True)),
                ('prix_total', models.FloatField(default=0)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.agency')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='visitor.customer')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.vehicle')),
            ],
        ),
    ]
