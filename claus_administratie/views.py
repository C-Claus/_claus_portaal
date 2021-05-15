from django.shortcuts import render
from .models import BedrijfsAdministratie
from .tables import AdministratieTable

from django.views.generic import (  View,
                                    ListView,
                                    DetailView, 
                                    CreateView,
                                    UpdateView,
                                    DeleteView
                                    )

def administratie(response):


    return render(response, 'claus_administratie/claus_administratie.html')



class AdministratieCreate(CreateView):

    model = BedrijfsAdministratie
    
    fields = (  'bedrijfsnummer',
                'bedrijfsnaam', 
                'omschrijving',
                'kvk_nummer',
                'vestigings_nummer',
                'straatnaam_nummer',
                'postcode',
                'plaats',
                'status')

    template_name = 'claus_administratie/administratie_maken.html'

    success_url = '/administratie_list'



class AdministratieUpdate(UpdateView):
    model = BedrijfsAdministratie

    fields = (  'bedrijfsnummer',
                'bedrijfsnaam', 
                'omschrijving',
                'kvk_nummer',
                'vestigings_nummer',
                'straatnaam_nummer',
                'postcode',
                'plaats',
                'status')
   
    template_name = 'claus_administratie/administratie_update.html' 
    
    success_url = '/administratie_list'  


class AdministratieDetails(DetailView):

    template_name = 'claus_administratie/administratie_details.html' 

    model = BedrijfsAdministratie


def administratie_list(response):
 
    table = AdministratieTable(BedrijfsAdministratie.objects.all())

    return render(response, 'claus_administratie/administratie_list.html', { 'table':table})

def administratie_beheer(response):
 
   

    return render(response, 'claus_administratie/claus_administratie_beheer.html')
                                                                        

