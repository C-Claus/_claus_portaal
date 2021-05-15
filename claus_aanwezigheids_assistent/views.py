from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy 
from django.views.generic import UpdateView
from django.http import  HttpResponseRedirect                                  

import datetime 
from datetime import timedelta, date
from datetime import datetime as date_time

from collections import defaultdict
from collections import OrderedDict

from claus_personen.models import Personen
from claus_aanwezigheids_assistent.models import Aanwezigheid

from .forms import *
from .tables import *


import uuid
import itertools

#print (uuid.uuid4().hex)

#persoon_guid van coen
#a309a3867f684506a75243edea5b3492

def aanwezigheid(response, persoon):

    #print (uuid.uuid4().hex)

    persoon = Personen.objects.get(id=persoon)
    persoon_id = Personen.objects.filter(account_id=response.user.id).values_list('id', flat=True)[0]
    persoon_guid = persoon.persoon_guid

    aanwezigheid_form = AanwezigheidsForm(initial={'persoon': persoon,  'status':'Actief'})

    aanwezigheid_form.fields['status'].widget = forms.HiddenInput()
    aanwezigheid_form.fields['persoon'].widget = forms.HiddenInput()

    if response.method == 'POST':
        
        if 'save' in response.POST:
            aanwezigheid_form = AanwezigheidsForm(response.POST)
            aanwezigheid_form.save()

            #https://docs.djangoproject.com/en/3.1/ref/forms/api/#django.forms.Form.cleaned_data
            cleaned_data = aanwezigheid_form.cleaned_data
            aanwezigheid_datum =  Aanwezigheid()
            aanwezigheid_datum.datum = cleaned_data['datum']

            jaar = aanwezigheid_datum.datum.year
            maand = aanwezigheid_datum.datum.month
            dag = aanwezigheid_datum.datum.day

            url = reverse('aanwezigheids_overzicht', kwargs={ 'persoon_guid': persoon_guid,  'jaar': jaar, 'maand':maand, 'dag':dag })
            
            return HttpResponseRedirect(url)
            

    return render(response, "aanwezigheid/aanwezigheid.html", {"aanwezigheid_form":aanwezigheid_form,
                                                               "persoon":persoon}
                                                               )

def aanwezigheid_list(response):

    persoon_id_ingelogd = Personen.objects.filter(account_id=response.user.id).values_list('id', flat=True)[0]
    persoon = Personen.objects.get(id=persoon_id_ingelogd)
 
    table = AfwezigheidTable(Aanwezigheid.objects.filter(persoon=persoon))


   

    dag_list = Aanwezigheid.objects.filter(persoon_id=persoon_id_ingelogd)

    return render(response, 'aanwezigheid/aanwezigheid_list.html', { 'table':table,
                                                                      'persoon':persoon,
                                                                      'persoon_id':persoon_id_ingelogd,
                                                                      'dag_list':dag_list,
                                                                      })
 
class AanwezigheidUpdate(UpdateView):

    model = Aanwezigheid
    fields = ('datum','begintijd','eindtijd', 'status')
    template_name = 'aanwezigheid/aanwezigheid_update.html' 



    def get_context_data(self, **kwargs):
        context = super(AanwezigheidUpdate, self).get_context_data(**kwargs)
       
        context['datum'] = self.get_object().datum 


        #print (context)
        return context



    def get_success_url(self):

       
        #print ('datum uit succes url')

        #url = reverse('aanwezigheids_overzicht', kwargs={ 'persoon_guid': persoon_guid,  'jaar': jaar, 'maand':maand, 'dag':dag })
            
        #return HttpResponseRedirect(url)


        return reverse('aanwezigheid_list')       


