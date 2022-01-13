from django.contrib import admin
from .models import Category, Agency
#from django.contrib.auth.models import User

admin.site.site_header = 'SUPERLOC - Administrateur'

@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'zip_code', 'city', 'is_active')
    search_fields = ['name', 'zip_code', 'city']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'sample', 'nb_seats', 'nb_doors', 'gear', 'energy', 'winter', 'is_active')
    list_filter = ('code', 'gear')

#from django.contrib.auth.models import Permission
#@admin.register(Permission)
#    list_display = ('id')
#    list_filter = ('id')

#@admin.register(User)
#class UserAdmin(admin.ModelAdmin):
#    list_filter = (
#        ('is_staff', admin.BooleanFieldListFilter),
#    )