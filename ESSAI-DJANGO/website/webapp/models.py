from django.db import models

 # ---------------------------------------------------------------------------------------------------

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
    # clé étrangères : relation n,n - plusieurs à plusieurs -
    amis = models.ManyToManyField('self')

    def __str__(self):
        "Fonction permettant d'afficher le nom (intitulé) de l'objet en clair dans l'espace d'administration"
        return self.nom + " " + self.prenom

        # ------------------------------------------------------------------------------------------


class Message(models.Model):
    # Clé étrangère : relation (liaison) 1,n (l'auteur d'un message est d'abord un utilisateur)
    # l'héritage ici peut se faire avec les côtes
    auteur = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    contenu = models.TextField()
    date_de_publication = models.DateField()

    def __str__(self):
        if len(self.contenu) > 20:
            return self.contenu[:19] + "..."
        else:
            return self.contenu


         # ------------------------------------------------------------------------------------------


class Employe(Utilisateur): # NB: l'héritage en classe se fait sans les côtes
    service = models.CharField(max_length=30)
    # Clé étrangère : relation 1,n
    poste = models.ForeignKey('Poste', default=None, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.service


         # ------------------------------------------------------------------------------------------

class Poste(models.Model):
    titre = models.CharField(max_length=30)

    def __str__(self):
        return self.titre
    
    


