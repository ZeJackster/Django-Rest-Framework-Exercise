# Django-Rest-Framework-Exercise
This project is the design and function of a REST API using Django's framework

# Motivation
The motivation for the project is to learn how to use the Django REST Framework

# Build Status
Build Status == Passing

# Frameworks Used
Django 3.1.1 <br>
Django REST Framework 3.11.0

# Features
* GET and POST requests to the `/breeds/` endpoint, and the `/dogs/` endpoint
* GET, PUT, and DELETE requests to the `/breeds/{int:pk}/` endpoint, and the `/dogs/{int:pk}` endpoint

# Code Example
models.py
```
#Dogs Model as requested in the exercise
class Dogs(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, related_name="breed_name", on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favouritefood = models.CharField(max_length=100)
    favouritetoy = models.CharField(max_length=100)
```

serializers.py
```
class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dogs
        fields = ('id', 'name', 'age', 'breed', 'gender', 'color', 'favouritefood', 'favouritetoy')
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    breed = serializers.SlugRelatedField(slug_field='name', queryset=Breed.objects.all())
    gender = serializers.CharField()
    color = serializers.CharField()
    favouritefood = serializers.CharField()
    favouritetoy = serializers.CharField()

```

views.py
```
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
```

tests.py
```
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
```

# Installation
On Windows OS, ensure you have the python 3.8.5 installed<br>
Python can be downloaded from the following link https://www.python.org/downloads/ <br>
When launching Python.exe to install it, ensure you lick 'Add Python to Environment Variables'
Download the project to your desired project folder<br>

Open PowerShell and navigate to the directory you want to download the project
```
$ cd /path/to/desired/folder/
```

Use pip to install virtualenv
```
$ pip install virtualenv
```

Use pip to install pipenv
```
$ pip install pipenv
```

Create a virtual environment
```
$ python -m venv env
```

There should be a folder called env now<br>
Run the following command to start the environemnt
```
$ env\Scripts\activate
```

Navigated to the folder that was downloaded
```
$ cd testfolder
```

From here, install the packages from the requirements.txt
```
$ pip install -r requirements.txt
```

Start the environment
```
$ python manage.py runserver
```

From here, you should be able to go to your browser, type in http://localhost:8000/dogs/ and see a return of the original get request.<br>
Once you are done with the environment, press CTRL+C to close it.

# Tests
While the server is active, go to the project root folder and run the `python manage.py test` command to run the unit tests to ensure everything is working

# How to use?
### Breeds Requests
* GET ALL - Get a list of all existing breeds of dogs with a `GET` request to the `/breeds/` endpoint
* CREATE NEW - Create a new breed of dog by using a `POST` request to the `/breeds/` endpoint
* GET ONE - Get the details for a single breed using a `GET` request to the `/breeds/<int:pk>/` endpoint
* UPDATE ONE - Update a breed with a `PUT` request to `/breeds/<int:pk>/`
* DELETE ONE - Delete a breed with a `DELETE` request to `/breeds/<int:pk>/`
Note: pk is the ID which can be retrieved with GET ALL request

### Dogs Requests
* GET ALL - Get a list of all existing dogs with a `GET` request to the `/dogs/` endpoint
* CREATE NEW - Create a new dog by using a `POST` request to the `/dogs/` endpoint 
* GET ONE - Get the details for a single dog by using a `GET` request to the `/dogs/<int:pk>/` endpoint
* UPDATE ONE - Update a dog with a `PUT` request to `/dogs/<int:pk>/` endpoint
* DELETE ONE - Delete a dog with a `DELETE` request to `/dogs/<int:pk>/` endpoint
Note: pk is the ID which can be retrieved by the GET ALL request

# Contribute
Suggestions on how to improve code along with an explanation of how is always appreciated

# Credits
@MLHale for creating the exercise
https://mlhale.github.io/CYBR8470/modules/building-a-server/django-exercise.html

# License
Django: Copyright (c) Django Software Foundation and individual contributors.
Django REST Framework: Copyright © 2011-present, Encode OSS Ltd. All rights reserved.
