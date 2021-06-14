from django.shortcuts import render
import datetime 
from datetime import date

from claus_personen.models import Personen
from claus_administratie.models import BedrijfsAdministratie
from django.urls import reverse
from django.http import HttpResponseRedirect

from django import template
register = template.Library() 

def index(response): 

    #persoon_groep = response.user.groups.all()[0]

    #url = 'login'

    url = reverse('login')
    return HttpResponseRedirect(url)

  
    return render(response, "claus_portaal/base.html")




                                                        

def claus_portaal(response):


    persoon_groep = response.user.groups.all()
    persoon_id = Personen.objects.filter(account_id=response.user.id).values_list('id', flat=True)[0]

    persoon_ingelogd = Personen.objects.get(account=response.user.id)
    persoon_guid = persoon_ingelogd.persoon_guid
    persoon_administratie = persoon_ingelogd.administratie_werkgever


    nu = datetime.datetime.now()
    huidig_jaar = nu.year
    huidige_dag = nu.day
    huidige_week = datetime.date(nu.year, nu.month, nu.day).isocalendar()[1]


    return render(response, "claus_portaal/claus_portaal.html", {   "persoon_id":int(persoon_id),
                                                                    "persoon_guid":persoon_guid,
                                                                    "jaar":huidig_jaar,
                                                                    "week":huidige_week,
                                                                    "persoon_administratie":persoon_administratie
                                                                    
                                                                    })