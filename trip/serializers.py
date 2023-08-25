from rest_framework import serializers
from .models import *
from django_countries.serializers import CountryFieldMixin
from account.models import *
class UserSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'userSex',
            'userAge',
            'userNation',
            'selfIntro',
            'language',
            'userUni',
            'userSNS'
        )

class TripGetSerializer(serializers.ModelSerializer):
    leader = UserSerializer()
    class Meta:
        model = trip
        fields = '__all__'

class TripPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = trip
        fields = '__all__'