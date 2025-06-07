from django.db import models
from django.contrib.auth import get_user_model
from services.models import Service

User = get_user_model()


class Booking(models.Model):
    """Represents a booking between a user and a service provider."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="bookings")
    scheduled_at = models.DateTimeField()
    confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Booking {self.id} for {self.service.title}"
