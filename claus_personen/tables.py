from django_tables2 import tables, TemplateColumn
from django_tables2.utils import Accessor
from .models import Personen



class PersoonsGegevens(tables.Table):

   class Meta:
      model = Personen 
      


class PersonenTable(tables.Table):

   class Meta:
      model = Personen
      template_name = "django_tables2/bootstrap-responsive.html"

      fields = (  'persoonnr',
                  'naam', 
                  'in_dienst_status',
                  'administratie_werkgever',
                  'gebruikersgroep',
                  'account',
               )
              

   details = TemplateColumn(template_name='claus_persoon/button_tabel_details.html')

   bewerk = TemplateColumn(template_name='claus_persoon/button_tabel_wijzig.html')