from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name='visitor'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('legal_notice', views.legal_notice, name = 'legal_notice'),
    path('tourism/categories', views.tourism_categories, name = 'tourism_categories'),
    path('tourism/categories/<str:code>', views.tourism_category, name = 'tourism_category'),
    path('TODO', views.todo, name= 'todo'),
    path('login/', auth_views.LoginView.as_view(), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': 'home'}, name='logout'),
    path('inscription', views.inscription, name= 'inscription'),
    path('customer/edit', views.edit_customer, name='edit_customer'),
    path('language_choice', views.language_choice, name= 'language_choice'),
    path('agencies', views.agencies, name= 'agencies'),
    ]