from django.contrib.auth import views as auth_views
from django.core.exceptions import PermissionDenied
from django.urls import path

from . import views

app_name = 'manager'


def permission_denied_view(request):
    raise PermissionDenied


urlpatterns = [
    path('', views.home, name='home'),
    path('logged_out', views.logged_out, name='logged_out'),
    path('login', views.LoginManager.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(),
         {'next_page': 'logged_out'}, name='logout'),
    path('403', permission_denied_view, name='forbidden'),
    path('vehicles', views.vehicles_home, name='vehicles'),
    path('agencies', views.agencies_home, name='agencies'),
    path('customer', views.customers_home, name='customers'),
]