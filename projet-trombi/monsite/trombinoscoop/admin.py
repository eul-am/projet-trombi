from django.contrib import admin
# on importe toutes les tables (les classes)
from trombinoscoop.models import *

# Register your models here.

# le modele Personne a volontairement été omis
admin.site.register(Message)
admin.site.register(Faculte)
admin.site.register(Campus)
admin.site.register(Emploi)
admin.site.register(Cursus)
admin.site.register(Employe)
admin.site.register(Etudiant)