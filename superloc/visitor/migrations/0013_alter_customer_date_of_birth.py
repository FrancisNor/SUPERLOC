# Generated by Django 3.2.9 on 2022-01-04 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0012_auto_20220104_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_of_birth',
            field=models.DateField(verbose_name='Date de naissance'),
        ),
    ]
