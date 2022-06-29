from django.urls import path
from .views import connexion, inscription, bienvenue, deconnexion, affichage_profile, modification_profile, \
    suppression_profile

urlpatterns = [
    # URL 'vide', appelé sans aucun nom de page
    path('', connexion, name='connexion'),
    #
    path('connexion', connexion, name='connexion'),
    path('inscription/', inscription, name='inscription'),
    path('bienvenue/', bienvenue, name='bienvenue'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    path('affichage_profile/', affichage_profile, name='affichage_profile'),
    path('modification_profile/', modification_profile, name='modification_profile'),
    path('suppression_profile/', suppression_profile, name='suppression_profile'),
]
