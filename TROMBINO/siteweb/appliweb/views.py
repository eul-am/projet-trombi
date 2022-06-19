# On importe tous les formulaires depuis forms.py
from .forms import FormConnexion, FormProfilEtudiant, FormProfilEmploye
#
from django.shortcuts import render, redirect
#
from .models import Personne, Etudiant, Employe


def connexion(request):
    """ Cette fonction affiche la page de connexion """
    # (2) si le formulaire a été soumis
    if len(request.POST) > 0:
        # (2) initialiser
        form = FormConnexion(request.POST)
        # si
        if form.is_valid():
            # récupère l'email que l'utilisateur a saisi
            email_utilisateur = form.donnee['email']
            # récupérer l'utilisateur à qui cet email appartient
            utilisateur_connecte = Personne.objects.get(email=email_utilisateur)
            # sauvegarder l'id de cette personne dans la session
            request.session['id_utilisateur_connecte'] = utilisateur_connecte.id
            # puis on fait la redirection vers la page d'accueil
            return redirect('bienvenue')
        else:
            return render(request, 'appliweb/connexion.html', {'form': form})
    else:
        # (1) tant que le formulaire n'a pas été soumis,
        form = FormConnexion()
        return render(request, 'appliweb/connexion.html', {'form': form})


# ici on gère la session : on vérifie si un utilisateur est connecté
def bienvenue(request):
    """ Cette fonction donne accès à la page de bienvenue """
    utilisateur_connecte = trouve_utilisateur_connecte(request)
    # si on a un id utilisateur dans la session,
    if utilisateur_connecte :
        #
        return render(request, 'appliweb/bienvenue.html', {'utilisateur_connecte': utilisateur_connecte})
    # sinon
    else:
        # renvoyer
        return redirect('connexion')


""" Gestion des formulaires d'inscriptions des Étudiants et des Employés """
def inscription(request):
    """ Cette fonction affiche la page de connexion """
    # (1) si au moins 1 formulaire a été soumis
    if len(request.POST) > 0 and 'TypeProfil' in request.POST:
        # (2) initialiser
        formEtudiant = FormProfilEtudiant(prefix='etu')
        formEmploye = FormProfilEmploye(prefix='emp')
        # si
        if request.POST['TypeProfil'] == 'etudiant':
            formEtudiant = FormProfilEtudiant(request.POST, prefix='etu')
            if formEtudiant.is_valid():
                formEtudiant.save()
                return redirect('connexion')
        elif request.POST['TypeProfil'] == 'employe':
            formEmploye = FormProfilEmploye(request.POST, prefix='emp')
            if formEmploye.is_valid():
                formEmploye.save()
                return redirect('connexion')
            # Le formulaire envoyé n’est pas valide
        return render(request, 'appliweb/profil_utilisateur.html',
                      {'formEtudiant': formEtudiant, 'formEmploye': formEmploye})

    else:  # (2)
        # () tant que le formulaire n'a pas été soumis,
        formEtudiant = FormProfilEtudiant(request.POST, prefix='etu')
        formEmploye = FormProfilEmploye(request.POST, prefix='emp')

        return render(request, 'appliweb/profil_utilisateur.html',
                      {'formEtudiant': formEtudiant, 'formEmploye': formEmploye})

# Protection des pages privées : fonction dont le rôle sera également de récupérer, le cas échéant, l’utilisateur
# authentifié de la base de données.
def trouve_utilisateur_connecte(request):
    # si on trouve un id d’utilisateur dans la session
    if 'id_utilisateur_connecte' in request.session:
        id_utilisateur_connecte = request.session['id_utilisateur_connecte']
        # On cherche un etudiant
        if len(Etudiant.objects.filter(id=id_utilisateur_connecte)) == 1:
            return Etudiant.objects.get(id=id_utilisateur_connecte)
        # On cherche un Employé
        elif len(Employe.objects.filter(id=id_utilisateur_connecte)) == 1:
            return Employe.objects.get(id=id_utilisateur_connecte)
        # Si on n’a rien trouvé,
        else:
            return None
    #  Si rien n’est trouvé, alors on retourne None
    else:
        return None
