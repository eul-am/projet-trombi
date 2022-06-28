from django.db import models

class Utilisateur(models.Model):

    CHOIX_SEXE = [
        ('H', 'HOMME'),
        ('F', 'FEMME'),
    ]
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    sexe = models.CharField(max_length=30, choices=CHOIX_SEXE)
    email = models.EmailField()
    # Dans un cas reel, nous ne devrions pas stocker le mot de passe en clair.
    password = models.CharField(max_length=32)


    def __str__(self):
        return self.nom + " " + self.prenom

