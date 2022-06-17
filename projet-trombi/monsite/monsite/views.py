# (1) on importe les modules render et redirect
from ast import For
from  django.shortcuts import render, redirect
# on importe le (module de) formulaire créé : la classe, le type d’objet 'FormAuthentification'
from monsite.forms import *

# définir la vue (le nom de la page web : son rôle de la page, sa fonction)
def index(request):
    """page principale du site"""
    # on retourne le templates (le fichier html)
    return render (request, 'monsite/index.html', )


def inscription(request):
    """sert à créer un compte"""
    if len(request.GET) > 0:
        form = FormProfilEtudiant(request.GET)

        if form.is_valid():
            form.save()
            return redirect('/connexion')
        else:
            return render (request, 'monsite/profil.html', {'form': form})
    else:
        form = FormProfilEtudiant()
        return render (request, 'monsite/profil.html', {'form', form})


def connexion(request):
    """sert à s'authentifier"""
    # (2) si le formulaire a été soumis
    if len(request.POST) > 0:
        # (2) initialiser
        form = FormConnexion(request.POST)
        # si
        if form.is_valid() :
            return redirect('/index')
        else:
            return render (request, 'monsite/connexion.html', {'form': form})
    else:
        # (1) tant que le formulaire n'a pas été soumis,
        form = FormConnexion()
        return render(request, 'monsite/connexion.html', {'form': form})


def modification(request):
    """sert à modifier des informations personnelles de l'internaute"""
    return render (request, 'monsite/modification.html')


def profil(request):
    """sert à afficher soit le profil de l'utilisateur connecté, soit celui de l'un de ses amis"""
    return render (request, 'monsite/profil.html')



def ajout(request):
    """sert à ajouter un ami à partir de son adresse e-mail"""
    return render (request, 'monsite/ajout.html')
