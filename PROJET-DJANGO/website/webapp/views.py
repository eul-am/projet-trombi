from django.shortcuts import render

# On importe tous les formulaires depuis forms.py
from .forms import Login_Form, Register_Form


#
def login(request):
    #
    form = Login_Form()
    #
    return render(request, 'webapp/login.html', {'form': form})


#
def register(request):
    #
    form = Login_Form()
    #
    return render(request, 'webapp/register.html', {'form': form})
