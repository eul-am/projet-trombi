from django.db import models

class Utilisateur(models.Model):

    CHOIX_SEXE = [
        ('H', 'HOMME'),
        ('F', 'FEMME'),
    ]
    nom = models.CharField(verbose_name='Nom', max_length=30)
    prenom = models.CharField(verbose_name='Prénom', max_length=30)
    sexe = models.CharField(verbose_name='Sexe', max_length=30, choices=CHOIX_SEXE)
    email = models.EmailField(verbose_name='Courriel',)
    password = models.CharField(verbose_name='Mot de passe', max_length=30)
    type_profile = 'generic'
    
    def __str__(self):
        "Fonction permettant d'afficher le nom (intitulé) de l'objet en clair dans l'espace d'administration"
        return self.nom + " " + self.prenom

class Particulier(Utilisateur):
    type_profile = 'particulier'

class Entreprise(Utilisateur):
    raison_sociale = models.CharField(verbose_name='Raison sociale', max_length=30)
    type_profile = 'entreprise'

