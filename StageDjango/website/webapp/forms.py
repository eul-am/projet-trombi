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
            resultat = Utilisateur.objects.filter(password=password, email=email)
            # si l'un des identifiants est différent de celui qui est stocké dans la base de données
            if len(resultat) != 1:  # (5)
                # lever cette erreur d'exception
                raise forms.ValidationError("Adresse de courriel ou mot de passe erronné.")  # (6)

        return donnees  # (7)


# conversion de la table UTILISATEUR en formulaire d'inscription
class FormInscription(forms.ModelForm):
    class Meta:
        # la table qu'on convertit en formulaire
        model = Utilisateur
        # tous les champs de la table doivent être utilisés
        fields = '__all__'
