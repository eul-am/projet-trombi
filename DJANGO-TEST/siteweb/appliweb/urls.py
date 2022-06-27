from django.urls import path

from .views import welcome, login, register, ajax_check_email_field, ajax_add_friend, show_profile, modify_profile, \
    add_friend

urlpatterns = [
    # URL 'vide', appelé sans aucun nom de page
    path('', login, name='login'),
    # URL qui nomme explicitement la page Login
    path('login/', login, name='login'),
    path('welcome/', welcome, name='welcome'),
    path('register/', register, name='register'),
    path('add_friend/',  add_friend, name='add_friend'),
    path('show_profile/',  show_profile, name='show_profile'),
    path('modify_profile/', modify_profile, name='modify_profile'),
    path('ajax/checkEmailField/', ajax_check_email_field, name='checkEmailField'),
    path('ajax/addFriend/', ajax_add_friend, name='addFriend'),
]
