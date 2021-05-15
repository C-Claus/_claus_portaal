from django.db import models

from claus_personen.models import Personen
from claus_administratie.models import BedrijfsAdministratie
from claus_projecten.models import Projecten
from claus_projecttaken.models import ProjectTaak

class Planning(models.Model):

      status = (('Actief','Actief'), ('Inactief','Inactief'))

      persoon = models.ForeignKey(Personen, on_delete=models.CASCADE)
      project = models.ForeignKey(Projecten, on_delete=models.CASCADE)
      projecttaak = models.ForeignKey(ProjectTaak, on_delete=models.CASCADE)
      
      datum = models.DateField()
      begintijd = models.TimeField()
      eindtijd = models.TimeField()
      status = models.CharField(max_length=100, choices=status)

      class Meta:
        verbose_name_plural = "Planningen"