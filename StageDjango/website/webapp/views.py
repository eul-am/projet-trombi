from django.shortcuts import render, redirect

# On importe tous les formulaires depuis forms.py
from .forms import FormConnexion, FormInscription

# Create your views here.
from .models import Utilisateur


def connexion(request):
    """ Cette fonction affiche la page de connexion """

    form = FormConnexion(request.POST)
    return render(request, 'webapp/connexion.html', {'form': form})



""" Gestion des formulaires d'inscriptions des Étudiants et des Employés """
def inscription(request):
    """ Cette fonction affiche la page d'inscription """
    # (1) si au moins 1 formulaire a été soumis
    if len(request.POST) > 0 :
        # (2) initialiser
        form = FormInscription(request.POST)
        # si le formulaire est valide
        if form.is_valid():
            # il faut le sauvegarder
            form.save()
            # et retourner vers la page de connexion
            return redirect('connexion')
        # sinon,
        else:
            # rester sur le formulaire de la page d'inscription
            return render(request, 'webapp/inscription.html', {'form': form})

    else:  # (2)
        # () tant que le formulaire n'a pas été soumis,
        form = FormInscription()
        return render(request, 'webapp/inscription.html', {'form': form})


""" Gestion des formulaires d'inscriptions des Étudiants et des Employés """
def accueil(request):
    """ Cette fonction affiche la page d'accueil """
    return render(request, 'webapp/accueil.html',)