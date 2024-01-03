from rest_framework import serializers
from .models import TPlace

class TPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPlace
        fields = '__all__'
