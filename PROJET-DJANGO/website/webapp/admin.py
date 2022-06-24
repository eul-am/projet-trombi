from django.contrib import admin
#
from .models import Particulier, Entreprise

admin.site.register(Particulier)
admin.site.register(Entreprise)
