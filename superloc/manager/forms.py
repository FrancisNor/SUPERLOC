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

'''
def date_check(date, timelimit, message):
    now = datetime.now().replace(tzinfo=date.tzinfo)
    delta = date - now
    delta = delta.total_seconds() / 3600
    if delta < timelimit:
        raise ValidationError(message)

def departure_date_check(value):
    date_check(value, 1, "La réservation doit être faite au moins une heure avant le départ.")
    
def back_date_check(value):
    date_check(value, 0, "Le date de retour ne peut pas antérieure à la date de départ.")
'''

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
                                         #validators = [departure_date_check]
                                         )
    date_back = forms.DateTimeField(label='Date de retour',
                                    input_formats = [DATE_FORMAT],
                                    widget = forms.DateTimeInput(
                                        attrs = {'type': 'datetime-local', },
                                        format = DATE_FORMAT, ),
                                    required = True,
                                    #validators = [back_date_check]
                                    )
'''
def clean(self):
        cleaned_data = super().clean()
        date_departure = cleaned_data.get('date_departure')
        date_back = cleaned_data.get('date_back')
        if date_departure is not None and date_back is not None:
            timelimit = date_back-date_departure
            timelimit = timelimit.total_seconds()/3600
        if timelimit<1:
            message = "Le retour doit être au moins une heure après le départ."
            self.add_error('date_back', ValidationError(message, code='invalid'))    
'''
"""
Utiliser la form de visitor (à surcharger ?) pour sélection du client ? 
class BookingEditForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('vehicle', 'agency', 'customer', 'date_start', 'scheduled_date_end', 'date_end')
"""
