from django.shortcuts import render
from .models import Personen
from .tables import PersonenTable
from django import forms
import uuid


from django.contrib.auth.models import User,  Group, Permission
#from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test

from .decorators import allowed_users

#decorators = [allowed_users]


#print (uuid.uuid4().hex)

# persoon_guid moet automatisch gevuld worden
# e-mail moet verstuurd worden naar e-mail adres
# daarna kan persoon zelf persoonsgegevens invullen
# gebruikersgroepen inrichten, gebruikersgroepen kunnen levels of voorgedefinieerd zijn
# van 10 naar 100 , 100 = ict, 90 = administratie, 80 = vestigingleider, 70 = teamleider, 60 = uitvoerend
# persoonggegevens
# gebruikersgroep administratie taakbalk,

# administratie mag uitvoerend zien
# uitvoerend kan administratie niet zien


from django.views.generic import (  View,
                                    ListView,
                                    DetailView, 
                                    CreateView,
                                    UpdateView,
                                    DeleteView
                                    )





def persoon(response):


    return render(response, 'claus_persoon/claus_persoon.html')


def persoon_gegevens(response):

    gebruikersgroep_list  = []

    administratie = 'Administratie'
    uitvoerend = 'Uitvoerend'


    if response.user.groups.filter(name=administratie).exists():
        gebruikersgroep_list.append(administratie)    

    if response.user.groups.filter(name=uitvoerend).exists():
        gebruikersgroep_list.append(uitvoerend)  

    else:
        gebruikersgroep_list.append('Niet in bestaande gebruikersgroep')   


    return render(response, 'claus_persoon/claus_persoon_gegevens.html', {'gebruikersgroep_list':gebruikersgroep_list[0] })

@login_required
@allowed_users(allowed_roles=['Administratie'])
def persoon_account(response):

    return render(response, 'claus_persoon/claus_persoon_account.html')



#@method_decorator(decorators, name='dispatch')
class PersoonCreate(CreateView):

    model = Personen
    
    fields = (    'persoonnr',
                  'naam', 
                  'in_dienst_status',
                  'administratie_werkgever',
                  'gebruikersgroep',
                  'account',
                  'persoon_guid',
               )
              
               

    template_name = 'claus_persoon/persoon_maken.html'

    success_url = '/persoon_list'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.request = self.request

        form.fields['persoon_guid'].initial = uuid.uuid4().hex
        form.fields['persoon_guid'].widget = forms.HiddenInput()

  
        return form


#@method_decorator(decorators, name='dispatch')
class PersoonUpdate(UpdateView):
    model = Personen

    fields = (   'persoonnr',
                  'naam', 
                  'in_dienst_status',
                  'administratie_werkgever',
                  'gebruikersgroep',
                  'account',
               )
         
   
    template_name = 'claus_persoon/persoon_update.html'

    success_url = '/persoon_list'


class PersoonDetails(DetailView):

    model = Personen

    fields = (   'persoonnr',
                  'naam', 
                  'in_dienst_status',
                  'administratie_werkgever',
                  'gebruikersgroep',
                  'account',
               )

    template_name = 'claus_persoon/persoon_details.html' 




@login_required
@allowed_users(allowed_roles=['Administratie'])
def persoon_list(response):

    group_user_ingelogd = response.user.groups.all()[0]


    table = PersonenTable(Personen.objects.all())
    #table = PersonenTable(Personen.objects.filter(gebruikersgroep=group_user_ingelogd))
 
    return render(response, 'claus_persoon/persoon_list.html', { 'table':table })    