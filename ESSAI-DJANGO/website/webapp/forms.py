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
            result = Utilisateur.objects.filter(password=password, email=email)

            if len(result) != 1:
                raise forms.ValidationError("Adresse de courriel ou mot de passe erroné.")
        return cleaned_data

    class Meta:
        model = Utilisateur
        exclude = ('nom', 'prenom', 'sexe',)


class Form_Inscription(forms.ModelForm):
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = Utilisateur
        fields = '__all__'