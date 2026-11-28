from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Event(models.Model):
    class Categorie(models.TextChoices):
        sport = "sport"
        Agriculture = "Agriculture"
        bussiness = "bussiness"
        technologie = "technologie"

    title = models.CharField(max_length=200)
    description = models.TextField()

    categorie = models.CharField(max_length=20, choices=Categorie.choices, default=Categorie.sport)

    date_debut = models.DateTimeField()
    duree = models.PositiveIntegerField()
    lieu = models.CharField(max_length=30)
    capacite = models.IntegerField(validators=[MinValueValidator(50, message="L'évenement doit acceuillir au mois 50 personne")])


    class Meta:
        ordering = ["-date_debut"]

    def __str__(self):
        return self.title