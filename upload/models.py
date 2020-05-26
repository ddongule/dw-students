from django.db import models
from django.utils import timezone 

class Assignment(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(blank=True, null=True, upload_to="assignments/%Y/%m/%d")
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
