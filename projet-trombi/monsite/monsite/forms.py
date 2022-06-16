
from xml.dom.pulldom import START_DOCUMENT
from django import forms

from trombinoscoop.models import Etudiant

# Formulaire de connexion
class FormConnexion(forms.Form):
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    def clean(self):
        donnee_valide = super(FormConnexion, self).clean()
        email = donnee_valide.get('email')
        password = donnee_valide.get('password')

        if email and password:
            if password != 'sesame' or email != 'euloge@mail.fr':
                raise forms.ValidationError("Courriel ou mot de passe erroné")
        return donnee_valide

# Formulaire Étudiant
class FormProfilEtudiant(forms.ModelForm):
    class Meta:
        model = Etudiant
        # tuple avec un seul paramètre
        exclude = ('amis',)
