from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.db.models import Q, Sum, Max, Count
from django.db.models.functions import Extract

#backlog
# definieer ingelogd gebruiker adhv guid
# laat gebruik eerst dag en week registren
# geef mogelijkheid tussen dag en weekregistratie
# gebruikerregistratie

# totaal aantal uren per week
# totaal aantal uren per dag

# laat gebruiker projecten voor de bv waar hij werkzaam voor is  dmv zoekvenster
# geef projecten weer via zoekvenster
# niet gewerkte uren kunnen boeken

# geef actieve kostencodes zien op bv waar hij werkzaam voor is
# geef actieve projecttaken weer op bv waar hij werkzaam voor is

# totaal aantal uren in card header 
# bevestig week knop waarbij status gaat naar bevestigd    
# zorg ervoor dat er door week geklikt kan worden, ook bij wisseling jaar moet dit goed gaan

# profielgegevens weergeven

# kijk bij binnenkomst of uren ingevoerd of bevestigd zijn voor die week
# laat zien in weekselectie welke bevestigd en ingevoerd zijn, grijs bevestigde weken uit
import time
import datetime 
from datetime import date




from .models import Personen, Projecten, UrenRegistratie
from .forms import RegistratieUrenForm
from django import forms

from django.views.generic import (  
                                    View,
                                    ListView,
                                    DetailView, 
                                    CreateView,
                                    UpdateView,
                                    DeleteView
                                    )


from claus_uren.models import UrenRegistratie

from .tables import UrenRegistratieTable, UrenRegistratieTableBevestigd


import locale


locale.setlocale(locale.LC_TIME, "nl_NL") 




def registreer_vandaag(response, persoon_guid, jaar, week):



    dagen_van_de_week_list = []
    week_nummer_list = []
    week_nummer_list_selectie = []
    weeknummer_jaar_list = []
    datum_list = []
    datum_weeknummer_dict = {}
 
    account_id = response.user.id
    persoon_ingelogd = Personen.objects.get(account=account_id)
    persoon_guid = persoon_ingelogd.persoon_guid

    for dag in range(1,8):
        dagen_van_de_week_list.append([date.fromisocalendar(jaar, week, dag), date.fromisocalendar(jaar, week, dag).strftime("%A")])


    for weeknummer in range(1, (datetime.date(jaar, 12, 31).isocalendar()[1])+1):
        week_nummer_list_selectie.append([jaar,weeknummer])


    week_nummer_list = week_nummer_list_selectie[week-4:week]
    week_nummer_vorig = week_nummer_list_selectie[week-2:week-1]
    week_nummer_volgend = week_nummer_list_selectie[week:week+1]


    nu = datetime.datetime.now()
    huidig_weeknummer = datetime.date(nu.year, nu.month, nu.day).isocalendar()[1]
    #constructeer list datum week 
    #haal query op per week en persoon
    #spiegel deze query aan weeknummers
    #kijk of ze ingevoerd of bevestigd zijn
    #zijn ze bevestigds link ze naar week bevestigd method
    #zijn ze ingevoerd laat open staan voor bewerking
    #zijn ze goedgekeurd link naar ntb method

    #.filter(model__date__week=datetime.date.today().isocalendar()[1])

    

    urenregistratie_persoon = UrenRegistratie.objects.filter(persoonnr=persoon_ingelogd)
    urenregistratie_per_week = urenregistratie_persoon
 

 

    for jaar_, week_nummer in week_nummer_list:
       
        for dag in range(1,8):
            datum = date.fromisocalendar(jaar_, week_nummer, dag)
            datum_list.append(datum)
            
        
        datum_weeknummer_dict[ str(jaar_) + "-" + str(week_nummer)] = datum_list
        #print (week_nummer)
        break

        


    
    #for k,v in datum_weeknummer_dict.items():
    #    print (k, v)
        
  

            
    #data_per_week = ["2021-04-05", "2021-04-06"]

    #urenregistratie_per_week = urenregistratie_persoon.filter(datum__range=data_per_week)
    

   


 
    return render(response, 'claus_uren/registreer_vandaag.html', {     "persoon_ingelogd":persoon_ingelogd,
                                                                      
                                                                        "huidig_weeknummer":huidig_weeknummer,
                                                                        "week_nummer_list":week_nummer_list,
                                                                        "huidig_jaar":jaar,
                                                                        "persoon_guid":persoon_guid,
                                                                        "week_nummer_vorig":week_nummer_vorig,
                                                                        "week_nummer_volgend":week_nummer_volgend,
                                                                      
                                                                                                                                                 
                                                                    })


