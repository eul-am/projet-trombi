from django.shortcuts import render, redirect
# On importe tous les formulaires depuis forms.py
from .forms import Login_Form, Register_Form
from .models import User


# Page de connexion
def login(request):
    # si la requête n'a pas (encore) été effectuée
    if not request.method == 'POST':
        # créer un formulaire (vierge)
        form = Login_Form()
        # qui s'affiche à la page de connexion
        return render(request, 'webapp/connexion.html', {'form': form})
    # ou bien
    else:
        #
        form = Login_Form(request.POST)
        #
        if form.is_valid():
            #
            user_email = form.cleaned_data['email']
            #
            logged_user = User.objects.get(email=user_email)
            #
            request.session['logged_user_id'] = logged_user.id
            #
            return redirect('bienvenue')


#
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
            # Sauvegarder les formulaires
            form.save()
            # Rediriger vers une autre page
            return redirect('connexion')


#
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
    # Vérufication que l'utilisateur est authentifié
    logged_user = get_logged_user_from_request(request)

    if logged_user:
        return render(request, 'webapp/bienvenue.html', {'logged_user': logged_user})

    else:
        return redirect('connexion')
