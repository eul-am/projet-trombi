from django.shortcuts import render, redirect

# On importe tous les formulaires depuis forms.py
from .forms import FormConnexion, FormInscription

# Create your views here.
from .models import Utilisateur


def connexion(request):
    """ Cette fonction affiche la page de connexion et permet de s'authentifier """
    # (2) si le formulaire a été soumis
    if len(request.POST) > 0:
        # (2) initialiser
        form = FormConnexion(request.POST)
        # si
        if form.is_valid():
            # récupère l'email que l'utilisateur a saisi
            #email_utilisateur = form.donnee['email']
            # récupérer l'utilisateur à qui cet email appartient
            #utilisateur_connecte = Utilisateur.objects.get(email=email_utilisateur)
            # sauvegarder l'id de cette personne dans la session
            #request.session['id_utilisateur_connecte'] = utilisateur_connecte.id
            # puis on fait la redirection vers la page d'accueil
            return redirect('accueil')
        else:
            return render(request, 'webapp/connexion.html', {'form': form})
    else:
        # (1) tant que le formulaire n'a pas été soumis,
        form = FormConnexion()
        return render(request, 'webapp/connexion.html', {'form': form})


def inscription(request):
    """ Cette fonction affiche la page d'inscription """
    # (1) si au moins 1 formulaire a été soumis
    if len(request.POST) > 0:
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


def accueil(request):
    """ Cette fonction affiche la page d'accueil """
    return render(request, 'webapp/accueil.html', )
