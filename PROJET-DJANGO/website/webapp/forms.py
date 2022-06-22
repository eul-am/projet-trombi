from django import forms

from .models import User

# Formulaire de Connexion
class Login_Form(forms.ModelForm):
    #
    class Meta:
        # la table (modèle) à convertir
        model = User
        # liste, tuple des champs à utiliser
        fields = ('email', 'password',)
        # OU liste des champs à exclure
        # exclude = ['name', 'title', 'birth_date']

# Formulaire d'Inscription
class Register_Form(forms.ModelForm):
    #
    class Meta:
        # la table (modèle) à convertir
        model = User
        # liste, tuple des champs à utiliser
        fields = '__all__'
        # OU liste des champs à exclure
