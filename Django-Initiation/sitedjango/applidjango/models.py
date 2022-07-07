from django.db import models


class Personne(models.Model):
    """ Table Personne """
    CHOIX_SEXE = [
        ('HOMME', 'Homme'),
        ('FEMME', 'Femme'),
    ]

    nom = models.CharField('Nom', max_length=30)
    prenom = models.CharField('Prénom', max_length=30)
    sexe = models.CharField('Sexe', max_length=30, choices=CHOIX_SEXE)
    email = models.EmailField('Courriel',)
    password = models.CharField('Mot de passe', max_length=30)
    #
    ami = models.ManyToManyField('self')
    type_personne = 'generique'

    def __str__(self):
        return self.prenom + ' ' + self.nom

class Message(models.Model):
    """ Table Message """
    auteur = models.ForeignKey('Personne', on_delete=models.CASCADE)
    contenu = models.TextField()
    date_de_publication = models.DateField()

    def __str__(self):
        if len(self.contenu) > 20:
            return self.contenu[:19] + "..."
        else:
            return self.contenu

# python manage.py migrate --run-syncdb
