from django import forms
from .models import Utilisateur


class Connexion(forms.ModelForm):

    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    def clean(self):

        cleaned_data = super(Connexion, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            donnees = Utilisateur.objects.filter(password=password, email=email)
            # si l'un des deux identifiants n'est pas vrai (si l'un est mal écrit ou inexistant)
            if len(donnees) != 1:
                # il faut dire ceci
                raise forms.ValidationError("Adresse de courriel ou mot de passe erroné.")
            # et si les deux sont faux (s'il n'existent pas)
            elif len(donnees) <= 0:
                raise forms.ValidationError("Adresse de courriel inexistant.")

        return cleaned_data

        # NB : les formulaires de type (forms.Form) ne prennent pas de classe Meta

    class Meta:
        model = Utilisateur
        fields = ('email', 'password',)


class Inscription(forms.ModelForm):
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    def clean(self):
        # nettoyage des données du formulaire d'inscription
        cleaned_data = super(Inscription, self).clean()
        #
        email = cleaned_data.get("email")
        # si l'email a bien été saisi
        if email:
            # on compte le nombre d'email saisie par l'utilisateur
            email = Utilisateur.objects.filter(email=email).count()
            # s'il y en a plus de zéro, ça veut dire que l'email existe
            if email > 0:
                # et il faut le signaler
                raise forms.ValidationError("Compte existant.")
            # sinon, il faut retourner les données nettoyées
        return cleaned_data

    class Meta:
        model = Utilisateur
        fields = '__all__'
