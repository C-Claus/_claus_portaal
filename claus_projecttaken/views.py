from django.shortcuts import render
from .models import ProjectTaak
from .tables import ProjecttakenTable

from django.views.generic import (  View,
                                    ListView,
                                    DetailView, 
                                    CreateView,
                                    UpdateView,
                                    DeleteView
                                    )


def projecttaak(response):


    return render(response, 'claus_projecttaken/claus_projecttaken.html')



class ProjecttaakCreate(CreateView):

    model = ProjectTaak
    
    fields = (  'nummer',
                'omschrijving',
                'status',
                )

    template_name = 'claus_projecttaken/projecttaak_maken.html'

    success_url = '/projecttaak_list'



class ProjecttaakUpdate(UpdateView):
    model = ProjectTaak

    fields = (  'nummer',
                'omschrijving',
                'status',
                )
   
    template_name = 'claus_projecttaken/projecttaak_update.html' 
    
    success_url = '/projecttaak_list'  


class ProjecttaakDetails(DetailView):

    template_name = 'claus_projecttaken/projecttaak_details.html' 

    model = ProjectTaak


def projecttaak_list(response):
 
    table = ProjecttakenTable(ProjectTaak.objects.all())

    return render(response, 'claus_projecttaken/projecttaak_list.html', { 'table':table})

def projecttaak_beheer(response):
 
   
    return render(response, 'claus_projecttaken/projecttaak_beheer.html')

