from django.shortcuts import render, redirect
from .forms import Connexion, Inscription_Employe
from .models import Utilisateur


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
            utilisateur = Utilisateur.objects.get(email=email)

            # On ouvre la session (de l') utilisateur
            request.session['utilisateur'] = utilisateur.id

            # on redirige l'utilisateur vers la page ...
            return redirect('bienvenue')

        # s'il y a une erreur de saisie
        else:
            # on l'indique sur la page de connexion
            return render(request, 'monappli/connexion.html', {'form': form})

    # avant traitement des données, (3)
    else:
        # on créé une variable vide : (1)
        form = Connexion()
        # dont le contenu s'affiche dans cette vue (view.py) (2)
        return render(request, 'monappli/connexion.html', {'form': form})


def logout(request):
    # dès que l'utilisateur (nous) envoie ses données (4)
    if request.method == 'POST':
        # on remplis le formulaire
        form = Connexion(request.POST)
        # si le formulaire est valide
        if form.is_valid():

            # on nettoie d'abord toutes les valeurs des champs les données saisies
            email = form.cleaned_data['email']

            # on récupère l'email existant dans la base de données et on le compare avec celui saisi par l'utilisateur
            utilisateur = Utilisateur.objects.get(email=email)

            # On ouvre la session (de l') utilisateur
            del request.session['utilisateur']

            # on redirige l'utilisateur vers la page ...
            return redirect('connexion')

        # s'il y a une erreur de saisie
        else:
            # on l'indique sur la page de connexion
            return render(request, 'monappli/connexion.html', {'form': form})

    # avant traitement des données, (3)
    else:
        # on créé une variable vide : (1)
        form = Connexion()
        # dont le contenu s'affiche dans cette vue (view.py) (2)
        return render(request, 'monappli/connexion.html', {'form': form})


def welcome(request):
    # toujours initialiser la variable de session
    utilisateur = utilisateur_en_ligne(request)
    # si l'utilisateur est en ligne
    if utilisateur:
        return render(request, 'monappli/bienvenue.html')
    # s'il n'est pas en ligne
    else:
        return redirect('deconnexion')


def register(request):
    if request.method == 'POST':

        form = Inscription_Employe(request.POST)

        if form.is_valid():

            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            sexe = form.cleaned_data['sexe']
            service = form.cleaned_data['service']
            poste = form.cleaned_data['poste']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            form.save()

            return redirect('connexion')

        else:
            form = Inscription_Employe()
            return render(request, 'monappli/profile_utilisateur.html', {'form': form})
    else:

        form = Inscription_Employe()

        return render(request, 'monappli/profile_utilisateur.html', {'form': form})


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
