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

'''
.exclude(id__in=Subquery(liste_contrats_conclus_bloquants_sur_la_periode_demandee.values('vehicule'))) #à condition que le véhicule ne figure pas dans un contrat déjà conclu aux dates souhaitées​
    )​
    return vehicules_disponibles​
def liste_vehicules_disponibles(categorie, agence, reservation_date_depart, reservation_date_retour):​
    liste_contrats_conclus_bloquants_sur_la_periode_demandee = (​
        Contrat.objects.all() # On part de la liste de tous les contrats puis on va la filtrer​
        .filter(agence=agence) # on retient ceux signés dans l'agence concernée par la recherche​
        .filter(date_fin__gte=reservation_date_depart) # si la date de retour d'un contrat existant est postérieur à notre date de départ​
        .filter(date_debut__lte=reservation_date_retour) # et si la date de début d'un contrat existant est antérieur à notre date de retour​
    )​
​
    vehicules_disponibles = (​
        Vehicule.objects.all() # On part de la liste de tous les véhicules puis on va la filtrer​
        #.filter(active=True) # à condition qu'ils soient actifs​
        .filter(categorie=categorie) # à condition que la catégorie corresponde à celle demandée dans le formulaire​
        .filter(agence=agence)  #à condition que l'agence corresponde à celle demandée dans le formulaire​
        .exclude(id__in=Subquery(liste_contrats_conclus_bloquants_sur_la_periode_demandee.values('vehicule'))) #à condition que le véhicule ne figure pas dans un contrat déjà conclu aux dates souhaitées​
    )​
    return vehicules_disponibles​
'''

'''
# Fonction de sélection de véhicule disponibles
# (appelée à partir du moment où le formulaire agence / dates de réservations) est valide

# En fonction des données soumies et de leue validité, affiche un template ou un autre :
#       confirm-reservation-infos-vehicule.html
#  ou   enregistrement-contrat.html
def selection_vehicule(request, reservation, reservation_form):
    #Récupération des informations soumies par le formualire
    categorie = reservation.get('categorie')​
    agence = reservation.get('agence_depart')​
    date_depart = reservation.get('date_depart')​
    date_retour = reservation.get('date_retour')​
    vehicule_id = request.POST.get('vehicule_id')​
    reservation_step = request.POST.get('reservation-step')​
​
    if (vehicule_id):​
        client_form = ClientForm()​
        if (request.user.client):​
            client_form = ClientForm(instance=request.user.client)​
        if (reservation_step and reservation_step == 'infos-client'):​
            client_form = ClientForm(request.POST, instance=request.user.client or None)​
            if (client_form.is_valid()):​
                client = client_form.save(commit=False)​
                if (not client.user):​
                    client.user = request.user​
                client.save()​
​
                vehicule = Vehicule.objects.get(id=vehicule_id)​
                already_contracted = (​
                    Contrat.objects.all()​
                        .filter(agence=agence)​
                        .filter(vehicule=vehicule)​
                        .filter(date_fin__gte=date_depart)​
                        .filter(date_debut__lte=date_retour)​
                )​
​
                error = ''​
                if already_contracted.count() > 0:​
                    ctr_error = 'Impossible de réserver à partir des choix transmis. Le véhicule demandé n\'est plus disponible.'​
                    context = {'ctr_error': ctr_error}​
                    return render(request, 'enregistrement-contrat.html', context)​
                elif not error:​
                    # création du contrat​
                    ctr_error = ''​
                    contrat = Contrat(vehicule=vehicule, client=client, agence=agence, date_debut=date_depart, date_fin=date_retour)​
                    contrat.save()​
​
                    # context​
                    context = {​
                        'ctr_error': ctr_error,​
                        'agence': agence,​
                        'vehicule': vehicule,​
                        'date_debut': date_depart,​
                        'date_fin': date_retour,​
                        'client': client,​
                        'contrat': contrat,​
                    }​
                    return render(request, 'enregistrement-contrat.html', context)​
                elif(error):​
                    ctr_error = error​
                    context = {'ctr_error': ctr_error}​
                    return render(request, 'enregistrement-contrat.html', context)​
​
        context = {'vehicule_id': vehicule_id, 'reservation': reservation, 'client_form': client_form}​
        return render(request, 'confirm-reservation-infos-client.html', context)​
​
    #Récupération de la liste des véhicules disponibles​
    vehicules = liste_vehicules_disponibles(categorie, agence, date_depart, date_retour)​
​
    context = {'vehicules': vehicules, 'reservation': reservation, 'reservation_form': reservation_form}​
    return render(request, 'confirm-reservation-infos-vehicule.html', context)​
'''