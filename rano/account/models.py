from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Ajoutez ici vos champs personnalisés
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    # Exemple : champ pour la date de naissance
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