def registreer_week(response, persoon_guid, jaar, week):


    uren_status_list = []
    uren_status = 'hoi'

    dagen_van_de_week_list = []
    dagen_week_query_list = []
    week_nummer_list = []
    week_dag_dict = {}
    

    account_id = response.user.id
    persoon_ingelogd = Personen.objects.get(account=account_id)
    persoon_guid = persoon_ingelogd.persoon_guid
    persoon_pk = persoon_ingelogd.id


    nu = datetime.datetime.now()
    huidig_jaar = nu.year
    huidige_week = week


    for dag in range(1,8):
        dagen_van_de_week_list.append([date.fromisocalendar(jaar, week, dag), date.fromisocalendar(jaar, week, dag).strftime("%A")])
        dagen_week_query_list.append(date.fromisocalendar(jaar, week, dag))

    for week_nummer in range(week-1, week+2):
        week_nummer_list.append(week_nummer)


    uren_registratie_persoon = UrenRegistratie.objects.filter(persoonnr=persoon_pk)

    for dag in dagen_week_query_list:
        

        uren_registratie_dag = uren_registratie_persoon.filter(datum=dag)
        uren_registratie_dag_persoon = uren_registratie_dag.values('persoonnr').order_by('persoonnr')
        uren_registratie_dag_totaal = uren_registratie_dag_persoon.annotate(aantal_uren=Sum('aantal_uur'))
   
        week_dag_dict[dag] = [UrenRegistratieTable(uren_registratie_persoon.filter(datum=dag)), uren_registratie_dag_totaal]

 


    if response.method == 'POST':
        for dag in dagen_week_query_list:   
            for uren in uren_registratie_persoon.filter(datum=dag):

                #if uren.registratie_status != 'Bevestigd':

                uren.registratie_status = 'Bevestigd'
                uren.save()

            
                #redirect naar andere view registree_week_bevestigf
                url = reverse('registreer_week_bevestigd', kwargs={ 'persoon_guid':persoon_guid, 'jaar': jaar, 'week':week})
                return HttpResponseRedirect(url)

             



    return render(response, 'claus_uren/registreer_week.html', { "persoon_ingelogd":persoon_ingelogd,
                                                                "dagen_van_de_week_list":dagen_van_de_week_list,
                                                                "week_nummer_list":week_nummer_list,
                                                                "week":week,
                                                                "persoon_guid":persoon_guid,
                                                                "week_dag_dict":week_dag_dict,
                                                                "uren_status":uren_status,
                                                                })  

def registreer_week_bevestigd(response, persoon_guid, jaar, week ):

    uren_status_list = []

    dagen_van_de_week_list = []
    dagen_week_query_list = []
    week_nummer_list = []
    week_dag_dict = {}
    

    account_id = response.user.id
    persoon_ingelogd = Personen.objects.get(account=account_id)
    persoon_guid = persoon_ingelogd.persoon_guid
    persoon_pk = persoon_ingelogd.id


    nu = datetime.datetime.now()
    huidig_jaar = nu.year
    huidige_week = week


    for dag in range(1,8):
        dagen_van_de_week_list.append([date.fromisocalendar(jaar, week, dag), date.fromisocalendar(jaar, week, dag).strftime("%A")])
        dagen_week_query_list.append(date.fromisocalendar(jaar, week, dag))

    for week_nummer in range(week-1, week+2):
        week_nummer_list.append(week_nummer)


    uren_registratie_persoon = UrenRegistratie.objects.filter(persoonnr=persoon_pk)

    for dag in dagen_week_query_list:
        

        uren_registratie_dag = uren_registratie_persoon.filter(datum=dag)
        uren_registratie_dag_persoon = uren_registratie_dag.values('persoonnr').order_by('persoonnr')
        uren_registratie_dag_totaal = uren_registratie_dag_persoon.annotate(aantal_uren=Sum('aantal_uur'))
   
        week_dag_dict[dag] = [UrenRegistratieTableBevestigd(uren_registratie_persoon.filter(datum=dag)), uren_registratie_dag_totaal]

    return render(response, 'claus_uren/registreer_week_bevestigd.html',  {"persoon_ingelogd":persoon_ingelogd,
                                                                            "dagen_van_de_week_list":dagen_van_de_week_list,
                                                                            "week_nummer_list":week_nummer_list,
                                                                            "week":week,
                                                                            "persoon_guid":persoon_guid,
                                                                            "week_dag_dict":week_dag_dict,})

