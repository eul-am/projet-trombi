from django.shortcuts import render, redirect
# On importe tous les formulaires depuis forms.py
from .forms import Login_Form, Register_Form
# Create your views here.
from .models import User

#
def login(request):
    #
    if request.method == 'POST':
        #
        form = Login_Form(request.POST)
        #
        if form.is_valid():
            #
            email = form.cleaned_data['email']
            #
            utilisateur = User.objects.get(email=email)
            #
            request.session['id'] = utilisateur.id
            # Rediriger vers une autre page
            return redirect('index')
        #
        else:
            #
            return render(request, 'webapp/login.html', {'form': form})
    #
    else:
        #
        form = Login_Form()
        #
    return render(request, 'webapp/login.html', {'form': form})


#
def register(request):
    # On initialise les variables

    if request.method == 'POST':
        #
        form = Register_Form(request.POST)
        #
        if form.is_valid():
            #  Nettoyer les données
            form.save()
            # Rediriger vers une autre page
            return redirect('login')
        # if a GET (or any other method) we'll create a blank form
    else:
        #
        form = Register_Form()
        #
    return render(request, 'webapp/login.html', {'form': form})




#
def index(request):

    return render(request, 'webapp/index.html')
