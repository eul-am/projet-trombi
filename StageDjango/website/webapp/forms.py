from django import forms

from .models import Utilisateur


# conversion de la table UTILISATEUR en formulaire de connexion
class FormConnexion(forms.ModelForm):
    class Meta:
        # la table (modèle) à convertir
        model = Utilisateur
        # on liste, tuple des champs à exclure
        exclude = ('nom', 'sexe',)
        # OU liste des champs à utiliser
        # fields = ['name', 'title', 'birth_date']



# conversion de la table UTILISATEUR en formulaire d'inscription
class FormInscription(forms.ModelForm):
    class Meta:
        # la table qu'on convertit en formulaire
        model = Utilisateur
        # tous les champs de la table doivent être utilisés
        fields = '__all__'
