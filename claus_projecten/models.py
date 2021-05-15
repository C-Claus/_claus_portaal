from django.db import models
from django.contrib.auth.models import User

from claus_administratie.models import BedrijfsAdministratie

class Projecten(models.Model):
    project_status = (('Actief', 'Actief'), 
                    ('Inactief', 'Inactief'),
                    ('Afgesloten','Afgesloten'),
                    )

    projectnummer  = models.CharField(max_length=200, blank=True)
    projectomschrijving = models.CharField(max_length=200, blank=True)
    projectleider = models.ForeignKey(User, on_delete=models.CASCADE)
    bedrijfsadministratie = models.ForeignKey(BedrijfsAdministratie, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=project_status)

    class Meta:
        verbose_name_plural = "Projecten"

    def __str__(self):
    
            return  self.projectnummer + ' ' + self.projectomschrijving 
