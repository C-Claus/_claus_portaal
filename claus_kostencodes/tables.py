from django_tables2 import tables, TemplateColumn
from django_tables2.utils import Accessor
from .models import KostenCode


class KostenCodeTable(tables.Table):

   class Meta:
      model = KostenCode
      template_name = "django_tables2/bootstrap-responsive.html"
      fields = ('nummer','omschrijving','status', 'bedrijfsadministratie')

   #details = TemplateColumn(template_name='claus_administratie/button_tabel_details.html')

   bewerk = TemplateColumn(template_name='claus_kostencodes/button_tabel_wijzig.html')
