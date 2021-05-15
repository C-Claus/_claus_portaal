from django.db import models

class BedrijfsAdministratie(models.Model):

    bedrijfs_status = (('Actief','Actief'),
                        ('Inactief','Inactief'),)

    bedrijfsnummer = models.CharField(max_length=10)
    bedrijfsnaam = models.CharField(max_length=200)
    kvk_nummer = models.CharField(max_length=200)
    vestigings_nummer = models.CharField(max_length=200)

    straatnaam_nummer = models.CharField(max_length=200)
    postcode = models.CharField(max_length=200)
    plaats = models.CharField(max_length=200)

    omschrijving = models.CharField(max_length=200)
    
    status = models.CharField(max_length=200, choices=bedrijfs_status)

    class Meta:
        verbose_name_plural = "Bedrijven"

    def __str__(self):
        return self.bedrijfsnummer + " " + self.bedrijfsnaam
