from django.shortcuts import render, redirect
# On importe tous les formulaires depuis forms.py
from .forms import Login_Form, Register_Form, Part_Profile_Form, Ent_Profile_Form
from .models import User, Particulier


# Inscription
def register(request):
    # Si une requête n'a pas encore été effectuée (1)
    if not request.method == 'POST':
        # Créez un formulaire vierge (2)
        form = Register_Form()
        # À retourner vers la page d'inscription (3)
        return render(request, 'webapp/inscription.html', {'form': form})
    # sinon,
    else:
        # la variable form est un formulaire vierge
        form = Register_Form(request.POST)
        #
        if form.is_valid():
            # Sauvegarder les données
            form.save()
            # Rediriger l'utilisateur vers la page de connexion
            return redirect('connexion')

        else:
            return render(request, 'webapp/inscription.html', {'form': form})


# Page de connexion
def login(request):
    # si la requête n'a pas (encore) été effectuée 1
    if not request.method == 'POST':
        # créer un formulaire (vierge) 2
        form = Login_Form()
        # et l'envoyer vers page de connexion 3
        return render(request, 'webapp/connexion.html', {'form': form})
    # ou bien 4
    else:
        #
        form = Login_Form(request.POST)
        # 5
        if form.is_valid():
            # 6 on nettoie l'email de l'utilisateur
            user_email = form.cleaned_data['email']
            # 7 on compare avec celui de la base de données
            logged_user = User.objects.get(email=user_email)
            # 8 on créé la session
            request.session['logged_user_id'] = logged_user.id
            #
            return redirect('bienvenue')
        # 7
        else:
            # 8
            return render(request, 'webapp/connexion.html', {'form': form})


# On vérifie que l'utilisateur est bien authentifié
def get_logged_user_from_request(request):
    "Fonction dont le rôle est de récupérer, le cas échéant, l'utilisateur authentifié de la base de données"

    if 'logged_user_id' in request.session:

        logged_user_id = request.session['logged_user_id']

        # On cherche un type d'utilisateur (donc une Table, un modèle)
        if len(User.objects.filter(id=logged_user_id)) == 1:
            return User.objects.get(id=logged_user_id)

        else:
            return None
    else:
        return None


def bienvenue(request):
    # Vérification que l'utilisateur est authentifié
    logged_user = get_logged_user_from_request(request)
    #
    if logged_user:
        return render(request, 'webapp/bienvenue.html', {'logged_user': logged_user})

    else:
        return redirect('connexion')


def profile(request):
    # Vérification que l'utilisateur est authentifié
    logged_user = get_logged_user_from_request(request)
    #
    if logged_user:
        if 'User' in request.POST and request.POST['User'] != '':
            #
            User_id = int(request.POST['User'])
            #
            donnees = User.objects.filter(id=User_id)

            if len(donnees) == 1:
                return render(request, 'webapp/profile.html', {'User': User})

            else:
                return render(request, 'webapp/profile.html', {'User': logged_user})

        else:
            return render(request, 'webapp/profile.html', {'User': logged_user})

    else:
        return redirect('connexion')


def modification(request):
    # Vérification que l'utilisateur est authentifié
    logged_user = get_logged_user_from_request(request)
    #
    if logged_user:
        #
        if len(request.POST) > 0:
            #
            if type(logged_user) == Particulier:
                #
                form = Part_Profile_Form(request.POST, instance=logged_user)
            else:
                form = Ent_Profile_Form(request.POST, instance=logged_user)
            if form.is_valid:
                form.save()
                return redirect('bienvenue')
            else:
                return render(request, 'webapp/modify_profile.html', {'form': form})
        else:
            if type(logged_user) == Particulier:
                form = Part_Profile_Form(request.POST, instance=logged_user)
            else:
                form = Ent_Profile_Form(request.POST, instance=logged_user)
            return render(request, 'webapp/modify_profile.html', {'form': form})
    else:
        return redirect('connexion')
