from django.forms import ModelForm
from django import forms

from visitor.models import Category, Vehicle, Agency, Booking

def get_agencies():
    agencies = Agency.objects.filter(is_active=True)
    return tuple(list(agencies.values_list('id', 'name')))

class GetAgencyForm(ModelForm) :
    class Meta:
        model = Agency
        fields = ['name']
        labels = {'name': ('Agence')}
        widgets = {'name': forms.Select(choices=get_agencies())}

def get_categories():
    categories = Category.objects.filter(is_active=True)
    return tuple(list(categories.values_list('id', 'code')))

class VehicleAddForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('category', 'manufacturer', 'car_model', 'registration_number', 'vehicle_identification_number')
        labels = {'category': ('Catégorie'), 'vehicle_identification_number': ("Numéro d'identification du véhicule (VIN)")}
        widgets = {'category': forms.Select(choices=get_categories())}

"""
Utiliser la form de visitor (à surcharger ?) pour sélection du client ? 
class BookingEditForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('vehicle', 'agency', 'customer', 'date_start', 'scheduled_date_end', 'date_end')
"""