from rest_framework import serializers
from .models import Houses, Lands, LandImages, HouseImages


class HouseImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImages
        fields = "__all__"

class HousesSerializer(serializers.ModelSerializer):
    images = HouseImagesSerializer(many=True, read_only=True)
    class Meta:
        model = Houses
        fields = "__all__"


class LandImageSerializer(serializers.ModelSerializer):
    images = serializers.ReadOnlyField()
    class Meta:
        model = LandImages
        fields = "__all__"

class LandsSerializer(serializers.ModelSerializer):
    images = HouseImagesSerializer(many=True, read_only=True)
    class Meta:
        model = Lands
        fields = '__all__'

        
    
