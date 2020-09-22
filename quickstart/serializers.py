from rest_framework import serializers
from .models import Dogs, Breed

# choice array to be used for Sizes in Breeds
SIZE_CHOICES = (
    "Tiny",
    "Small",
    "Medium",
    "Large",
)


# Serializes Data for the Breed Model
class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = (
            'id',
            'name',
            'size',
            'friendliness',
            'trainability',
            'sheddingamount',
            'exerciseneeds'
        )

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    size = serializers.ChoiceField(choices=SIZE_CHOICES)
    friendliness = serializers.ChoiceField(choices=("1", "2", "3", "4", "5"))
    trainability = serializers.ChoiceField(choices=("1", "2", "3", "4", "5"))
    sheddingamount = serializers.ChoiceField(choices=("1", "2", "3", "4", "5"))
    exerciseneeds = serializers.ChoiceField(choices=("1", "2", "3", "4", "5"))


# Serialized Data for the Dogs Model
class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dogs
        fields = (
            'id',
            'name',
            'age',
            'breed',
            'gender',
            'color',
            'favouritefood',
            'favouritetoy'
        )
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    breed = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Breed.objects.all()
    )
    gender = serializers.CharField()
    color = serializers.CharField()
    favouritefood = serializers.CharField()
    favouritetoy = serializers.CharField()
