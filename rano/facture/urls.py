from django.urls import path
from . import views

urlpatterns = [
    path('', views.facture_list, name='facture_list'),
    path('ajouter/', views.ajouter_facture, name='ajouter_facture'),
]
