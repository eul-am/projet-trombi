from django.db import models

"""
    une table 'Faculté' dans laquelle vont être stockés le nom et la couleur de l'université 
"""


class Faculte(models.Model):
    nom = models.CharField(max_length=30)
    couleur = models.CharField(max_length=6)

    def __str__(self):
        """ Cette fonction permet d'afficher le nom de la faculté en toutes lettres dans le panneau d'administration """
        return self.nom


"""
    une table 'Campus' dans laquelle vont être stockés le nom et l'adresse du Campus 
"""


class Campus(models.Model):
    nom = models.CharField(max_length=30)
    adresse = models.CharField(max_length=60)

    def __str__(self):
        """ Cette fonction permet d'afficher le nom du campus en toutes lettres dans le panneau d'administration """
        return self.nom


"""
    une table 'Job' dans laquelle va être stocké l'intitulé du poste occupé par une personne
"""


class Job(models.Model):
    """ """
    poste = models.CharField(max_length=30)

    def __str__(self):
        """ Cette fonction permet d'afficher le titre du Job en toutes lettres dans le panneau d'administration """
        return self.poste


"""
    une table 'Cursus' dans laquelle on va stocker l'intitulé de la formation d'une personne
"""


class Formation(models.Model):
    titre = models.CharField(max_length=30)

    def __str__(self):
        """ Cette fonction permet d'afficher le titre du cursus en toutes lettres dans le panneau d'administration """
        return self.titre


class Personne(models.Model):
    """ où l'on stocke les nom, prénom, date de naissance, e-mail, téléphone, mot de passe des personnes"""

    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField()
    # Dans un cas reel, nous ne devrions pas stocker le mot de passe en clair.
    password = models.CharField(max_length=32)
    # 'friends' est une clé étrangère qui lie les personnes entre elles | relation n,n
    # 1 personne peut avoir plusieurs amis et plusieurs amis peuvent avoir 1 ami en commun
    amis = models.ManyToManyField('self')
    # 'faculté' est une clé étrangère qui lie les tables 'Faculté' et 'Personne' | relation 1,n
    #
    #
    faculte = models.ForeignKey(Faculte, default=None, null=True, on_delete=models.CASCADE)

    def __str__(self):
        """ Cette fonction permet d'afficher le nom et le prénom de la personne en toutes lettres dans le panneau
        d'administration """
        return self.nom, self.prenom


"""
    une table 'Employé' dans laquelle on va stocker la fonction le d'un employé, son emploi et son campus
"""
class Employe(Personne):

    job = models.ForeignKey(Job, on_delete=models.CASCADE)

"""
    un (une table) 'Étudiant' qui hérite des caractéristiques de la (table) 'Personne'
    et qui est lui même caractérisé par son année d'étude et son cursus
"""


class Etudiant(Personne):
    #
    #
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)


class Message(models.Model):
    """ où seront stockés le contenu de ses messages et la date de publication des messages des personnes."""
    # 'auteur' est une clé étrangère qui permet d'identifier la personne qui a posté un message | relation 1,n
    # 1 personne peut envoyer 0 ou plusieurs messages et en recevoir 0 ou plusieurs
    #
    auteur = models.ForeignKey(Personne, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_publication = models.DateField()

    def __str__(self):
        """Cette fonction permet d'afficher le contenu du message, jusqu'à 20 caractères et 3 points de suspensions,
        en toutes lettres dans le panneau d'administration """
        # si le message dépasse 20 caractères,
        if len(self.contenu) > 20:
            # afficher jusqu'à 19 caractères et ...
            return self.contenu[:19] + "..."
        # sinon, afficher
        return self.contenu
