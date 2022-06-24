from django.urls import path
from .views import login, register, bienvenue, profile, modification

urlpatterns = [
    path('modification/', modification, name='modification'),
    path('profile/', profile, name='profile'),
    path('bienvenue/', bienvenue, name='bienvenue'),
    path('', login, name='connexion'),
    path('inscription/', register, name='inscription'),
]