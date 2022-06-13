from  django.shortcuts import render


# (1) définir le nom de la page web
# le rôle de la page, sa fonction
def index(request):
    """page principale du site"""
    return render (request, 'monsite/index.html', )


def inscription(request):
    """sert à créer un compte"""
    return render (request, 'monsite/inscription.html')


def connexion(request):
    """sert à s'authentifier"""
    return render (request, 'monsite/connexion.html')


def modification(request):
    """sert à modifier des informations personnelles de l'internaute"""
    return render (request, 'monsite/modification.html')


def profil(request):
    """sert à afficher soit le profil de l'utilisateur connecté, soit celui de l'un de ses amis"""
    return render (request, 'monsite/profil.html')



def ajout(request):
    """sert à ajouter un ami à partir de son adresse e-mail"""
    return render (request, 'monsite/ajout.html')
