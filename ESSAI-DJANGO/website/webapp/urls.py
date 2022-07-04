from django.urls import path
from .views import login, inscription, bienvenue, deconnexion, profile, update_profile, \
    del_profile, add_user

urlpatterns = [

    path('', login, name='connexion'),
    path('connexion/', login, name='connexion'),
    path('inscription/', inscription, name='inscription'),
    path('bienvenue/', bienvenue, name='bienvenue'),

    path('deconnexion/', deconnexion, name='deconnexion'),
    path('profile/', profile, name='profile'),
    path('modification_profile/', update_profile, name='modification_profile'),
    path('suppression_profile/', del_profile, name='suppression_profile'),
    path('ajout_utilisateur/', add_user, name='ajout_utilisateur'),
]
