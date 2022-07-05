from django.db import models


class Utilisateur(models.Model):
    CHOIX_SEXE = [
        ('H', 'HOMME'),
        ('F', 'FEMME'),
    ]
    nom = models.CharField(verbose_name='Nom', max_length=30)
    prenom = models.CharField(verbose_name='Prénom', max_length=30)
    sexe = models.CharField(verbose_name='Sexe', max_length=30, choices=CHOIX_SEXE)
    email = models.EmailField(verbose_name='Courriel', )
    password = models.CharField(verbose_name='Mot de passe', max_length=30)
    #ami = models.ManyToManyField('self')
    type_profile = 'generic'

    def __str__(self):
        "Fonction permettant d'afficher le nom (intitulé) de l'objet en clair dans l'espace d'administration"
        return self.nom + " " + self.prenom


class Message(models.Model):
    auteur = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    contenu = models.TextField()
    date_publication = models.DateField()

    def __str__(self):
        if len(self.contenu) > 20:
            return self.contenu[:19] + "..."
        else:
            return self.contenu

class Employe(Utilisateur):
    CHOIX_SERVICE = [
        ('D', 'DIRECTION'),
        ('A', 'AUDIT'),
        ('I', 'INFORMATIQUE'),
        ('CPT', 'COMPTABILITÉ'),
        ('J', 'JURIDIQUE'),
        ('M', 'MARKETING'),
        ('CMC', 'COMMERCIAL'),
        ('COUR', 'COURRIER'),
        ('CM', 'COMMUNICATION'),
    ]
    service = models.CharField(max_length=30, choices=CHOIX_SERVICE)
    poste = models.CharField(max_length=30)
    #type_profile = 'employe'

    def __str__(self):
        return self.poste


class Stagiaire(Utilisateur):
    cursus = models.CharField(max_length=30)
    #type_profile = 'stagiaire'

    def __str__(self):
        return self.cursus
