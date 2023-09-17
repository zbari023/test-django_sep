from django.db import models
from django.utils import timezone
# Create your models here.


class Video(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    description= models.CharField(max_length=500)
    create_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name