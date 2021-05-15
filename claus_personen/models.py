from django.db import models
from django.contrib.auth.models import User,  Group, Permission

from claus_administratie.models import BedrijfsAdministratie

class Personen(models.Model):

    #gebruikersgroep_status = (("Administratie","Administratie"), ("Vestigingleider","Vestigingleider"), ("Teamleider","Teamleider"), ("Uitvoerend","Uitvoerend"))


    in_dienst_status = (('Ja','Ja'),('Nee','Nee'),)
    goedkeurder_status  = (('Ja','Ja'),('Nee','Nee'),)

    persoonnr = models.CharField(max_length=30)
    naam = models.CharField(max_length=100)
    administratie_werkgever = models.ForeignKey(BedrijfsAdministratie, on_delete=models.CASCADE)
    in_dienst_status = models.CharField(max_length=200, choices=in_dienst_status)

    persoon_guid = models.CharField(max_length=100)

    gebruikersgroep  = models.ForeignKey(Group, on_delete=models.CASCADE)
 
   
    

    #User model komt uit de standaard Django tabel
    account = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Personen"

    def __str__(self):
        return self.naam