from django import forms
from .models import Utilisateur


class Form_Connexion(forms.ModelForm):
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(Form_Connexion, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            donnees = Utilisateur.objects.filter(password=password, email=email)
            # si
            if len(donnees) != 1:
                # s'il existe,
                raise forms.ValidationError("Adresse de courriel ou mot de passe erroné.")
        return cleaned_data

    class Meta:
        model = Utilisateur
        exclude = ('nom', 'prenom', 'sexe',)


class Form_Inscription(forms.ModelForm):
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    def clean(self):
        # nettoyage des données du formulaire d'inscription
        cleaned_data = super(Form_Inscription, self).clean()
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