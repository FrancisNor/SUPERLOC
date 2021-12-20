from django.urls import path

from . import views

app_name='visitor'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('legal_notice', views.legal_notice, name = 'legal_notice'),
    path('tourism/categories', views.tourism_categories, name = 'tourism_categories'),
    path('tourism/categories/<str:code>', views.tourism_category, name = 'tourism_category'),
    path('TODO', views.todo, name= 'todo'),
    path('login', views.todo, name= 'login'),
    path('inscription', views.todo, name= 'inscription'),
    ]