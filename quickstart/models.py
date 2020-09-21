from django.db import models
# Create your models here.

#Breed Model as requested in the exercise
class Breed(models.Model):
    name = models.CharField(max_length=100, unique=True)
    size = models.CharField(max_length=10)
    friendliness = models.IntegerField()
    trainability = models.IntegerField()
    sheddingamount = models.IntegerField()
    exerciseneeds = models.IntegerField()

#Dogs Model as requested in the exercise
class Dogs(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=2)
    breed = models.ForeignKey(Breed, related_name="breed_name", on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favouritefood = models.CharField(max_length=100)
    favouritetoy = models.CharField(max_length=100)
