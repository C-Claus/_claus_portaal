from django.db import models


from claus_administratie.models import BedrijfsAdministratie


class KostenCode(models.Model):

    kostencode_status = (('Actief', 'Actief'), 
                        ('Inactief', 'Inactief'),)

    nummer = models.CharField(max_length=20)
    omschrijving = models.CharField(max_length=200)

    bedrijfsadministratie = models.ForeignKey(BedrijfsAdministratie, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=kostencode_status)

    class Meta:
        verbose_name_plural = "Kostencodes"

    def __str__(self):
        return self.nummer + ' ' + self.omschrijving 