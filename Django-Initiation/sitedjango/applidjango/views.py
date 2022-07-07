from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import Connexion, Form_Profil_Utilisateur, Form_Ajout_Ami, Form_Modif_Profil
from .models import Personne, Message

def welcome(request):

    utilisateur = utilisateur_en_ligne(request)
    if utilisateur:
        if 'newMessage' in request.POST and request.POST['newMessage'] != '':
            newMessage = Message(auteur=utilisateur, contenu=request.POST['newMessage'], date_de_publication=date.today())
            newMessage.save()
        friendMessages = Message.objects.filter(auteur__ami=utilisateur).order_by('-date_de_publication')
        return render(request, 'applidjango/bienvenue.html', {'utilisateur': utilisateur,
                                                              'friendMessages': friendMessages})
    else:
        return redirect('connexion')


def login(request):
    # dès que l'utilisateur (nous) envoie ses données (4)
    if request.method == 'POST':
        # on remplis le formulaire
        form = Connexion(request.POST)
        # si le formulaire est valide
        if form.is_valid():

            # on nettoie d'abord toutes les valeurs des champs les données saisies
            email = form.cleaned_data['email']

            # on récupère l'email existant dans la base de données et on le compare avec celui saisi par l'utilisateur
            utilisateur = Personne.objects.get(email=email)

            # On ouvre la session (de l') utilisateur
            request.session['utilisateur'] = utilisateur.id

            # on redirige l'utilisateur vers la page ...
            return redirect('bienvenue')

        # s'il y a une erreur de saisie
        else:
            # on l'indique sur la page de connexion
            return render(request, 'applidjango/connexion.html', {'form': form})

    # avant traitement des données, (3)
    else:
        # on créé une variable vide : (1)
        form = Connexion()
        # dont le contenu s'affiche dans cette vue (view.py) (2)
        return render(request, 'applidjango/connexion.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = Form_Profil_Utilisateur(request.POST)

        if form.is_valid():
            form.save()
            return redirect('connexion')

        else:
            form = Form_Profil_Utilisateur()
            return render(request, 'applidjango/profil_utilisateur.html', {'form': form})
    else:
        form = Form_Profil_Utilisateur()
        return render(request, 'applidjango/profil_utilisateur.html', {'form': form})


def utilisateur_en_ligne(request):
    """ fonction qui a pour rôle de vérifier si un utilisateur est authentifié;
       elle récupère également l'utilisateur authentifié dans la base de données. """

    # si l'utilisateur est (bien) connecté à la session
    if 'utilisateur' in request.session:
        # utilisateur est sa variable de session
        utilisateur = request.session['utilisateur']
        # si
        if len(Personne.objects.filter(id=utilisateur)) == 1:
            # retournez le
            return Personne.objects.get(id=utilisateur)
        # sinon,
        else:
            # ne rien afficher
            return None
    else:
        return None


def add_friend(request):

    utilisateur = utilisateur_en_ligne(request)
    if utilisateur:
        if len(request.POST) > 0:
            form = Form_Ajout_Ami(request.POST)
            if form.is_valid():
                email_nouvel_ami = form.cleaned_data['email']
                # récupérer l'email de l'ami(e) (de l'utilisateur à ajouter)
                nouvel_ami = Personne.objects.get(email=email_nouvel_ami)
                utilisateur.ami.add(nouvel_ami)  # PROBLEME
                utilisateur.save()
                return redirect('bienvenue')
            else:
                form = Form_Ajout_Ami()
                return render(request, 'applidjango/ajout_amis.html', {'form': form})
            # Le formulaire n’a pas été envoyé
        else:
            form = Form_Ajout_Ami()
            return render(request, 'applidjango/ajout_amis.html', {'form': form})
    else:
        return redirect('connexion')


def show_profile(request):

    utilisateur = utilisateur_en_ligne(request)

    # si l'utilisateur est en ligne
    if utilisateur:
        if 'profil' in request.POST and request.POST['profil'] != '':
            id_profil = int(request.POST['profil'])
            donnees = Personne.objects.filter(id=id_profil)
            if len(donnees) == 1:
                if Personne.objects.filter(id=id_profil):
                    profil = Personne.objects.get(id=id_profil)
                return render(request, 'applidjango/voir_profil.html', {'profil': profil})
            else:
                return render(request, 'applidjango/voir_profil.html', {'profil': utilisateur})
        else:
            return render(request, 'applidjango/voir_profil.html', {'profil': utilisateur})

    # s'il n'est pas en ligne,
    else:
        return redirect('connexion')


def modify_profile(request):
    # Vérification que l'utilisateur est authentifié
    utilisateur = utilisateur_en_ligne(request)
    if utilisateur:
        if len(request.POST) > 0:
            form = Form_Modif_Profil(request.POST, instance=utilisateur)
            if form.is_valid:
                form.save()
                return redirect('bienvenue')
            else:
                form = Form_Modif_Profil(instance=utilisateur)
                return render(request, 'applidjango/modification_profil.html', {'form': form})
        else:
            form = Form_Modif_Profil(instance=utilisateur)
            return render(request, 'applidjango/modification_profil.html', {'form': form})
    else:
        return redirect('connexion')


def logout(request):
    del request.session['utilisateur']
    return redirect(request, 'applidjango/deconnexion.html')

