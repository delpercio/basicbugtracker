from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class CustomUser(AbstractUser):
    position = models.CharField(max_length=40,null=True, blank=True)

# Ticket Model
class TicketModel(models.Model):
    title = models.CharField(max_length=50)
    time_reported = models.DateTimeField()
    created_by = models.ForeignKey()
    STATUS_CHOICES = [
        (NEW, 'New'),
        (INPROGRESS,'In Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid'),
    ]
    status = models.CharField
    (
    max_length=15,
    choices= STATUS_CHOICES,
    default= NEW
    ),
    assigned_to = models.ForeignKey()
    completed_by = models.ForeignKey()


