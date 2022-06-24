from django import forms

from .models import User


class User_Profile_Form(forms.ModelForm):
    #
    class Meta:
        model = User
        fields = '__all__'



# Formulaire de Connexion
class Login_Form(forms.ModelForm):
    #
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    # Mise en conformité des données : (Nettoyage des données)
    def clean(self):
        """ Fonction permettant le nettoyage des données """

        cleaned_data = super(Login_Form, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        # (1)  si l'utilisateur a renseigné ses identifiants
        # (2)  il faut les retourner
        # (3)  mais ils doivent être identiques à ceux stockés dans la base de données
        # (4)  si l'une de ces données est différente
        # (5)  lever une exception

        # (1)
        if email and password:
            # (3)
            donnees = User.objects.filter(email=email, password=password)
            # (4)
            if len(donnees) != 1:
                # (5)
                raise forms.ValidationError("Adresse de courriel ou mot de passe erronné.")
        # (2)
        return cleaned_data

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
    # on masque le mot de passe
    nom = forms.CharField(label="Nom")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

    #
    class Meta:
        # la table (modèle) à convertir
        model = User
        # liste, tuple des champs à utiliser
        fields = '__all__'


class Part_Profile_Form(User_Profile_Form):
    #
    class Meta:
        model: User_Profile_Form
        fields = '__all__'


class Ent_Profile_Form(User_Profile_Form):

    class Meta:
        model: User_Profile_Form
        exclude = ('sexe',)
