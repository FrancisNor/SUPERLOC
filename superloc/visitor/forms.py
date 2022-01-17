from django import forms
from django.contrib.auth.models import User
from datetime import datetime

from .models import Customer, Agency, Category


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Répéter le mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'last_name', 'first_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Les mots de passe ne correspondent pas')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CustomerEditForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('licence_scan', 'licence_number', 'address', 'zipcode', 'city', 'phone', 'date_of_birth','creditCardNumber','creditCardValidity',)

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
class BookingForm(forms.Form):
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
    date_back = forms.DateTimeField(label='Date de départ',
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