from django.db import models

# Create your models here.
class Etatcivil(models.Model):
    numero_ordre=models.IntegerField(blank=True)
    nom_prenom=models.CharField(max_length=30)
    cin=models.CharField(max_length=10)
    dossier=models.FileField(null=True,blank=True)
    

