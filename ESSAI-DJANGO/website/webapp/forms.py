from django import forms
from .models import Employe, Utilisateur


        # ------------------------------------------------------------------------------------------


class Form_Connexion(forms.Form):
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

        # NB : les formulaires de type (forms.Form) ne prennent pas de classe Meta



        # FORMULAIRE D'INSCRIPTION ET DE PROFIL EMPLOYÉ -------------------------------------------------------------------------------------------------------------------------------------


class Form_Profile_Employe(forms.ModelForm):
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    def clean(self):
        # nettoyage des données du formulaire d'inscription
        cleaned_data = super(Form_Profile_Employe, self).clean()
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
        model = Employe
        exclude = ('amis',)


        # -------------------------------------------------------------------------------------------



class Form_Modification_Profile(forms.ModelForm):

    class Meta:
        # Table dont on converti en formulaire
        model = Utilisateur
        fields = '__all__'


        # -------------------------------------------------------------------------------------------


