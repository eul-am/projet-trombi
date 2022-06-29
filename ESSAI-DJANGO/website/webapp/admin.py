from django.contrib import admin

from .models import Utilisateur, Message, Poste

admin.site.register(Utilisateur)
admin.site.register(Message)
admin.site.register(Poste)
