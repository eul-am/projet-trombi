# (1) on importe les modules render et redirect
from  django.shortcuts import render, redirect
# on importe le (module de) formulaire créé : la classe, le type d’objet 'FormAuthentification'
from appliweb.forms import *

# définir la vue (le nom de la page web : son rôle de la page, sa fonction)
def connexion(request):
    """sert à s'authentifier"""
    # (2) si le formulaire a été soumis
    if len(request.POST) > 0:
        # (2) initialiser
        form = FormConnexion(request.POST)
        # si
        if form.is_valid() :
            return redirect('/bienvenue')
        else:
            return render (request, 'appliweb/connexion.html', {'form': form})
    else:
        # (1) tant que le formulaire n'a pas été soumis,
        form = FormConnexion()
        return render(request, 'appliweb/connexion.html', {'form': form})



# définir la vue (le nom de la page web : son rôle de la page, sa fonction)
def bienvenue(request):
    """page de bienvenue """
    # on retourne le templates (le fichier html)
    return render (request, 'appliweb/bienvenue.html')
