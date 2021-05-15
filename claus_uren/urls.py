from django.urls import include, path 
from . import views
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns =   [ 
                path('registreer_vandaag/<str:persoon_guid>/<int:jaar>/<int:week>', views.registreer_vandaag,  name='registreer_vandaag' ),
                path('registreer_week/<str:persoon_guid>/<int:jaar>/<int:week>', views.registreer_week, name='registreer_week'),
                path('registreer_week_bevestigd/<str:persoon_guid>/<int:jaar>/<int:week>', views.registreer_week_bevestigd, name='registreer_week_bevestigd'),
                path('registreer_dag/<str:persoon_guid>/<int:jaar>/<int:maand>/<int:dag>', views.registreer_dag, name='registreer_dag'),

                path("registreer_wijzig/<int:pk>/", views.UrenWijzigen.as_view(), name="registreer_wijzig"),
                path('registreer_verwijderen/<int:pk>', views.UrenVerwijderen.as_view(), name="uren_verwijderen")

                ]