def aanwezigheids_overzicht(response, persoon_guid, jaar, maand, dag):


    ################################################################################
    ### 0 kijk welke gebruiker afwezigheid registreert en initaliseer variabelen ###
    ################################################################################
    vandaag  = datetime.datetime(jaar, maand, dag)

    
    persoon_id_ingelogd = Personen.objects.filter(account_id=response.user.id).values_list('id', flat=True)[0]
    persoon = Personen.objects.get(id=persoon_id_ingelogd)

    persoon_guid = persoon.persoon_guid

    #print ('guid van coen', persoon_guid)

   

    afwezigheid = Aanwezigheid.objects.all()
    afwezigheid_per_dag = Aanwezigheid.objects.filter(datum=datetime.date(jaar, maand, dag))
   
    persoon_dag_query  = Aanwezigheid.objects.filter(persoon=persoon).filter(datum=datetime.date(jaar, maand, dag))
    table_persoon_dag = AfwezigheidTable(persoon_dag_query)

    
    ######################################################################
    ### 1 defineer een verzameling (dictionary) van tijddeltas per key ###
    ######################################################################
    
    #initaliseer lists en dictionaries
    persoon_ingelogd_minuten_delta_list  = []
    persoon_overige_minuten_delta_list  = []
    persoon_naam_overige_minuten_delta_list = []
    persoon_ingelogd_dict = {}
    persoon_overige_dict = {}


    for i in afwezigheid_per_dag:

        #maak een list van minuten
        start = date_time.combine(vandaag, i.begintijd)
        seconds = (date_time.combine(vandaag, i.eindtijd) - date_time.combine(vandaag, i.begintijd)).total_seconds()
        step = timedelta(minutes=1)
        
        #controleer wie is ingelogd
        if str(Personen.objects.filter(account_id=response.user.id)[0]) == str(i.persoon):   

            for j in range(0, int(seconds)+60, int(step.total_seconds())):
                #maak minuten list van ingelogd persoon
                persoon_ingelogd_minuten_delta_list.append( start + (timedelta(seconds=j)))
                persoon_ingelogd_dict[i.persoon.naam] = persoon_ingelogd_minuten_delta_list

        else:

            for k in range(0, int(seconds)+60, int(step.total_seconds())):
                #maak list van persoon per naam
                persoon_naam_overige_minuten_delta_list.append([i.persoon, start + (timedelta(seconds=k))])
                
                #maak een dictionary met een totale list om te spiegelen later aan het ingelogd persoon
                persoon_overige_minuten_delta_list.append(start + (timedelta(seconds=k)))
                persoon_overige_dict['Overige'] = persoon_overige_minuten_delta_list




    #####################################
    ### 2. vind duplicates in de list ###
    #####################################

    #combineer de list van ingelogd persoon en overige persoon, met set haal alle identieke waardes eruit
    overlap_list = sorted(set(persoon_ingelogd_minuten_delta_list) & set(persoon_overige_minuten_delta_list))

 
    overlap_per_naam_list = []

    #met de list van persoon per naam kan per minuut worden gekeken welke persoon afwezig is op die minuut
    for j in overlap_list:
        for i in persoon_naam_overige_minuten_delta_list:
            if i[1] == j:
                overlap_per_naam_list.append( [i[0], [j]])

   
    #zet de list van lists om naar een dictionary met defaultdict, defaultdict kan een dynamische key bevatten ipv dict
    overlap_dict = defaultdict(list)

    for naam, minuten in overlap_per_naam_list:
        overlap_dict[naam].append(minuten)

    overlap_persoon_minuut_list = overlap_dict.items()   


    #fatsoeneer de lijst om mooi te renderen in HTML
    render_persoon_minuut_list = []
    for i in overlap_persoon_minuut_list:
        render_persoon_minuut_list.append([i[0], i[1][0], i[1][-1]])   

   
   
  
 
 

    return render(response, "aanwezigheid/aanwezigheids_overzicht.html", {"persoon":persoon,
                                                                          "jaar":jaar,
                                                                          "maand":maand,
                                                                          "dag":dag,
                                                                          "table_persoon_dag":table_persoon_dag,
                                                                          
                                                                          
                                                                          "afwezigheid_per_dag":afwezigheid_per_dag,
                                                                          "overlap_per_naam_list":overlap_per_naam_list,
                                                                          "render_persoon_minuut_list":render_persoon_minuut_list,
                                                                          
                                                                          })      

def aanwezigheid_dagoverzicht(response):

    persoon_id_ingelogd = Personen.objects.filter(account_id=response.user.id).values_list('id', flat=True)[0]
    persoon = Personen.objects.get(id=persoon_id_ingelogd)

    persoon_guid = persoon.persoon_guid

    afwezigheid_list = Aanwezigheid.objects.filter(persoon_id=persoon_id_ingelogd)


    datum_keuze_list = []
    for i in afwezigheid_list:
        datum_keuze_list.append([i.datum.year, i.datum.month, i.datum.day])


    #print (datum_keuze_list.sort())

    gesorteerde_datum_list = list(datum_keuze_list for datum_keuze_list,_ in itertools.groupby(datum_keuze_list))

    #print (gesorteerde_datum_list)

    #persoon_id_ingelogd = Personen.objects.filter(account_id=response.user.id).values_list('id', flat=True)[0]
    #persoon = Personen.objects.get(id=persoon_id_ingelogd)

    #persoon_guid = persoon.persoon_guid

    #print ('guid van coen', persoon_guid)



   

    

    return render(response, "aanwezigheid/aanwezigheid_overzicht_per_dag.html", { "persoon_id":persoon_id_ingelogd,
                                                                                    "persoon_guid":persoon_guid,
                                                                                   "persoon":persoon,
                                                                                   "afwezigheid_list":set(afwezigheid_list),
                                                                                   "gesorteerde_datum_list":gesorteerde_datum_list,
                                                                                
                                                                                })                                                                                                                                  