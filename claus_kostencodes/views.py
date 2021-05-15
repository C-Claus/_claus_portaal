from django.shortcuts import render

def kostencodes(response):

    return render(response, 'claus_kostencodes/kostencodes.html')

from django.shortcuts import render
from .models import KostenCode
from .tables import KostenCodeTable

from django.views.generic import (  View,
                                    ListView,
                                    DetailView, 
                                    CreateView,
                                    UpdateView,
                                    DeleteView
                                    )


#def projecttaak(response):


#    return render(response, 'claus_projecttaken/claus_projecttaken.html')



class KostenCodeCreate(CreateView):

    model = KostenCode
    
    fields = (  'nummer',
                'omschrijving',
                'status',
                'bedrijfsadministratie',
                )

    template_name = 'claus_kostencodes/kostencodes_maken.html'

    success_url = '/kostencodes_list'



class KostenCodeUpdate(UpdateView):
    model = KostenCode

    fields = (  'nummer',
                'omschrijving',
                'status',
                'bedrijfsadministratie',
                )
   
    template_name = 'claus_kostencodes/kostencodes_update.html' 
    
    success_url = '/kostencodes_list'  


class KostenCodeDetails(DetailView):

    template_name = 'claus_kostencodes/kostencode_details.html' 

    model = KostenCode


def kostencodes_list(response):
 
    table = KostenCodeTable(KostenCode.objects.all())

    return render(response, 'claus_kostencodes/kostencodes_list.html', { 'table':table})


def kostencodes_beheer(response):
 
   
    return render(response, 'claus_kostencodes/kostencodes_beheer.html')

