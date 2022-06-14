
from django.db import models

# définition des tables de la base de données


# table utilisateur (Personne)
class Personne(models.Model):
    numero_inscription = models.CharField(max_length = 10)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_naissance = models.DateField()
    email = models.EmailField()
    telephone_fixe = models.CharField(max_length=20)
    telephone_portable = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    # clé étrangère : relation n,n
    # 1 personne peut avoir 0 ou plusieurs amis et plusieurs amis peuvent avoir 1 même ami
    amis = models.ManyToManyField('self')
    # clé étrangère : relation 1,n
    # 1 personne peut étudier dans 1 seule université et 1 université peut accueillir plusieurs personnes
    universite = models.ForeignKey('Universite', on_delete=models.CASCADE)


# table message :
class Message(models.Model):
    """cette table contient les messages d'une personne"""
    # clé étrangère : relation 1,n
    # 1 personne peut envoyer 0 ou plusieurs messages et vice versa
    auteur = models.ForeignKey('Personne', on_delete=models.CASCADE)
    contenu = models.TextField()
    date_publication = models.DateField()

class Universite(models.Model):
    nom = models.CharField(max_length=30)
    couleur = models.CharField(max_length=20)


class Campus(models.Model):
    nom = models.CharField(max_length=30)
    adresse = models.CharField(max_length=60)


class Emploi(models.Model):
    poste = models.CharField(max_length=30)


class Formation(models.Model):
    titre = models.CharField(max_length=30)

# --------------- L'HÉRITAGE --------------------

# l'employé hérite des caractéristique d'une personne
class Employe(Personne):
    bureau = models.CharField(max_length=30)
    # clé étrangère : 1 employé peut travailler dans 1 ou plusieurs campus
    campus = models.ForeignKey('Campus', on_delete=models.CASCADE)
    # clé étrangère : 1 employé peut avoir 1 ou plusieurs emplois
    emploi = models.ForeignKey('Emploi', on_delete=models.CASCADE)

# l'étudiant hérite des caractèristiques d'une personne
class Etudiant(Personne):
    # clé étrangère : 1 étudiant peut avoir 1 ou plusieurs formations
    formation = models.ForeignKey('Formation', on_delete=models.CASCADE)
    annee = models.IntegerField()

