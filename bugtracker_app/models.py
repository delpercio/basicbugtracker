from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Custom User Model
class CustomUser(AbstractUser):
    position = models.CharField(max_length=40,null=True, blank=True)

# Ticket Model

STATUS_CHOICES = (
    ('New', 'NEW'),
    ('In Progress','INPROGRESS'),
    ('Done','DONE'),
    ('Invalid', 'INVALID')
    )

class Ticket(models.Model):
    title = models.CharField(max_length=50)
    time_reported = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    # created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # completed_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    def __str__(self):
        return self.title