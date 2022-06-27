from django.shortcuts import render, redirect
from .forms import Form_Connexion, Form_Inscription
from .models import Utilisateur


def connexion(request):
    if len(request.POST) > 0:
        form = Form_Connexion(request.POST)
        if form.is_valid():
            # vérification et nettoyage des données
            email_utilisateur = form.cleaned_data['email']
            utilisateur_en_ligne = Utilisateur.objects.get(email=email_utilisateur)
            request.session['id_utilisateur_en_ligne'] = utilisateur_en_ligne.id
            return redirect('bienvenue')
        else:
            return render(request, 'webapp/connexion.html', {'form': form})
    else:
        form = Form_Connexion()
        return render(request, 'webapp/connexion.html', {'form': form})


def inscription(request):
    if len(request.POST) > 0:
        form = Form_Inscription(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bienvenue')
        else:
            return render(request, 'webapp/inscription.html', {'form': form})
    else:
        form = Form_Inscription()
        return render(request, 'webapp/inscription.html', {'form': form})


def bienvenue(request):
    utilisateur_en_ligne = recherche_utilisateur_en_ligne(request)
    if utilisateur_en_ligne:
        return render(request, 'webapp/bienvenue.html', {'utilisateur_en_ligne': utilisateur_en_ligne})
    else:
        return redirect('connexion')


def recherche_utilisateur_en_ligne(request):
    """Protection des pages privées"""

    if 'id_utilisateur_en_ligne' in request.session:
        id_utilisateur_en_ligne = request.session['id_utilisateur_en_ligne']
        # On cherche un etudiant
        if len(Utilisateur.objects.filter(id=id_utilisateur_en_ligne)) == 1:
            return Utilisateur.objects.get(id=id_utilisateur_en_ligne)
        else:
            return None
    else:
        return None


def deconnexion(request):
    try:
        del request.session['id_utilisateur_en_ligne']
    except KeyError:
        pass
    return render(request, 'webapp/connexion.html')