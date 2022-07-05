from django.contrib import admin

from .models import Utilisateur, Message, Employe, Stagiaire

admin.site.register(Utilisateur)
admin.site.register(Message)
admin.site.register(Employe)
admin.site.register(Stagiaire)

