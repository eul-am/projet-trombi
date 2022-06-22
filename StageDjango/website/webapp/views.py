from django.shortcuts import render, redirect

# On importe tous les formulaires depuis forms.py
from .forms import FormConnexion, Form_inscription_Particulier, Form_inscription_Entreprise

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
            email = form.cleaned_data['email']
            utilisateur = Utilisateur.objects.get(email=email)
            request.session['id'] = utilisateur.id
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
    if len(request.POST) > 0 and 'TypeProfil' in request.POST:
        # (2) initialiser
        formE = Form_inscription_Entreprise(prefix='en')
        formP = Form_inscription_Particulier(prefix='pa')
        # si le contenu de la variable POST est une entreprise
        if request.POST['TypeProfil'] == 'entreprise':
            formE = Form_inscription_Entreprise(request.POST, prefix='en')
            if formE.is_valid():
                formE.save()
                return redirect('connexion')

        elif request.POST['TypeProfil'] == 'particulier':
            formP = Form_inscription_Particulier(request.POST, prefix='pa')
            if formP.is_valid():
                formP.save()
                return redirect('connexion')

        return render(request, 'webapp/donnees_utilisateur.html', {'formE': formE, 'formP': formP})

    else:  # (2)
        # () tant que le formulaire n'a pas été soumis,
        formE = Form_inscription_Entreprise(request.POST, prefix='en')
        formP = Form_inscription_Particulier(request.POST, prefix='pa')
        return render(request, 'webapp/donnees_utilisateur.html', {'formE': formE, 'formP': formP})


# Protection des pages privées : fonction dont le rôle est également de récupérer, le cas échéant, l’utilisateur
# authentifié de la base de données.
def utilisateur_connecte(request):
    
    # si on trouve un id d’utilisateur dans la session
    if 'id' in request.session:
        id_utilisateur = request.session['id']
        # On cherche un etudiant
        if len(Etudiant.objects.filter(id=id_utilisateur)) == 1:
            return Etudiant.objects.get(id=id_utilisateur)
        # On cherche un Employé
        elif len(Employe.objects.filter(id=id_utilisateur)) == 1:
            return Employe.objects.get(id=id_utilisateur)
        # Si on n’a rien trouvé,
        else:
            return None
    #  Si rien n’est trouvé, alors on retourne None
    else:
        return None


def accueil(request):
    """ Cette fonction affiche la page d'accueil """
    # une connexion réussie est un utilisateur connecté
    connexion_reussie = connexion (request)
    # si la connexion réussie,
    if connexion_reussie:
        # rendez-vous vers la page d'accueil
        return render(request, 'webapp/accueil.html', {'utilisateur_connecte': utilisateur_connecte})
    # sinon,
    else:
        # restez sur la page de connexion
        return redirect('connexion')
