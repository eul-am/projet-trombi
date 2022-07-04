from datetime import date

from django.shortcuts import render, redirect
from .forms import Form_Connexion, Form_Modif_Profile, Form_Inscription, Form_Ajout_Utilisateur, Form_Supp_Profile
from .models import Utilisateur, Message


def login(request):
    # dès que l'utilisateur (nous) envoie ses données (4)
    if request.method == 'POST':
        # on remplis le formulaire
        form = Form_Connexion(request.POST)
        # si le formulaire est valide
        if form.is_valid():

            # on nettoie d'abord toutes les valeurs des champs les données saisies
            email = form.cleaned_data['email']

            # on récupère l'email existant dans la base de données et on le compare avec celui saisi par l'utilisateur
            utilisateur = Utilisateur.objects.get(email=email)

            # On ouvre la session (de l') utilisateur
            request.session['utilisateur'] = utilisateur.id

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

            form = Form_Inscription()

            return render(request, 'webapp/inscription.html', {'form': form})
    else:

        form = Form_Inscription()

        return render(request, 'webapp/inscription.html', {'form': form})


def utilisateur_en_ligne(request):
    """ fonction qui a pour rôle de vérifier si un utilisateur est authentifié;
    elle récupère également l'utilisateur authentifié dans la base de données. """

    # si l'utilisateur est (bien) connecté à la session
    if 'utilisateur' in request.session:
        # utilisateur est sa variable de session
        utilisateur = request.session['utilisateur']
        # si
        if len(Utilisateur.objects.filter(id=utilisateur)) == 1:
            # retournez le
            return Utilisateur.objects.get(id=utilisateur)
        # sinon,
        else:
            # ne rien afficher
            return None
    else:
        return None


def bienvenue(request):
    # toujours initialiser la variable de session
    utilisateur = utilisateur_en_ligne(request)
    # si l'utilisateur est en ligne
    if utilisateur:
        if 'newMessage' in request.POST and request.POST['newMessage'] != '':
            newMessage = Message(auteur=utilisateur,
                                 contenu=request.POST['newMessage'],
                                 date_de_publication=date.today())
            newMessage.save()

        friendMessages = Message.objects.filter(auteur=utilisateur).order_by('-date_de_publication')

        return render(request, 'webapp/bienvenue.html', {'utilisateur': utilisateur,
                                                         'friendMessages': friendMessages})
    # s'il n'est pas en ligne
    else:
        return redirect('connexion')




def deconnexion(request):

    del request.session['utilisateur']

    return redirect(request, 'monappli/deconnexion.html')


def profile(request):
    utilisateur = utilisateur_en_ligne(request)

    # si l'utilisateur est en ligne
    if utilisateur:
        # si
        if 'profile' in request.POST and request.POST['profile'] != '':
            #
            profile = int(request.POST['profile'])
            #
            donnees = Utilisateur.objects.filter(id=profile)

            if len(donnees) == 1:

                if Utilisateur.objects.filter(id=profile):
                    profile = Utilisateur.objects.get(id=profile)

                return render(request, 'webapp/profile.html', {'profile': profile})

            else:
                return render(request, 'webapp/profile.html', {'profile': utilisateur})

        else:
            return render(request, 'webapp/profile.html', {'profile': utilisateur})

    # s'il n'est pas en ligne,
    else:
        return redirect('connexion')


def update_profile(request):
    # Vérification que l'utilisateur est authentifié
    utilisateur = utilisateur_en_ligne(request)
    #
    if utilisateur:
        #
        if len(request.POST) > 0:
            #
            if type(utilisateur) == Utilisateur:
                #
                form = Form_Modif_Profile(request.POST, instance=utilisateur)

                if form.is_valid:
                    form.save()
                    return redirect('bienvenue')
        else:
            form = Form_Modif_Profile(instance=utilisateur)
            return render(request, 'webapp/modification_profile.html', {'form': form})
    else:
        return redirect('connexion')


def del_profile(request):
    # Vérification que l'utilisateur est authentifié
    utilisateur = utilisateur_en_ligne(request)
    #
    if utilisateur:
        #
        if len(request.POST) > 0:
            #
            if type(utilisateur_en_ligne) == Utilisateur:
                #
                form = Form_Supp_Profile(request.POST)

                if form.is_valid:
                    # récupère le seul utilisateur en question
                    utilisateur = Utilisateur.objects.get(id=1)
                    # supprime cet utilisateur
                    utilisateur.delete()

                    return redirect('connexion')
        else:
            # rempli des données de l'utilisateur
            form = Form_Supp_Profile()
            return render(request, 'webapp/suppression_profile.html', {'form': form})
    else:
        return redirect('connexion')


def add_user(request):
    utilisateur = utilisateur_en_ligne(request)

    if utilisateur:

        if len(request.POST) > 0:

            form = Form_Ajout_Utilisateur(request.POST)

            if form.is_valid():

                email = form.cleaned_data['email']
                # récupérer l'email du contact (de l'utilisateur à ajouter)
                contact = Utilisateur.objects.get(email=email)

                # problème à ce niveau
                utilisateur.contact.add(contact)  # PROBLEME

                utilisateur.save()
                return redirect('bienvenue')

            else:

                form = Form_Ajout_Utilisateur()

                return render(request, 'webapp/ajout_utilisateur.html', {'form': form})
            # Le formulaire n’a pas été envoyé
        else:

            form = Form_Ajout_Utilisateur()

            return render(request, 'webapp/ajout_utilisateur.html', {'form': form})
    else:
        return redirect('connexion')
