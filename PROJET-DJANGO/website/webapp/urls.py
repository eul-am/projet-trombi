from django.urls import path
from .views import login, register, bienvenue

urlpatterns = [
    path('bienvenue/', bienvenue, name='bienvenue'),
    path('', login, name='connexion'),
    path('inscription/', register, name='inscription'),
]