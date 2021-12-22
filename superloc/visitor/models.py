from django.db import models

GEARS_CHOICES = (
    ('M', 'Manuelle'),
    ('A', 'Automatique'),
    ('MA', 'Manuelle ou Automatique')
)

ENERGY_CHOICES = (
    ('G', 'Essence'),
    ('D', 'Diesel'),
    ('GD', 'Essence ou Diesel'),
    ('E', 'Electrique'),
    ('H', 'Hybride')
)

class Category(models.Model):
    code = models.CharField(max_length=1, unique=True)
    label = models.CharField(max_length=30, default='default')
    sample = models.CharField(max_length=30, default='default')
    image = models.ImageField(upload_to='static/visitor/images', max_length=300, default='static/visitor/images')
    description = models.TextField(null=True)
    nb_seats = models.IntegerField(default=5)
    nb_luggage = models.IntegerField(default=0)
    nb_doors = models.IntegerField(default=5)
    gear = models.CharField(max_length=2, choices=GEARS_CHOICES, default='MA')
    energy = models.CharField(max_length=2, choices=ENERGY_CHOICES, default='GD')
    climate_control = models.BooleanField(default=True)
    winter = models.BooleanField(default=False)
    pre_pay = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    equivalent = models.TextField(null=True)

    class Meta:
        verbose_name = 'Categorie'
        ordering = ['code']

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.id, self.code, self.label, self.sample)