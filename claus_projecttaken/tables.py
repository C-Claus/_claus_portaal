from django_tables2 import tables, TemplateColumn
from django_tables2.utils import Accessor
from .models import ProjectTaak


class ProjecttakenTable(tables.Table):

   class Meta:
      model = ProjectTaak
      template_name = "django_tables2/bootstrap-responsive.html"
      fields = ('nummer','omschrijving','status')

   #details = TemplateColumn(template_name='claus_administratie/button_tabel_details.html')

   bewerk = TemplateColumn(template_name='claus_projecttaken/button_tabel_wijzig.html')
