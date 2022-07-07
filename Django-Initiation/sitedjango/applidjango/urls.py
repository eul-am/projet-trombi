from django.urls import path
from .views import welcome, login, register, add_friend, show_profile, modify_profile, logout

urlpatterns = [

    path('', welcome, name='bienvenue'),
    path('login/', login, name='connexion'),
    path('bienvenue/', welcome, name='bienvenue'),
    path('inscription/', register, name='inscription'),
    path('ajout_amis/', add_friend, name='ajout_amis'),
    path('voir_profil/', show_profile, name='voir_profil'),
    path('modification_profil/', modify_profile, name='modification_profil'),
    path('deconnexion/', logout, name='deconnexion'),

]
