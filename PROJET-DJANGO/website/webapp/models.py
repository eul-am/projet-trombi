from django.db import models


# (I) on créé la table
class User(models.Model):

    SEXE_CHOICE = [
        ('H', 'Homme'),
        ('F', 'Femme'),
    ]


    nom = models.CharField(max_length=30)
    sexe = models.CharField(max_length=30, choices=SEXE_CHOICE)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        """  """
        return self.nom


class Particulier(User):
    #
    pass

    def __str__(self):
        """  """
        return self.nom


class Entreprise(User):
    #
    pass

    def __str__(self):
        """  """
        return self.nom