from django.shortcuts import render, redirect
from .forms import Connexion
from .models import Personne

def welcome(request):

    return render(request, 'applidjango/bienvenue.html')

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

