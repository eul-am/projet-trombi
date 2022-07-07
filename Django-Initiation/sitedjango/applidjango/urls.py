from django.urls import path
from .views import welcome, login, register

urlpatterns = [

    path('', welcome, name='bienvenue'),
    path('login', login, name='connexion'),
    path('bienvenue/', welcome, name='bienvenue'),
    path('inscription/', register, name='inscription'),
]
