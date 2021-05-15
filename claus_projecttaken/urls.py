from django.urls import include, path 
from . import views
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns =   [
                    
                    
                    path('projecttaak', views.projecttaak,  name='projecttaak' ),
                    path('projecttaak_maken', views.ProjecttaakCreate.as_view(), name='projecttaak_maken'),
                    path('projecttaak/<int:pk>/', views.ProjecttaakUpdate.as_view(), name='projecttaak_update'),
                    path('projecttaak_details/<int:pk>/', views.ProjecttaakDetails.as_view(), name='projecttaak_details'),
                    path('projecttaak_beheer', views.projecttaak_beheer, name='projecttaak_beheer'),
                    path('projecttaak_list', views.projecttaak_list, name='projecttaak_list'),
                    
                    ]

