from django.urls import path
from .views import login, register, index

urlpatterns = [
    path('index/', index, name='index'),
    path('', login, name='login'),
    path('register/', register, name='register'),
]