from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from . import views

app_name='visitor'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('legal_notice', views.legal_notice, name = 'legal_notice'),
    path('tourism/categories', views.tourism_categories, name = 'tourism_categories'),
    path('tourism/categories/<str:code>', views.tourism_category, name = 'tourism_category'),
    path('TODO', views.todo, name= 'todo'),
    path('login', auth_views.LoginView.as_view(), name= 'login'),
    path('inscription', views.inscription, name= 'inscription'),
    path('inscription_done', views.inscription, name= 'inscription_done'),
    path('language_choice', views.language_choice, name= 'language_choice'),
    path('agencies', views.agencies, name= 'agencies'),
    ]