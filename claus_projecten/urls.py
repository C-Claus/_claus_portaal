from django.urls import include, path 
from . import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns =   [
                    
                    
                    path('projecten', views.project, name='projecten' ),
                    path('project_maken', views.ProjectCreate.as_view(), name='project_maken'),
                    path('project/<int:pk>/', views.ProjectUpdate.as_view(), name='project_update'),
                    path('project_details/<int:pk>/', views.ProjectDetails.as_view(), name='project_details'),
                    path('project_beheer', views.project_beheer, name='project_beheer'),
                    path('project_list', views.project_list, name='project_list'),
                    
                    ]

