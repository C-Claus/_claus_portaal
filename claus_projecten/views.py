from django.shortcuts import render
from .models import Projecten
from .tables import ProjectenTable

from django.views.generic import (  View,
                                    ListView,
                                    DetailView, 
                                    CreateView,
                                    UpdateView,
                                    DeleteView
                                    )


def project(response):


    return render(response, 'claus_projecten/claus_projecten.html')


class ProjectCreate(CreateView):

    model = Projecten
    
    fields = (  'projectnummer',
                'projectomschrijving', 
                'bedrijfsadministratie',
                'projectleider',
                'status',
                )
               

    template_name = 'claus_projecten/project_maken.html'

    success_url = '/project_list'



class ProjectUpdate(UpdateView):
    model = Projecten 

    fields = (  'projectnummer',
                'projectomschrijving', 
                'bedrijfsadministratie',
                'projectleider',
                'status',
    )
         
   
    template_name = 'claus_projecten/project_update.html' 
    
    success_url = '/project_list'  


class ProjectDetails(DetailView):

    template_name = 'claus_projecten/project_details.html' 

    model = Projecten


def project_list(response):
 
    table = ProjectenTable(Projecten.objects.all())

    return render(response, 'claus_projecten/project_list.html', { 'table':table })


def project_beheer(response):
 
   

    return render(response, 'claus_projecten/claus_project_beheer.html')
                                                                            