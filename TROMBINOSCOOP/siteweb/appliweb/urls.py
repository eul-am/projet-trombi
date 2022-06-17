from django.urls import path
# depuis la views.py, importer les noms des pages web (les fonctions, les rôles)
from . views import connexion, bienvenue

urlpatterns = [
    path('', connexion, name='connexion'),
    path('connexion/', connexion, name='connexion'),
    path('bienvenue/', bienvenue, name='bienvenue'),
]