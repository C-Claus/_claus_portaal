from django.urls import include, path 
from . import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns =   [
                    
                    path("aanwezigheid_list", views.aanwezigheid_list, name="aanwezigheid_list"),                                                              
                    path("aanwezigheid/<int:pk>/", views.AanwezigheidUpdate.as_view(), name="aanwezigheid_update"),
                    path('aanwezigheid/<int:persoon>', views.aanwezigheid, name="aanwezigheid"),
                    path('aanwezigheids_overzicht/<str:persoon_guid>/<int:jaar>/<int:maand>/<int:dag>', views.aanwezigheids_overzicht, name="aanwezigheids_overzicht"),
                    path('aanwezigheids_overzicht_per_dag', views.aanwezigheid_dagoverzicht, name="aanwezigheid_dagoverzicht"),
        
                    
                    ]