def registreer_dag(response, persoon_guid, jaar, maand, dag):

    account_id = response.user.id
    persoon_ingelogd = Personen.objects.get(account=account_id)
    persoon_guid = persoon_ingelogd.persoon_guid
    persoon_administratie = persoon_ingelogd.administratie_werkgever

    week_nummer = datetime.date(jaar, maand, dag).isocalendar()[1]






    #initialisatie waarden voor het form 
    persoon_pk = persoon_ingelogd.id
    persoon_bedrijf = persoon_ingelogd.administratie_werkgever
    datum = datetime.date(jaar, maand, dag)

    #Form
    registratie_uren_form = RegistratieUrenForm()

    #Form waarden geinitialiseerd
    registratie_uren_form.fields['persoonnr'].initial = persoon_pk
    registratie_uren_form.fields['bedrijfsadministratie'].initial = persoon_bedrijf
    registratie_uren_form.fields['datum'].initial = datum
    registratie_uren_form.fields['registratie_status'].initial = "Ingevoerd"
    registratie_uren_form.fields['ingevoerd_door'].initial = persoon_pk

    #Form waarden verborgen 
    registratie_uren_form.fields['persoonnr'].widget = forms.HiddenInput()
    registratie_uren_form.fields['bedrijfsadministratie'].widget = forms.HiddenInput()
    registratie_uren_form.fields['datum'].widget = forms.HiddenInput()
    registratie_uren_form.fields['registratie_status'].widget = forms.HiddenInput()
    registratie_uren_form.fields['ingevoerd_door'].widget = forms.HiddenInput()

    registratie_uren_form.fields['geaccordeerd_door'].widget = forms.HiddenInput()




    if response.method == 'POST': 
        registratie_uren_form = RegistratieUrenForm(response.POST)  

        #Form waarden geinitialiseerd
        registratie_uren_form.fields['persoonnr'].initial = persoon_pk
        registratie_uren_form.fields['bedrijfsadministratie'].initial = persoon_bedrijf
        registratie_uren_form.fields['datum'].initial = datum
        registratie_uren_form.fields['registratie_status'].initial = "Ingevoerd"
        registratie_uren_form.fields['ingevoerd_door'].initial = persoon_pk

        #Form waarden verborgen 
        registratie_uren_form.fields['persoonnr'].widget = forms.HiddenInput()
        registratie_uren_form.fields['bedrijfsadministratie'].widget = forms.HiddenInput()
        registratie_uren_form.fields['datum'].widget = forms.HiddenInput()
        registratie_uren_form.fields['registratie_status'].widget = forms.HiddenInput()
        registratie_uren_form.fields['ingevoerd_door'].widget = forms.HiddenInput()

        registratie_uren_form.fields['geaccordeerd_door'].widget = forms.HiddenInput()

        if response.POST.get('registreer_uren'):
            registratie_uren_form.save()
            url = reverse('registreer_week', kwargs={ 'persoon_guid':persoon_guid, 'jaar': jaar, 'week':week_nummer})
            return HttpResponseRedirect(url)




    #registratie_uren_form.fields['persoonnr'].widget = forms.HiddenInput()

    







    return render(response, "claus_uren/registreer_dag.html", { "persoon_ingelogd":persoon_ingelogd,
                                                                "jaar":jaar,
                                                                "maand":maand,
                                                                "dag":dag,
                                                                "registratie_uren_form":registratie_uren_form,
                                                                
                                                            
                                                            })


class UrenWijzigen(UpdateView):

    model = UrenRegistratie

    fields = (  'projectnr',
                'projecttaaknummer',
                'kostencode',
                #'datum',
                'aantal_uur',
                'opmerking',
                )

    template_name = 'claus_uren/registreer_wijzig.html'
    succes_url = 'claus_uren/registreer_week/<str:persoon_guid>/<int:jaar>/<int:week>'


    def get_success_url(self):

        if 'pk' in self.kwargs:
            pk = self.kwargs['pk']

        registratie = UrenRegistratie.objects.get(id=pk)
        persoon = Personen.objects.get(id=registratie.persoonnr_id)
        weeknummer = datetime.date(registratie.datum.year, registratie.datum.month, registratie.datum.day).isocalendar()[1]


        url = reverse('registreer_week', kwargs={'persoon_guid':persoon.persoon_guid, 'jaar':registratie.datum.year, 'week':weeknummer})

        return url                                                           

class UrenVerwijderen(DeleteView):

    model = UrenRegistratie 
    template_name = 'claus_uren/registreer_verwijderen.html'
    succes_url = 'claus_uren/registreer_week/<str:persoon_guid>/<int:jaar>/<int:week>'


    def get_success_url(self):

        if 'pk' in self.kwargs:
            pk = self.kwargs['pk']

        registratie = UrenRegistratie.objects.get(id=pk)
        persoon = Personen.objects.get(id=registratie.persoonnr_id)
        weeknummer = datetime.date(registratie.datum.year, registratie.datum.month, registratie.datum.day).isocalendar()[1]


        url = reverse('registreer_week', kwargs={'persoon_guid':persoon.persoon_guid, 'jaar':registratie.datum.year, 'week':weeknummer})

        return url


     