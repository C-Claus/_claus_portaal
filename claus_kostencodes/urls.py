from django.urls import include, path 
from . import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns =   [
                    
                    
                    path('kostencodes', views.kostencodes,  name='kostencodes' ),
                    path('kostencodes_maken', views.KostenCodeCreate.as_view(), name='kostencodes_maken'),
                    path('kostencodes/<int:pk>/', views.KostenCodeUpdate.as_view(), name='kostencodes_update'),
                    path('kostencodes_details/<int:pk>/', views.KostenCodeDetails.as_view(), name='kostencodes_details'),
                    path('kostencodes_beheer', views.kostencodes_beheer, name='kostencodes_beheer'),
                    path('kostencodes_list', views.kostencodes_list, name='kostencodes_list'),
                    
                    ]
