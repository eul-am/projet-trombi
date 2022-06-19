from django import forms

from .models import Personne, Etudiant, Employe

""" Création d'un formulaire de Connexion"""
class FormConnexion(forms.Form):
    """ Formulaire de connexion d'une Personne """
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    def clean(self):  # (1)
        """ """
        #
        donnees = super(FormConnexion, self).clean()  # (2)
        #
        email = donnees.get("email")  # (3)
        password = donnees.get("password")  # (3)

        # Si l'email et le mot de passe saisis par l'utilisateur correspondent à ceux stockés dans la base de données
        if email and password:  # (4)
            #
            resultat = Personne.objects.filter(password=password, email=email)
            # si l'un des identifiants est différent de celui qui est stocké dans la base de données
            if len(resultat) != 1:  # (5)
                # lever cette erreur d'exception
                raise forms.ValidationError("Adresse de courriel ou mot de passe erronné.")  # (6)

        return donnees  # (7)


""" Conversion de la table Étudiant en Formulaire """
class FormProfilEtudiant(forms.ModelForm):
    class Meta:
        model = Etudiant
        exclude = ('amis',)


""" Conversion de la table Employé en Formulaire """
class FormProfilEmploye(forms.ModelForm):
    class Meta:
        model = Employe
        exclude = ('amis',)