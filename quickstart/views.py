from django.shortcuts import render
from .models import Dogs, Breed
from .serializers import DogSerializer, BreedSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404

# Create your views here.

class DogList(APIView):
    #get
    def get(self, request, format=None):
        dogs = Dogs.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)
    #post
    def post(self, request, format=None):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DogDetail(APIView):
    def get_object(self, pk):
        try:
            return Dogs.objects.get(id=pk)
        except Dogs.DoesNotExist:
            return None
    #get
    def get(self, request, pk, format=None):
        dogs = self.get_object(pk)
        if dogs == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = DogSerializer(dogs)
            return Response(serializer.data)

    #put
    def put(self, request, pk, format=None):
        dogs = self.get_object(pk)
        serializer = DogSerializer(dogs, data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #delete
    def delete(self, request, pk, format=None):
        dogs = self.get_object(pk)
        if dogs == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            dogs.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class BreedList(APIView):
    #get
    def get(self, request, format='json'):
        breed = Breed.objects.all()
        serializer = BreedSerializer(breed, many=True)
        return Response(serializer.data)
    #post
    def post(self, request, format=None):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class BreedDetail(APIView):
    def get_object(self, pk):
        try:
            return Breed.objects.get(id=pk)
        except Breed.DoesNotExist: 
            return None

    #get
    def get(self, request, pk, format=None):
        breed = self.get_object(pk)
        if breed == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = BreedSerializer(breed)
            return Response(serializer.data)

    #put
    def put(self, request, pk, format=None):
        breed = self.get_object(pk)
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #delete
    def delete(self, request, pk, format=None):
        breed = self.get_object(pk)
        if breed == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            breed.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
