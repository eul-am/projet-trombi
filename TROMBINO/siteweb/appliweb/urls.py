from django.urls import path
# On importe toutes les pages depuis forms.py
from . views import connexion, bienvenue, inscription

# espace de nom de l'application
nom_appli = 'appliweb'

urlpatterns = [

    path('', connexion, name='connexion'),
    path('bienvenue/', bienvenue, name='bienvenue'),
    path('inscription/', inscription, name='inscription'),
]
