from django.shortcuts import render

def home(request):
    """
    Vue pour la page d'accueil.
    """
    return render(request, 'main/index.html')
