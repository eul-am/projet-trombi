from django import forms
from .models import Personne

class Connexion(forms.Form):
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(Connexion, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            donnees = Personne.objects.filter(password=password, email=email)
            # si l'un des deux identifiants n'est pas vrai (si l'un est mal écrit ou inexistant)
            if len(donnees) != 1:
                # il faut dire ceci
                raise forms.ValidationError("Adresse de courriel ou mot de passe erroné.")
            # et si les deux sont faux (s'il n'existent pas)
            elif len(donnees) == 0:
                # il faut dire au client
                raise forms.ValidationError('Compte inexistant')

        return cleaned_data

        # NB : les formulaires de type (forms.Form) ne prennent pas de classe Meta