from django.urls import path
from . import views

app_name = "main"

from . import views
from rest_framework import routers
from django.urls import path, include


urlpatterns = [

    #
    path('', views.Index),

    
    ]