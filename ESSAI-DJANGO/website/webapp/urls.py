from django.urls import path
from .views import connexion, inscription, bienvenue, deconnexion

urlpatterns = [
    # URL 'vide', appelé sans aucun nom de page
    path('', connexion, name='connexion'),
    path('inscription/', inscription, name='inscription'),
    path('bienvenue/', bienvenue, name='bienvenue'),
    path('deconnexion/', deconnexion, name='deconnexion'),
]
