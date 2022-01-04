from django.contrib import admin
from .models import Category, Agency, Vehicle, Customer

@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'zip_code', 'city', 'is_active')
    search_fields = ['name', 'zip_code', 'city']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'sample', 'nb_seats', 'nb_doors', 'gear', 'energy', 'winter', 'is_active')
    list_filter = ('code', 'gear')

'''
TODO : supprimer vues administration Véhicule et client
'''

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'car_model', 'registration_number', 'is_active')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('address', 'city')

'''
TODO : supprimer vues administration Véhicule et client
'''