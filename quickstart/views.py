from django.shortcuts import render, get_object_or_404
from .models import Dogs, Breed
from .serializers import DogSerializer, BreedSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets


class DogList(viewsets.ModelViewSet):
    queryset = Dogs.objects.all()
    serializer_class = DogSerializer


class DogDetail(viewsets.ModelViewSet):
    queryset = Dogs.objects.all()
    serializer_class = DogSerializer


class BreedList(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedDetail(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
