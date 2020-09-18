import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
#from rest_framework.test import APIRequestFactory
from .models import Breed, Dogs
from .serializers import BreedSerializer, DogSerializer

client = Client()

class GetAllBreeds(TestCase):
    """Test Module for GET all Breeds API"""
    def setUp(self):
        Breed.objects.create(
            name='Yorkshire Terrier',
            size='Small',
            friendliness='3',
            trainability='5',
            sheddingamount='2',
            exerciseneeds='1'
        )
        Breed.objects.create(
            name='Chinese Crested',
            size='Small',
            friendliness='4',
            trainability='2',
            sheddingamount='1',
            exerciseneeds='2'
        )
        Breed.objects.create(
            name='Corgi',
            size='Medium',
            friendliness='5',
            trainability='3',
            sheddingamount='2',
            exerciseneeds='3'
        )

    def test_all_dog_breeds(self):
        #getAPIResponse
        response = client.get(reverse('GET_POST_DogList'))
        #getDataFromDB
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)