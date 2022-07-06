from django.urls import path
from .views import welcome, login

urlpatterns = [

    path('bienvenue/', welcome, name='bienvenue'),
    path('', login, name='connexion'),
    path('connexion', login, name='connexion'),
]