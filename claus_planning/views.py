from django.shortcuts import render
import datetime

from claus_personen.models import Personen
from claus_projecten.models import Projecten
from claus_projecttaken.models import ProjectTaak
from claus_planning.models import Planning


from .forms import *



def claus_planning(response):

    return render(response, 'claus_planning/claus_planning.html')


def planning_persoon(response, persoon, jaar, maand, dag):


    datum = datetime.date(jaar, maand, dag)
    persoon = Personen.objects.get(id=persoon)
    planning = Planning.objects.all() #filter(datum=datum)

     
    planning_form = PlanningForm()
    planning_form = PlanningForm(initial={'persoon': persoon,  'status':'Actief'})
    planning_form.fields['datum'].initial = (str(jaar)+"-"+str(maand)+"-"+str(dag))
    planning_form.fields['persoon'].widget = forms.HiddenInput()
    planning_form.fields['status'].widget = forms.HiddenInput()
    planning_form.fields['datum'].widget = forms.HiddenInput()

 
   
    if response.method == 'POST': 

        if 'save' in response.POST:
            print ('knop + is geklikt')
      
            #if planning_form.is_valid():
           
            planning_form = PlanningForm(response.POST)
            planning_form.save()

            #https://docs.djangoproject.com/en/3.1/ref/forms/api/#django.forms.Form.cleaned_data
            cleaned_data = planning_form.cleaned_data

            planning_form = PlanningForm(initial={'persoon': persoon,  'status':'Actief'})
            planning_form.fields['datum'].initial = (str(jaar)+"-"+str(maand)+"-"+str(dag))

            planning_form.fields['persoon'].widget = forms.HiddenInput()
            planning_form.fields['status'].widget = forms.HiddenInput()
            planning_form.fields['datum'].widget = forms.HiddenInput()
               
        if 'delete' in response.POST:     
            print ('knop - is geklikt')  

        if 'edit' in response.POST:
            print ('knop wijzig is geklikt')

  
 
    

    return render(response, "claus_planning/planning_persoon.html", {   "planning":planning,
                                                                        "planning_form":planning_form,
                                                                        "persoon":persoon,
                                                                        "jaar":jaar,
                                                                        "maand":maand,
                                                                        "dag":dag,
                                                                
                                                                  })  


def planning_persoon_selecteer_dag(response):

    if response.POST:
        print ('response.POST',(response.POST))
        
        if response.POST.get('datum'):
            print (response.POST.get('datum'))


    return render(response, 'claus_planning/planning_persoon_selecteer_dag.html')  
