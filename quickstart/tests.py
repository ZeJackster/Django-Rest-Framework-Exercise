import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
#from rest_framework.test import APIRequestFactory
from .models import Breed, Dogs
from .serializers import BreedSerializer, DogSerializer

client = Client()

class GetAllBreeds(TestCase):
    """Test for getting a list of all breeds"""
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

    def test_get_all_breeds(self):
        #getAPIResponse
        response = client.get(reverse('GET_POST_BreedList'))
        #getDataFromDB
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateNewBreedTest(TestCase):
    """Test for creating a new breed"""
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
    
    def test_create_valid_breed(self):
        response = client.post(
            reverse('GET_POST_BreedList'),
            data = json.dumps(self.valid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_breed(self):
        response = client.post(
            reverse('GET_POST_BreedList'),
            data = json.dumps(self.invalid_paylod),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class GetSingleBreed(TestCase):
    """Test For Getting a single breeds details"""
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

class UpdateSingleBreedTest(TestCase):
    """Test for updating a single breed"""
    def setUp(self):
        self.dachshund = Breed.objects.create(
            name='Dachshund',
            size='Tiny',
            friendliness='5',
            trainability='3',
            sheddingamount='3',
            exerciseneeds='4'
        )
        self.dane = Breed.objects.create(
            name='Great Dane',
            size='Large',
            friendliness='4',
            trainability='1',
            sheddingamount='2',
            exerciseneeds='4'
        )
        self.valid_payload = {
            'name':'Dachshund',
            'size':'Large',
            'friendliness':'5',
            'trainability':'2',
            'sheddingamount':'2',
            'exerciseneeds':'1',
        }
        self.invalid_payload = {
            'name':'Great Dane',
            'size':'Very Large',
            'friendliness':'4',
            'trainability':'1',
            'sheddingamount':'6',
            'exerciseneeds':'1',
        }

    def test_valid_update_breed(self):
        response = client.put(
            reverse('GET_PUT_DELETE_Breed_Detail', kwargs={'pk':self.dachshund.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_breed(self):
        response = client.put(
            reverse('GET_PUT_DELETE_Breed_Detail', kwargs={'pk':self.dane.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleBreedTest(TestCase):
    """Test case for deleting a single breed of dogs"""
    
    def setUp(self):
        self.lapphund = Breed.objects.create(
            name='Finnish Lapphund',
            size='Small',
            friendliness='2',
            trainability='1',
            sheddingamount='2',
            exerciseneeds='5'
        )
        self.pug = Breed.objects.create(
            name='Pug',
            size='Small',
            friendliness='4',
            trainability='3',
            sheddingamount='1',
            exerciseneeds='5'
        )
        
    def test_valid_delete_breed(self):
        response = client.delete(reverse('GET_PUT_DELETE_Breed_Detail', kwargs={'pk':self.lapphund.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_breed(self):
        response = client.delete(reverse('GET_PUT_DELETE_Breed_Detail', kwargs={'pk':50}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class GetAllDogsTest(TestCase):
    """Test Case for Get All Dogs"""
    def setUp(self):
        greatDane = Breed.objects.create(
            name='Great Dane',
            size='Large',
            friendliness='4',
            trainability='1',
            sheddingamount='2',
            exerciseneeds='4'
        )        
        chineseCrested = Breed.objects.create(
            name='Chinese Crested',
            size='Small',
            friendliness='4',
            trainability='2',
            sheddingamount='1',
            exerciseneeds='2'
        )
        corgi = Breed.objects.create(
            name='Corgi',
            size='Medium',
            friendliness='5',
            trainability='3',
            sheddingamount='2',
            exerciseneeds='3'
        )
        Dogs.objects.create(
            name='Molly',
            age='10',
            breed=greatDane,
            gender='Female',
            color='Gray',
            favouritefood='Peanut Butter',
            favouritetoy='Tennis Ball'
        )
        Dogs.objects.create(
            name='Hairy',
            age='2',
            breed=chineseCrested,
            gender='Male',
            color='White',
            favouritefood='Broccoli',
            favouritetoy='Slippers'
        )
        Dogs.objects.create(
            name='Dorky',
            age='5',
            breed=corgi,
            gender='Male',
            color='Beige',
            favouritefood='Chicken',
            favouritetoy='Frisby'
        )
    def test_get_all_dogs(self):
        #getAPIResponse
        response = client.get(reverse('GET_POST_DogList'))
        #getDataFromDB
        dogs = Dogs.objects.all()
        serializer = DogSerializer(dogs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateNewDogTest(TestCase):
    """Create a a new dog"""
    def setUp(self):
        beagle = Breed.objects.create(
            name='Beagle',
            size='Small',
            friendliness='4',
            trainability='2',
            sheddingamount='3',
            exerciseneeds='2'
        )
        basset = Breed.objects.create(
            name='Basset Hound',
            size='medium',
            friendliness='3',
            trainability='3',
            sheddingamount='3',
            exerciseneeds='3',
        )
        self.valid_payload = {
            'name':'Ginger',
            'age':'5',
            'breed':'Beagle',
            'gender':'Female',
            'color':'Beige',
            'favouritefood':'Ice Cream',
            'favouritetoy':'shoes'
        }
        self.invalid_payload = {
            'name':'Lady',
            'age':'500',
            'breed':'Underdog',
            'gender':'Female',
            'color':'Beige',
            'favouritefood':'Bones',
            'favouritetoy':'Beachball'
        }

    def test_create_valid_dog(self):
        response = client.post(
            reverse('GET_POST_DogList'),
            data = json.dumps(self.valid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_dog(self):
        response = client.post(
            reverse('GET_POST_DogList'),
            data = json.dumps(self.invalid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class GetSingleDog(TestCase):
    """Test GET a single dog details"""
    def setUp(self):
        chihuahua = Breed.objects.create(
            name='Chihuahua',
            size='Tiny',
            friendliness='1',
            trainability='2',
            sheddingamount='1',
            exerciseneeds='3'
        )
        boston = Breed.objects.create(
            name='Boston Terrier',
            size='Small',
            friendliness='3',
            trainability='4',
            sheddingamount='1',
            exerciseneeds='2'
        )
        self.spot = Dogs.objects.create(
            name='Spot',
            age='0',
            breed=chihuahua,
            gender='Male',
            color='Tan',
            favouritefood='Bananas',
            favouritetoy='Frisby'
        )
        self.toby = Dogs.objects.create(
            name='Toby',
            age='4',
            breed=boston,
            gender='Male',
            color='Black and White',
            favouritefood='Steak',
            favouritetoy='Plastic Steak'
        )
    def test_valid_single_dog(self):
        response = client.get(reverse('GET_PUT_DELETE_DogDetail', kwargs={'pk' : self.toby.pk}))
        dog = Dogs.objects.get(id=self.toby.pk)
        serializer = DogSerializer(dog)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_single_dog(self):
        response = client.get(reverse('GET_PUT_DELETE_DogDetail', kwargs={'pk' : 60}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class UpdateSingleDog(TestCase):
    """Test PUT Single Dog"""
    def setUp(self):
        jackRussel = Breed.objects.create(
            name='Jack Russel Terrier',
            size='Small',
            friendliness='5',
            trainability='2',
            sheddingamount='3',
            exerciseneeds='4'
        )
        dalmation = Breed.objects.create(
            name='Dalmation',
            size='Large',
            friendliness='4',
            trainability='5',
            sheddingamount='2',
            exerciseneeds='3'
        )
        self.jack = Dogs.objects.create(
            name='Jack',
            age='4',
            breed=jackRussel,
            gender='Male',
            color='Tan and White',
            favouritefood='Pasta',
            favouritetoy='Food Dish'
        )
        self.smoky = Dogs.objects.create(
            name='Smoky',
            age='6',
            breed=dalmation,
            gender='Female',
            color='Black and White',
            favouritefood='Smoked Meat',
            favouritetoy='Fire Hat'
        )
        self.valid_payload = {
            'name':'Smoky',
            'age':'7',
            'breed':'Dalmation',
            'gender':'Female',
            'color':'Black and White',
            'favouritefood':'Smoked Meat',
            'favouritetoy':'Fire Hat'
        }
        self.invalid_payload = {
            'name':'Jack',
            'age':'4',
            'breed':'Turkey',
            'gender':'Male',
            'color':'Brown and White',
            'favouritefood':'Pasta',
            'favouritetoy':''
        }
    def test_valid_update_breed(self):
        response = client.put(
            reverse('GET_PUT_DELETE_DogDetail', kwargs={'pk':self.smoky.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_breed(self):
        response = client.put(
            reverse('GET_PUT_DELETE_DogDetail', kwargs={'pk':self.jack.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleDogTest(TestCase):
    def setUp(self):
        lapphund = Breed.objects.create(
            name='Finnish Lapphund',
            size='Small',
            friendliness='2',
            trainability='1',
            sheddingamount='2',
            exerciseneeds='5'
        )
        pug = Breed.objects.create(
            name='Pug',
            size='Small',
            friendliness='4',
            trainability='3',
            sheddingamount='1',
            exerciseneeds='5'
        )
        self.fluffy = Dogs.objects.create(
            name='Fluffy',
            age='1',
            breed=lapphund,
            gender='Male',
            color='Black',
            favouritefood='Tacos',
            favouritetoy='Stuffed Bunny'
        )
        self.grumpy = Dogs.objects.create(
            name='Grumpy',
            age='3',
            breed=pug,
            gender='Female',
            color='Tan',
            favouritefood='Everything',
            favouritetoy='Soccer Ball'
        )

    def test_valid_delete_breed(self):
        response = client.delete(reverse('GET_PUT_DELETE_DogDetail', kwargs={'pk':self.fluffy.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_breed(self):
        response = client.delete(reverse('GET_PUT_DELETE_DogDetail', kwargs={'pk':50}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)