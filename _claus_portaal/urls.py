"""_claus_portaal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from claus_registratie import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"), 
    
    path('', include('claus_portaal.urls')),
    path('', include('claus_administratie.urls')),
    path('', include('claus_personen.urls')),
    path('', include('claus_projecten.urls')),
    path('', include('claus_kostencodes.urls')),
    path('', include('claus_projecttaken.urls')),


    path('', include('claus_bouwtechnische_opname.urls')),
    path('', include('claus_planning.urls')),
    
    path('', include('claus_aanwezigheids_assistent.urls')),

    path('', include('claus_uren.urls')),
    
    path('', include('django.contrib.auth.urls')),
    
]
