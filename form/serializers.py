from datetime import timezone
from rest_framework import serializers
from .models import  BookInspection

class BookInspectionSerializer(serializers.ModelSerializer):
    appointment_list = serializers.ReadOnlyField()

    class Meta:
        model = BookInspection
        fields = "__all__"


    def validate_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Appointment date should be in future.")
        return value