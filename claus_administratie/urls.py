from django.urls import include, path 
from . import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns =   [
                    
                    
                    path('administratie', views.administratie,  name='administratie' ),
                    path('administratie_maken', views.AdministratieCreate.as_view(), name='administratie_maken'),
                    path('administratie/<int:pk>/', views.AdministratieUpdate.as_view(), name='administratie_update'),
                    path('administratie_details/<int:pk>/', views.AdministratieDetails.as_view(), name='administratie_details'),
                    path('administratie_beheer', views.administratie_beheer, name='administratie_beheer'),
                    path('administratie_list', views.administratie_list, name='administratie_list'),
                    
                    ]

