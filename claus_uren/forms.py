from django import forms 
from django.forms import ModelForm
from django.contrib.auth.models import User, Group

#from claus_administratie.models import BedrijfsAdministratie
#from claus_kostencodes.models import KostenCode
#from claus_personen.models import Personen
#from claus_projecten.models import Projecten
#from claus_projecttaken.models import ProjectTaak

from claus_uren.models import UrenRegistratie


class RegistratieUrenForm(ModelForm):

    aantal_uur = forms.FloatField(min_value=0.25, max_value=15.0)

    class Meta:
        model = UrenRegistratie 
        fields = [  'persoonnr',
                    'bedrijfsadministratie',
                    'projectnr',
                    'projecttaaknummer',
                    'kostencode',
                    'datum',
                    'aantal_uur',
                    'opmerking',
                    'registratie_status',
                    'ingevoerd_door',
                    'geaccordeerd_door',
                    ]

        #widgets = {'datum':DateInput()}    
