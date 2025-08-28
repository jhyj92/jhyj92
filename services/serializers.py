from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "provider",
            "title",
            "description",
            "service_type",
            "location",
            "available",
        ]
        read_only_fields = ["provider"]
