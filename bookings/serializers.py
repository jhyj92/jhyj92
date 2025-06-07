from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "id",
            "user",
            "service",
            "scheduled_at",
            "confirmed",
            "created_at",
        ]
        read_only_fields = ["user", "confirmed", "created_at"]
