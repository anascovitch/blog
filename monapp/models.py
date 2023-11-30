# Create your models here.
from django.db import models
from django.conf import settings 
from django.contrib.auth.models import AbstractUser

# Modèle pour les posts
# class Post(models.Model):
#     titre = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     image = models.ImageField(upload_to='monapp/images/')
#     auteur = models.ForeignKey(User, on_delete=models.CASCADE)
#     date_creation=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.titre
    
#     class Meta:
#         ordering= ['-date_creation']

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     birth_date = models.DateField(null=True, blank=True)

#     # Vous pouvez ajouter d'autres champs ici si nécessaire

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('subscriber', 'Abonné'),
        ('creator', 'Créateur'),
        ('admin', 'Administrateur'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='subscriber')
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

class ImagePost(models.Model):
    titre = models.CharField(max_length=255)  # Intitulé du post
    description = models.TextField(blank=True)  # Description de l'image, facultatif
    image = models.ImageField(upload_to='images/')  # Chemin où les images seront stockées
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # L'auteur de l'image
    date_creation = models.DateTimeField(auto_now_add=True)  # Date de création du post

    def __str__(self):
        return self.titre  # Retourne le titre dans l'interface d'administration

    class Meta:
        ordering = ['-date_creation']  # Ordonne les posts par date de création descendante
