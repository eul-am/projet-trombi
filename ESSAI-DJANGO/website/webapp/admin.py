from django.contrib import admin

from .models import Utilisateur, Message

admin.site.register(Utilisateur)
admin.site.register(Message)
