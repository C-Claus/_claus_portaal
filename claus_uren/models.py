from django.db import models
from django.utils import timezone

timezone_now = timezone.now

from claus_administratie.models import BedrijfsAdministratie
from claus_personen.models import Personen
from claus_kostencodes.models import KostenCode
from claus_projecten.models import Projecten
from claus_projecttaken.models import ProjectTaak


class UrenRegistratie(models.Model):

    registratie_status =    (('Ingevoerd','Ingevoerd'),
                            ('Bevestigd','Bevestigd'),
                            ('Goedgekeurd','Goedgekeurd'),
                            ('Afgekeurd','Afgekeurd'),
                            ('Verwerkt','Verwerkt'),)

    persoonnr = models.ForeignKey(Personen, on_delete=models.CASCADE)
    bedrijfsadministratie = models.ForeignKey(BedrijfsAdministratie, on_delete=models.CASCADE, blank=True, null=True)
    projectnr = models.ForeignKey(Projecten, on_delete=models.CASCADE, blank=True, null=True)
    projecttaaknummer = models.ForeignKey(ProjectTaak, on_delete=models.CASCADE, blank=True, null=True)
    kostencode = models.ForeignKey(KostenCode, on_delete=models.CASCADE)
    
    datum = models.DateField(default=timezone.now)
    aantal_uur = models.FloatField()
    opmerking = models.CharField(max_length=500, blank=True)
    registratie_status = models.CharField(max_length=50, choices=registratie_status)
    
    #Dubbele ForeignKey, de relaties moeten gelabeld worden.
    ingevoerd_door = models.ForeignKey(Personen, related_name='%(class)s_ingevoerd_door', on_delete=models.CASCADE)
    geaccordeerd_door = models.ForeignKey(Personen, related_name='%(class)s_geaccordeerd_door', on_delete=models.CASCADE, blank=True, null=True)


    class Meta:
        verbose_name_plural = "UrenRegistratie"