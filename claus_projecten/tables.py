from django_tables2 import tables, TemplateColumn
from django_tables2.utils import Accessor
from .models import Projecten


class ProjectenTable(tables.Table):

   class Meta:
      model = Projecten
      template_name = "django_tables2/bootstrap-responsive.html"
      fields = (  'projectnummer',
                  'projectomschrijving', 
                  'bedrijfsadministratie',
                  'projectleider',
                  'status',
               )
              

   details = TemplateColumn(template_name='claus_projecten/button_tabel_details.html')

   bewerk = TemplateColumn(template_name='claus_projecten/button_tabel_wijzig.html')

   archiveer = TemplateColumn(template_name='claus_projecten/button_tabel_archiveer.html')