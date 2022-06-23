from django import forms

from .models import User


# Formulaire de Connexion
class Login_Form(forms.ModelForm):
    #
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    def clean(self):  # (1)
        """ """
        cleaned_data = super(Login_Form, self).clean()  # (2)
        email = cleaned_data.get("email")  # (3)
        password = cleaned_data.get("password")  # (3)

        # on vérifie que les deux champs sont valides

        if email and password:  # (4)
            #
            resultat = User.objects.filter(password=password, email=email)
            # si l'un des identifiants est différent de celui qui est stocké dans la base de données
            if len(resultat) != 1:  # (5)
                # lever cette erreur d'exception
                raise forms.ValidationError("Adresse de courriel ou mot de passe erronné.")  # (6)
        return cleaned_data  # (7)

    #
    class Meta:
        # la table (modèle) à convertir
        model = User
        # liste, tuple des champs à utiliser
        fields = ('email', 'password',)
        # OU liste des champs à exclure
        # exclude = ['name', 'title', 'birth_date']

    # Validation du courriel et du mote de passe en utilisant la base de données


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
