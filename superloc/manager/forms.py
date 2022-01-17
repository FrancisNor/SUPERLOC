from django.forms import ModelForm
from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError

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

class AvailabilityForm(forms.Form):
    DATE_FORMAT = '%Y-%m-%dT%H:%M'
    agency = forms.ModelChoiceField(label='Agence', queryset=Agency.objects.filter(is_active=True), required=True)
    category = forms.ModelChoiceField(label='Catégorie', queryset=Category.objects.filter(is_active=True), required=True)
    date_departure = forms.DateTimeField(label='Date de départ',    
                                         input_formats = [DATE_FORMAT],
                                         widget = forms.DateTimeInput(
                                             attrs = {'type': 'datetime-local', },
                                             format = DATE_FORMAT, ),
                                         required = True,
                                         )
    date_back = forms.DateTimeField(label='Date de retour',
                                    input_formats = [DATE_FORMAT],
                                    widget = forms.DateTimeInput(
                                        attrs = {'type': 'datetime-local', },
                                        format = DATE_FORMAT, ),
                                    required = True,
                                    )
