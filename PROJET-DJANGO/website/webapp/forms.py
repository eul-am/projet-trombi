from django import forms

from .models import User


# Formulaire de Connexion
class Login_Form(forms.ModelForm):
    #
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    #
    class Meta:
        # la table (modèle) à convertir
        model = User
        # liste, tuple des champs à utiliser
        fields = ('email', 'password',)
        # OU liste des champs à exclure
        # exclude = ['name', 'title', 'birth_date']

    # Mise en conformité des données
    def clean(self):
        """ Traitement du formulaire """
        #
        cleaned_data = super(Login_Form, self).clean()
        #
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        # Si l'email et le mot de passe saisis par l'utilisateur correspondent à ceux stockés dans la base de données
        if email and password:
            #
            resultat = User.objects.filter(password=password, email=email)
            # si l'un des identifiants est différent de celui qui est stocké dans la base de données
            if len(resultat) != 1:
                # lever cette erreur d'exception
                raise forms.ValidationError("Adresse de courriel ou mot de passe erronné.")

        return cleaned_data


# Formulaire d'Inscription
class Register_Form(forms.ModelForm):
    # on masque le mot de passe
    last_name = forms.CharField(label="Nom")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

    #
    class Meta:
        # la table (modèle) à convertir
        model = User
        # liste, tuple des champs à utiliser
        fields = '__all__'
