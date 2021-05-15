from django.urls import include, path 
from . import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns =   [
                    
                 
                    path('claus_planning', views.claus_planning, name='claus_planning'),
                    path('planning_persoon_selecteer_dag', views.planning_persoon_selecteer_dag, name='planning_persoon_selecteer_dag'),
                    path("planning_persoon/<int:persoon>/<int:jaar>/<int:maand>/<int:dag>", views.planning_persoon, name="planning_persoon"),
                
                   
                    
                    ]