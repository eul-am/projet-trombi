from django.urls import path
# On importe toutes les pages depuis forms.py
from . views import connexion, inscription, accueil

# espace de nom de l'application
nom_appli = 'webapp'

urlpatterns = [

    path('', connexion, name='connexion'),
    path('inscription/', inscription, name='inscription'),
    path('accueil/', accueil, name='accueil'),

]
