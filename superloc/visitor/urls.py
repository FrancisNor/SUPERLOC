from django.urls import path
from . import views

app_name='visitor'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('legal_notice', views.legal_notice, name = 'legal_notice'),
    ]