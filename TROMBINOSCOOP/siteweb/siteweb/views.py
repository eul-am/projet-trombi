from django.shortcuts import render

# définir la vue (le nom de la page web : son rôle de la page, sa fonction)
def index(request):
    """page d'index du site"""
    # on retourne le templates (le fichier html)
    return render (request, 'siteweb/index.html')