
from django import forms

class Authentification(forms.Form):
    numero_inscription = forms.CharField(max_length=10)
    nom = forms.CharField(max_length=30)
    prenom = forms.CharField(max_length=30)
    # pour une date si blank=True, il faut rajouter null=True
    date_naissance = forms.DateField(blank=True, null=True)
    email = forms.EmailField()
    telephone_fixe = forms.CharField(max_length=20)
    telephone_portable = forms.CharField(max_length=20)
    password = forms.CharField(min_length=6)
    # clé étrangère : relation n,n
    # 1 personne peut avoir 0 ou plusieurs amis et plusieurs amis peuvent avoir 1 même ami
    amis = forms.ManyToManyField('self')
    # clé étrangère : relation 1,n
    # 1 personne peut étudier dans 1 seule université et 1 université peut accueillir plusieurs personnes
    universite = forms.ForeignKey('Universite', on_delete=models.CASCADE)