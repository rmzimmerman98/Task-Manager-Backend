from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=32)
    time_to_complete = models.IntegerField()
    
    URGENT = 'URGENT'
    DO = 'DO'
    DEFER = 'DEFER'
    PRIORITY_CHOICES = (
        (URGENT, 'urgent'),
        (DO, 'do'),
        (DEFER, 'defer'),
    )
    priority = models.CharField(
        choices= PRIORITY_CHOICES,
        default=DO,
    )
    notes = models.CharField()
    
    # def get_priority_display(self):
    #     # Override get_FOO_display() to return the desired values
    #     # based on the checked radio button
    #     if self.priority == self.URGENT:
    #         return 'urgent'
    #     elif self.priority == self.DO:
    #         return 'do'
    #     elif self.priority == self.DEFER:
    #         return 'defer'