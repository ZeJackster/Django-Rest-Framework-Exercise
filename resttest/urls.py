"""resttest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from quickstart import views
from quickstart.models import Dogs, Breed


# Sets the URLs that Django will use for the requests and assigns it a view
urlpatterns = [
    path(
        'dogs/',
        views.DogList.as_view({'get': 'list', 'post': 'create'}),
        name='GET_POST_DogList'
        ),
    path(
        'dogs/<int:pk>/',
        views.DogDetail.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='GET_PUT_DELETE_DogDetail'
        ),
    path(
        'breeds/',
        views.BreedList.as_view({'get': 'list', 'post': 'create'}),
        name='GET_POST_BreedList'
        ),
    path(
        'breeds/<int:pk>/',
        views.BreedDetail.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='GET_PUT_DELETE_Breed_Detail'
        ),
]
