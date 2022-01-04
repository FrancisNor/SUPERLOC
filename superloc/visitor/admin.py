from django.contrib import admin

from .models import Category, Agency

@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'zip_code', 'city')
    search_fields = ['name', 'zip_code', 'city']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'sample', 'nb_seats', 'nb_doors', 'gear', 'energy', 'winter')
    list_filter = ('code', 'gear')