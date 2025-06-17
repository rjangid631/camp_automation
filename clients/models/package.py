from django.db import models
from django.core.exceptions import ValidationError

from clients.models.client import Client
from clients.models.service import Service  # Import from same directory

class Package(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    services = models.ManyToManyField(Service, related_name='packages')
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date cannot be earlier than start date.")

    def __str__(self):
        return f"{self.name} ({self.start_date} to {self.end_date})"
