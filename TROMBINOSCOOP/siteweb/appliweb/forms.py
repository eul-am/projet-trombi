
from xml.dom.pulldom import START_DOCUMENT
from django import forms

from appliweb.models import *

# Formulaire de connexion (qui ne dérive pas d'une table)
class FormConnexion(forms.Form):
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    # méthode
    def clean(self):
        donnee_valide = super(FormConnexion, self).clean()
        email = donnee_valide.get('email')
        password = donnee_valide.get('password')
        # conditions
        if email and password:
            if password != 'sesame' or email != 'euloge@mail.fr':
                raise forms.ValidationError("Courriel ou mot de passe erroné")
        return donnee_valide

""""
# Formulaire Étudiant (convertion de la table Étudiant en formulaire)
class FormProfilEtudiant(forms.ModelForm):
    class Meta:
        model = Etudiant
        # tuple avec un seul paramètre
        exclude = ('amis',)

"""