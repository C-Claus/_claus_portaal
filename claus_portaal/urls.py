from django.urls import include, path 
from . import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns =   [
                    
                    path('', views.index, name='index'),
                    path('claus_portaal', views.claus_portaal, name="claus_portaal"),
                  
                    
                    ]