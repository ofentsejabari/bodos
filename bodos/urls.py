"""projectRepository URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views

app_name = 'bodos'

urlpatterns = [
    #-- bodos/ --
    path('', views.index, name = 'index'),

    #-- bodos/login --
    path('login', views.login, name = 'login'),

    #-- bodos/register --
    path('register', views.register, name = 'register'),

    # #-- bodos/about --
    # path('', views.about, name = 'about'),
    #
    # #-- bodos/datasets --
    # path('', views.datasets, name = 'datasets'),
    #
    # #-- bodos/problemsets --
    # path('', views.problemsets, name = 'problemsets'),
    #
    # #-- bodos/functions --
    # path('', views.functions, name = 'functions'),
]
