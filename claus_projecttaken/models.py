from django.db import models

class ProjectTaak(models.Model):

      status = (('Actief','Actief'), ('Inactief','Inactief'))

      nummer = models.CharField(max_length=10)
      omschrijving = models.CharField(max_length=200)
      status = models.CharField(max_length=100, choices=status)

      class Meta:
        verbose_name_plural = "Projecttaken"

      def __str__(self):
            return self.omschrijving
            