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
        # si
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


def accueil(request):
    """ Cette fonction affiche la page d'accueil """

    if 'id' in request.session:
        id_utilisateur = request.session['id']
        utilisateur = Utilisateur.objects.get(id=id_utilisateur)
        return render(request, 'webapp/accueil.html', {'utilisateur': utilisateur})
    else:
        return redirect('connexion')


