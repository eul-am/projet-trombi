from django.contrib import admin

from .models import Personne, Message

admin.site.register(Personne)
admin.site.register(Message)
