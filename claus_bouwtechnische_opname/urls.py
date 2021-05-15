from django.urls import include, path 
from . import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns =   [
                    
                 
                    path('claus_bouwtechnische_opname', views.claus_bouwtechnische_opname, name="claus_bouwtechnische_opname"),
                    path('formulier_maken', views.formulier_maken, name='formulier_maken'),
                    
                    ]