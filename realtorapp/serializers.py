from rest_framework import serializers
from .models import Houses, Lands

class HousesSerializer(serializers.ModelSerializer):
    house_list = serializers.ReadOnlyField()

    class Meta:
        model = Houses
        fields = "__all__"

class LandsSerializer(serializers.ModelSerializer):
    land_list = serializers.ReadOnlyField()

    class Meta:
        model = Lands
        fields = "__all__"