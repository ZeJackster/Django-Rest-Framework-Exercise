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
        response = client.get(reverse('GET_POST_BreedList'))
        #getDataFromDB
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateNewBreedTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'name':'Bulldog',
            'size':'Medium',
            'friendliness':'3',
            'trainability':'2',
            'sheddingamount':'5',
            'exerciseneeds':'1'
        }
        self.invalid_paylod = {
            'name':'Hound',
            'size':'Extra Large',
            'friendliness':'0',
            'trainability':'0',
            'sheddingamount':'0',
            'exerciseneeds':'0'
        }
    
    def test_create_valid_dog_breed(self):
        response = client.post(
            reverse('GET_POST_BreedList'),
            data = json.dumps(self.valid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_dog_breed(self):
        response = client.post(
            reverse('GET_POST_BreedList'),
            data = json.dumps(self.invalid_paylod),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class GetSingleDogBreed(TestCase):
    def setUp(self):
        self.chihuahua = Breed.objects.create(
            name='Chihuahua',
            size='Tiny',
            friendliness='1',
            trainability='2',
            sheddingamount='1',
            exerciseneeds='3'
        )
        self.boston = Breed.objects.create(
            name='Boston Terrier',
            size='Small',
            friendliness='3',
            trainability='4',
            sheddingamount='1',
            exerciseneeds='2'
        )
        self.collie = Breed.objects.create(
            name='Boarder Collie',
            size='Small',
            friendliness='5',
            trainability='5',
            sheddingamount='2',
            exerciseneeds='4'
        )
    
    def test_get_valid_single_breed(self):
        response = client.get(reverse('GET_PUT_DELETE_Breed_Detail', kwargs={'pk' : self.boston.pk}))
        breed = Breed.objects.get(id=self.boston.pk)
        serializer = BreedSerializer(breed)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_breed(self):
        response = client.get(reverse('GET_PUT_DELETE_Breed_Detail', kwargs={'pk': 60}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)