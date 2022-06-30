from datetime import date

from django.shortcuts import render, redirect
from .forms import Form_Connexion, Form_Modification_Profile, Form_Inscription, AddFriendForm
from .models import Utilisateur, Message


# CONNEXION -----------------------------------------------------------------------------------------------------------

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


# INSCRIPTION EMPLOYÉ -------------------------------------------------------------------------------------------------

def inscription(request):
    if request.method == 'POST':

        form = Form_Inscription(request.POST)

        if form.is_valid():
            form.save()

            return redirect('connexion')

        else:

            form = Form_Inscription()

            return render(request, 'webapp/inscription.html', {'form': form})
    else:

        form = Form_Inscription()

        return render(request, 'webapp/inscription.html', {'form': form})


# -------------------------------------------------------------------------------------------------------------


def bienvenue(request):
    utilisateur_en_ligne = recherche_utilisateur_en_ligne(request)

    if utilisateur_en_ligne:
        if 'newMessage' in request.POST and request.POST['newMessage'] != '':
            newMessage = Message(auteur=utilisateur_en_ligne,
                                 contenu=request.POST['newMessage'],
                                 date_de_publication=date.today())
            newMessage.save()

        friendMessages = Message.objects.filter(auteur=utilisateur_en_ligne).order_by('-date_de_publication')

        return render(request, 'webapp/bienvenue.html', {'utilisateur_en_ligne': utilisateur_en_ligne,
                                                         'friendMessages': friendMessages})

    else:
        return redirect('connexion')

        # ------------------------------------------------------------------------------------------------------------


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

        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def deconnexion(request):
    del request.session['id_utilisateur_en_ligne']

    return redirect(request, 'webapp/connexion.html')

    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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

        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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

        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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

        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def ajouter_un_utilisateur(request):
    utilisateur_en_ligne = recherche_utilisateur_en_ligne(request)
    if utilisateur_en_ligne:
        # Teste si le formulaire a été envoyé
        if len(request.GET) > 0:
            form = AddFriendForm(request.GET)
            if form.is_valid():
                new_friend_email = form.cleaned_data['email']
                newFriend = Utilisateur.objects.get(email=new_friend_email)
                utilisateur_en_ligne.collegues.add(newFriend)
                utilisateur_en_ligne.save()
                return redirect('bienvenue')
            else:
                form = AddFriendForm()
                return render(request, 'webapp/ajouter_un_utilisateur.html', {'form': form})
            # Le formulaire n’a pas été envoyé
        else:
            form = AddFriendForm()
            return render(request, 'webapp/ajouter_un_utilisateur.html', {'form': form})
    else:
        return redirect('connexion')


def voir_profile_utilisateur(request):
    utilisateur_en_ligne = recherche_utilisateur_en_ligne(request)
    if utilisateur_en_ligne:

        if 'utilisateurAvoir' in request.POST and request.POST['utilisateurAvoir'] != '':

            id_utilisateur_a_voir = int(request.POST['utilisateurAvoir'])

            donnees = Utilisateur.objects.filter(id=id_utilisateur_a_voir)

            if len(donnees) == 1:
                utilisateur_a_voir = Utilisateur.objects.get(id=id_utilisateur_a_voir)

                return render(request, 'webapp/voir_profile_utilisateur.html', {'utilisateur_a_voir': utilisateur_a_voir})

            else:
                return render(request, 'webapp/voir_profile_utilisateur.html', {'utilisateur_a_voir': utilisateur_en_ligne})
                # Le paramètre n’a pas été trouvé
        else:
            return render(request, 'webapp/voir_profile_utilisateur.html', {'utilisateur_a_voir': utilisateur_en_ligne})
    else:
        return redirect('connexion')
