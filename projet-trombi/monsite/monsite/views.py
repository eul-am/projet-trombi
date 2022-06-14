from  django.shortcuts import render, redirect


# (1) définir la vue (le nom de la page web : son rôle de la page, sa fonction)
def index(request):
    """page principale du site"""
    # on retourne le templates (le fichier html)
    return render (request, 'monsite/index.html', )


def inscription(request):
    """sert à créer un compte"""
    return render (request, 'monsite/inscription.html')


def authentification(request):
    """sert à s'authentifier"""

    return render (request, 'monsite/authentification.html')


def modification(request):
    """sert à modifier des informations personnelles de l'internaute"""
    return render (request, 'monsite/modification.html')


def profil(request):
    """sert à afficher soit le profil de l'utilisateur connecté, soit celui de l'un de ses amis"""
    return render (request, 'monsite/profil.html')



def ajout(request):
    """sert à ajouter un ami à partir de son adresse e-mail"""
    return render (request, 'monsite/ajout.html')
