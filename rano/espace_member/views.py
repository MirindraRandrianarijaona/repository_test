from django.shortcuts import render

def member_home(request):
    """
    Vue pour la page d'accueil.
    """
    return render(request, 'espace_member/member_home.html')
