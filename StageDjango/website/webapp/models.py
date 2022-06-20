from django.db import models


# table UTILISATEUR
class Utilisateur(models.Model):
    """ où l'on stocke les nom, prénom, date de naissance, e-mail, téléphone, mot de passe des personnes"""

    HOMME = 'Homme'
    FEMME = 'Femme'
    CHOIX_SEXE = [(HOMME, 'Homme'), (FEMME, 'Femme'), ]

    nom = models.CharField(max_length=30)
    sexe = models.CharField(max_length=30, choices=CHOIX_SEXE)
    email = models.EmailField()
    password = models.CharField(max_length=32)

    def __str__(self):
        """ Cette fonction permet d'afficher le nom et le prénom de la personne en toutes lettres dans le panneau
        d'administration """
        return self.nom

