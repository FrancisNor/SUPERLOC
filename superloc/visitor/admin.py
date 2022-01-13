from django.contrib import admin
from .models import Category, Agency, Booking

admin.site.site_header = 'SUPERLOC - Administrateur'

@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'zip_code', 'city', 'is_active')
    search_fields = ['name', 'zip_code', 'city']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'sample', 'nb_seats', 'nb_doors', 'gear', 'energy', 'winter', 'is_active')
    list_filter = ('code', 'gear')

@admin.register(Booking)
class BoookingAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'agency', 'customer', 'date_start', 'date_end')
    list_filter = ('agency',)
