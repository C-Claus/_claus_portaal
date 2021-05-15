from django_tables2 import tables, TemplateColumn
from django_tables2.utils import Accessor
from .models import BedrijfsAdministratie


class AdministratieTable(tables.Table):

   class Meta:
      model = BedrijfsAdministratie
      template_name = "django_tables2/bootstrap-responsive.html"
      fields = ('bedrijfsnummer','bedrijfsnaam','status')

   details = TemplateColumn(template_name='claus_administratie/button_tabel_details.html')

   bewerk = TemplateColumn(template_name='claus_administratie/button_tabel_wijzig.html')