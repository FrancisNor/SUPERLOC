# Generated by Django 3.2.9 on 2022-01-03 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0007_auto_20220103_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='media/visitor', max_length=300, upload_to='media/visitor'),
        ),
    ]
