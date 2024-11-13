# account/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import LoginForm, SignupForm, CustomUserUpdateForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    """
    Vue pour la page de connexion.
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Vous êtes maintenant connecté.")
            return redirect('home')
        else:
            messages.error(request, "Les informations de connexion sont incorrectes.")
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})

def signup_view(request):
    """
    Vue pour la page d'inscription.
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect('home')
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = SignupForm()

    return render(request, 'account/signup.html', {'form': form})

def logout_view(request):
    """
    Vue pour se déconnecter.
    """
    logout(request)
    # Supprime tous les messages précédents
    storage = messages.get_messages(request)
    storage.used = True

    messages.success(request, "Vous avez été déconnecté.")
    return redirect('login')


@login_required
def update_profile(request):
    """
    Vue pour modifier le profil de l'utilisateur.
    """
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre profil a été mis à jour avec succès.")
            return redirect('home')  # Redirige vers une page appropriée après la mise à jour
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = CustomUserUpdateForm(instance=request.user)

    return render(request, 'account/update_profile.html', {'form': form})