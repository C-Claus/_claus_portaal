from django.shortcuts import render
import datetime 
from datetime import date

from claus_personen.models import Personen

from django import template
register = template.Library() 

def index(response): 

    persoon_groep = response.user.groups.all()[0]

  
    return render(response, "claus_portaal/base.html",{ "persoon_groep":persoon_groep})
                                                        

def claus_portaal(response):

    persoon_groep = response.user.groups.all()[0]
    persoon_id = Personen.objects.filter(account_id=response.user.id).values_list('id', flat=True)[0]


    account_id = response.user.id
    persoon_ingelogd = Personen.objects.get(account=account_id)
    persoon_guid = persoon_ingelogd.persoon_guid


    nu = datetime.datetime.now()
    huidig_jaar = nu.year
    huidige_dag = nu.day
    huidige_week = datetime.date(nu.year, nu.month, nu.day).isocalendar()[1]


    return render(response, "claus_portaal/claus_portaal.html", {   "persoon_id":int(persoon_id),
                                                                    "persoon_guid":persoon_guid,
                                                                    "jaar":huidig_jaar,
                                                                    "week":huidige_week,
                                                                    
                                                                    })