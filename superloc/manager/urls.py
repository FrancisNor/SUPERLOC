from django.contrib.auth import views as auth_views
from django.core.exceptions import PermissionDenied
from django.urls import path

from . import views

app_name = 'manager'

def permission_denied_view(request):
    raise PermissionDenied

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicles_availability_agency_choice', views.vehicles_availability_agency_choice, name='vehicles_availability_agency_choice'),
    path('vehicles_availability/<str:id>', views.vehicles_availability, name='vehicles_availability'),
    path('vehicles_management_agency_choice', views.vehicles_management_agency_choice, name='vehicles_management_agency_choice'),
    path('vehicles_management/<str:id>', views.vehicles_management, name='vehicles_management'),
    path('vehicles_management_vehicle_add', views.vehicles_management_vehicle_add, name='vehicles_management_vehicle_add'),
]
"""
    path('logged_out', views.logged_out, name='logged_out'),
    path('login', views.LoginManager.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(),
         {'next_page': 'logged_out'}, name='logout'),
    path('403', permission_denied_view, name='forbidden'),
"""