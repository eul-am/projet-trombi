"""monsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# (1) on importe depuis le fichier views.py (la vue) toutes les pages du site,
# (Les fonctions, les rôles, les noms de pages)
from . views import *

urlpatterns = [
    # (2) on définie les chemins d'urls des pages du site
    path('', index, name='index'),
    path('inscription/', inscription, name='inscription'),
    path('connexion/', connexion, name='connexion'),
    path('modification/', modification, name='modification'),
    path('profil/', profil, name='profil'),
    path('ajout/', ajout, name='ajout'),
    path('admin/', admin.site.urls),
]
