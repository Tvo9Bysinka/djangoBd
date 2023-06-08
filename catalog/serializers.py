# serializers.py
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import *

class FacultetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultet
        fields = '__all__'


class NapravlenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Napravlenie
        fields = '__all__'

class Forma_kontrol9Serializer(serializers.ModelSerializer):
    class Meta:
        model = Forma_kontrol9
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group 
        fields = '__all__'

class RabotnikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rabotnik 
        fields = '__all__'

class StudentiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studenti
        fields = '__all__'

class PredmetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predmet 
        fields = '__all__'

class JurnalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jurnal
        fields = '__all__'

class FicsationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficsation
        fields = '__all__'