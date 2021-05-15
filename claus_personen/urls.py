from django.urls import include, path 
from . import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns =   [
                    
                    
                    path('personen', views.persoon, name='personen'),
                    path('persoon_account', views.persoon_account, name='persoon_account'),
                    path('persoon_gegevens', views.persoon_gegevens, name='persoon_gegevens'),


                    path('persoon_maken', views.PersoonCreate.as_view(), name='persoon_maken'),
                    path('persoon_update/<int:pk>/', views.PersoonUpdate.as_view(), name='persoon_update'),
                    path('persoon_details/<int:pk>/', views.PersoonDetails.as_view(), name='persoon_details'),
                    #path('persoon_beheer', views.persoon_beheer, name='persoon_beheer'),
                    path('persoon_list', views.persoon_list, name='persoon_list'),
                    
                    ]