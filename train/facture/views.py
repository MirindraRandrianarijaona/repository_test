from django.shortcuts import render, redirect
from .models import Facture
from .forms import FactureForm

# Vue pour afficher la liste des factures
def facture_list(request):
    factures = Facture.objects.all()  # Récupère toutes les factures
    return render(request, 'facture/liste_factures.html', {'factures': factures})

# Vue pour afficher et traiter le formulaire d'ajout d'une facture
def ajouter_facture(request):
    if request.method == 'POST':
        form = FactureForm(request.POST)  # Crée un formulaire avec les données POST
        if form.is_valid():  # Si les données sont valides
            form.save()  # Sauvegarde la nouvelle facture dans la base de données
            return redirect('facture_list')  # Redirige vers la liste des factures
    else:
        form = FactureForm()  # Crée un formulaire vide pour GET
    
    return render(request, 'facture/ajouter_facture.html', {'form': form})