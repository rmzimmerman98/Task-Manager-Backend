from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=32)
    notes = models.CharField()
    time_to_complete = models.IntegerField()

    URGENT = 'UR'
    DO = 'DO'
    DEFER = 'DF'
    PRIORITY_CHOICES = (
        (URGENT, 'urgent'),
        (DO, 'do'),
        (DEFER, 'defer'),
    )
    priority = models.CharField(
        max_length=2,
        choices= PRIORITY_CHOICES,
        default=DO,
    )