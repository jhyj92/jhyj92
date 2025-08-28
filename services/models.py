from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Service(models.Model):
    """Represents a service offered by a provider."""

    SERVICE_TYPES = [
        ("cleaning", "Cleaning"),
        ("plumbing", "Plumbing"),
        ("electrical", "Electrical"),
        ("gardening", "Gardening"),
    ]

    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="services")
    title = models.CharField(max_length=100)
    description = models.TextField()
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    location = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.title} - {self.provider.username}"
