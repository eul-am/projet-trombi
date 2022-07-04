from django.urls import path
from .views import login, welcome, register, logout

urlpatterns = [
    
    path('', login, name='connexion'),
    path('connexion/', login, name='connexion'),
    path('bienvenue/', welcome, name='bienvenue'),
    path('inscription/', register, name='inscription'),
    path('deconnexion/', logout, name='deconnexion'),
  
]
