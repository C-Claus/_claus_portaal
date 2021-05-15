
from claus_uren.models import UrenRegistratie
from django_tables2 import tables, TemplateColumn
import django_tables2 as tables



class UrenRegistratieTable(tables.Table):

   projectnr = tables.Column(verbose_name='Project')

   class Meta:
      model = UrenRegistratie
      template_name = "django_tables2/bootstrap-responsive.html"

      fields = ('projectnr', 'kostencode', 'aantal_uur', 'registratie_status')
      #fields = ('projectnr','kostencode','aantal_uur','datum')
      #fields = ('datum','aantal_uur','registratie_status','opmerking','bedrijfsadministratie_id','kostencode','persoonnr','projectnr')


   bewerk = TemplateColumn(template_name="claus_uren/button_registratie_wijzig.html")  
   verwijder = TemplateColumn(template_name="claus_uren/button_registratie_verwijder.html")  


class UrenRegistratieTableBevestigd(tables.Table):

   projectnr = tables.Column(verbose_name='Project')

   class Meta:
      model = UrenRegistratie
      template_name = "django_tables2/bootstrap-responsive.html"

      fields = ('projectnr', 'kostencode', 'aantal_uur', 'registratie_status')
