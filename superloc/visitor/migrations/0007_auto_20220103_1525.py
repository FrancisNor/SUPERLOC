# Generated by Django 3.2.9 on 2022-01-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0006_auto_20220103_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='email',
            field=models.CharField(max_length=50, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nom'),
        ),
    ]
