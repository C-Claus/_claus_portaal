from claus_aanwezigheids_assistent.models import Aanwezigheid
from django_tables2 import tables, TemplateColumn
import django_tables2 as tables


class AfwezigheidTable(tables.Table):

   class Meta:
      model = Aanwezigheid
      template_name = "django_tables2/bootstrap-responsive.html"
      fields = ('datum', 'begintijd', 'eindtijd')

   bewerk = TemplateColumn(template_name='aanwezigheid/aanwezigheid_edit.html')   


