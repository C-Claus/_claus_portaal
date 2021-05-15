from django.db import models

from claus_personen.models import Personen


class Aanwezigheid(models.Model):

      status = (('Actief','Actief'), ('Inactief','Inactief'))

      persoon = models.ForeignKey(Personen, on_delete=models.CASCADE)
    
      
      datum = models.DateField()
      begintijd = models.TimeField()
      eindtijd = models.TimeField()
      status = models.CharField(max_length=100, choices=status)

      class Meta:
        verbose_name_plural = "Aanwezigheid"
