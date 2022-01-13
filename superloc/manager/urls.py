from django.contrib.auth import views as auth_views
from django.core.exceptions import PermissionDenied
from django.urls import path

from . import views

app_name = 'manager'

def permission_denied_view(request):
    raise PermissionDenied

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.LoginManager.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('403', permission_denied_view, name='forbidden'),    
    path('vehicles_availability_form', views.vehicles_availability_form, name='vehicles_availability_form'),
    path('vehicles_availability/<str:id>', views.vehicles_availability, name='vehicles_availability'),
    path('booking', views.booking, name='booking'),
    path('vehicles_management_agency_choice', views.vehicles_management_agency_choice, name='vehicles_management_agency_choice'),
    path('vehicles_management/<str:id>', views.vehicles_management, name='vehicles_management'),
    path('vehicles_management/vehicle_add/<str:id>', views.vehicle_add, name='vehicle_add'),
    path('vehicles_management/vehicle_delete/<str:id>', views.vehicle_delete, name='vehicle_delete'),
]