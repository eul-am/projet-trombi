
from django.shortcuts import render, redirect
from .forms import Form_Connexion, Form_Inscription, Form_Modification_Profile
from .models import Utilisateur


# décorateur : Si l’utilisateur est connecté, il exécute la vue normalement.
# Le code de la vue peut légitimement considérer l’utilisateur comme connecté.

def connexion(request):
    # dès que l'utilisateur (nous) envoie ses données (4)
    if request.method == 'POST':
        # on remplis le formulaire
        form = Form_Connexion(request.POST)
        # si le formulaire est valide
        if form.is_valid():

            # on nettoie d'abord toutes les valeurs des champs les données saisies
            email = form.cleaned_data['email']

            # on récupère l'email existant dans la base de données et on le compare avec celui saisi par l'utilisateur
            utilisateur_en_ligne = Utilisateur.objects.get(email=email)

            # On cré la session
            request.session['id_utilisateur_en_ligne'] = utilisateur_en_ligne.id

            # on redirige l'utilisateur vers la page ...
            return redirect('bienvenue')

        # s'il y a une erreur de saisie
        else:
            # on l'indique sur la page de connexion
            return render(request, 'webapp/connexion.html', {'form': form})

    # avant traitement des données, (3)
    else:
        # on créé une variable vide : (1)
        form = Form_Connexion()
        # dont le contenu s'affiche dans cette vue (view.py) (2)
        return render(request, 'webapp/connexion.html', {'form': form})


def inscription(request):
    if request.method == 'POST':

        form = Form_Inscription(request.POST)

        if form.is_valid():
            form.save()

            return redirect('connexion')

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

        if len(Utilisateur.objects.filter(id=id_utilisateur_en_ligne)) == 1:

            return Utilisateur.objects.get(id=id_utilisateur_en_ligne)

        else:
            return None
    else:
        return None


def deconnexion(request):

    del request.session['id_utilisateur_en_ligne']

    return redirect(request, 'webapp/connexion.html')




def affichage_profile(request):
    # Vérification que l'utilisateur est authentifié
    utilisateur_en_ligne = recherche_utilisateur_en_ligne(request)
    #
    if utilisateur_en_ligne:

        if 'donnees_profile' in request.POST and request.POST['donnees_profile'] != '':
            #
            id_donnees_profile = int(request.POST['donnees_profile'])
            #
            donnees = Utilisateur.objects.filter(id=id_donnees_profile)

            if len(donnees) == 1:

                if Utilisateur.objects.filter(id=id_donnees_profile):
                    donnees_profile = Utilisateur.objects.get(id=id_donnees_profile)

                return render(request, 'webapp/affichage_profile.html', {'donnees_profile': donnees_profile})

            else:
                return render(request, 'webapp/affichage_profile.html', {'donnees_profile': utilisateur_en_ligne})

        else:
            return render(request, 'webapp/affichage_profile.html', {'donnees_profile': utilisateur_en_ligne})

    else:
        return redirect('connexion')


def modification_profile(request):

    # Vérification que l'utilisateur est authentifié
    utilisateur_en_ligne = recherche_utilisateur_en_ligne(request)
    #
    if utilisateur_en_ligne:
        #
        if len(request.POST) > 0:
            #
            if type(utilisateur_en_ligne) == Utilisateur:
                #
                form = Form_Modification_Profile(request.POST, instance=utilisateur_en_ligne)

                if form.is_valid:
                    form.save()
                    return redirect('bienvenue')
        else:
            form = Form_Modification_Profile(instance=utilisateur_en_ligne)
            return render(request, 'webapp/modification_profile.html', {'form': form})
    else:
        return redirect('connexion')


def suppression_profile(request):

    # Vérification que l'utilisateur est authentifié
    utilisateur_en_ligne = recherche_utilisateur_en_ligne(request)
    #
    if utilisateur_en_ligne:
        #
        if len(request.POST) > 0:
            #
            if type(utilisateur_en_ligne) == Utilisateur:
                #
                form = Form_Suppression_Profile(request.POST, instance=utilisateur_en_ligne)

                if form.is_valid:
                    form.save()
                    return redirect('bienvenue')
        else:
            form = Form_Modification_Profile(instance=utilisateur_en_ligne)
            return render(request, 'webapp/suppression_profile.html', {'form': form})
    else:
        return redirect('connexion')
