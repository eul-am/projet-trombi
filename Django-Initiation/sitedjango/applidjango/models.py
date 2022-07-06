from django.db import models

class Personne(models.Model):

    CHOIX_SEXE = [
        ('HOMME', 'Homme'),
        ('FEMME', 'Femme'),
    ]

    nom = models.CharField('Nom', max_length=30)
    prenom = models.CharField('Prénom', max_length=30)
    sexe = models.CharField('Sexe', max_length=30, choices=CHOIX_SEXE)

    def __str__(self):
        return self.nom, self.prenom
