from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

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
    label = models.CharField('Nom de la catégorie', max_length=30)
    sample = models.CharField('Modèle principal', max_length=30)
    image = models.ImageField(upload_to='category', max_length=300)
    description = models.TextField(null=True)
    nb_seats = models.IntegerField('Nombre de places', default=5)
    nb_luggage = models.IntegerField('Nombre de bagages', default=0)
    nb_doors = models.IntegerField('Nombre de portes', default=5)
    gear = models.CharField('Type de boite', max_length=2, choices=GEARS_CHOICES, default='MA')
    energy = models.CharField('Energie', max_length=2, choices=ENERGY_CHOICES, default='GD')
    climate_control = models.BooleanField('Climatisation', default=True)
    winter = models.BooleanField('Equipé hiver', default=False)
    pre_pay = models.DecimalField('Montant du pré-paiement', decimal_places=2, max_digits=10, default=0)
    equivalent = models.TextField('Modèles équivalents', null=True)
    is_active = models.BooleanField('Actif', default=True)

    class Meta:
        verbose_name = 'Catégories de véhicule'
        ordering = ['code']

    def __str__(self):
        return 'Catégorie {} - {} - {}'.format(self.code, self.label, self.sample)

class Agency(models.Model):
    name = models.CharField('Nom', max_length=100, unique=True)
    address = models.CharField('Adresse', max_length=100)
    zip_code = models.CharField('Code postal', max_length=5)
    city = models.CharField('Ville', max_length=50)
    phone = models.CharField('Téléphone', max_length=10)
    email = models.CharField('E-mail', max_length=50, unique=True)
    is_active = models.BooleanField('Actif', default=True)

    class Meta:
        verbose_name = 'Agences de location'
        ordering = ['name']

    def __str__(self):
        return '{} - {}'.format(self.name, self.city)

class Vehicle(models.Model):
    manufacturer = models.CharField('Constructeur', max_length=50)
    car_model = models.CharField('Modèle', max_length=50, null=True)
    registration_number = models.CharField('Immatriculation', max_length=9, unique=True, validators=[RegexValidator(regex=r'^[A-Z]{2}-\d{3}-[A-Z]{2}$', message='Immatriculation invalide ! Le format attendu est AA-000-AA.')])
    vehicle_identification_number = models.CharField('VIN', max_length=17, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    agency = models.ForeignKey(Agency, on_delete=models.PROTECT)
    is_active = models.BooleanField('Actif', default=True)

    class Meta:
        verbose_name = 'Véhicule'
        ordering = ['manufacturer', 'car_model', 'registration_number']

    def __str__(self):
        return '{} - {} - {}'.format(self.manufacturer, self.car_model, self.registration_number)

CLIENT_CHOICES = (
    ('PRI', 'Particulier'),
    ('PRO', 'Professionnel'),
)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    client_type = models.CharField('Type de client', max_length=3, choices=CLIENT_CHOICES, default='PRI')
    date_of_birth = models.DateField('Date de naissance', null=True)
    address = models.CharField('Adresse', max_length=100, null=True)
    zipcode = models.CharField('Code postal', max_length=5, null=True)
    city = models.CharField('Ville', max_length=50, null=True)
    phone = models.CharField('Téléphone', max_length=10, null=True)
    licence_scan = models.ImageField('Copie permis de conduire', upload_to='customer_licences', blank=True)
    licence_number = models.CharField('Numéro du permis de conduire', max_length=12, null=True)
    receiveAdds = models.BooleanField('Accepte de recevoir de la publicité ?', default=True)
    creditCardNumber = models.CharField('Numéro de carte de paiement', max_length=16, null=True)
    creditCardValidity = models.DateField('Fin de validité de la carte de paiement', null=True)

    def __str__(self):
        return f'Customer {self.user.username}'

class Booking(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    agency = models.ForeignKey(Agency, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    date_start = models.DateTimeField('Date de début de location')
    date_end = models.DateTimeField('Date de fin de location')
    confirm = models.BooleanField(default=False)

def vehicle_availability_list(category, agency_departure, date_departure, date_back):
    bookings_to_exclude_list = (
        Booking.objects.all()
            .filter(agency=agency_departure)
            #.filter(date_end__gte=date_departure, date_start__lte=date_departure)
            .filter(date_start__lte=date_back, date_end__gte=date_departure)
    )
    available_vehicles = (
        Vehicle.objects.all()
            .filter(is_active=True)
            .filter(agency=agency_departure)
            .filter(category=category)
            .exclude(id__in=(bookings_to_exclude_list.values('vehicle')))
    )
    return available_vehicles