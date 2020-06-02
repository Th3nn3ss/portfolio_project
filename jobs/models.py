from django.db import models

# Create your models here.
class Job(models.Model):
    # Images for the tumbnails
    image = models.ImageField(upload_to='images/')
    # Summary for each tumbnail
    summary = models.CharField(max_length=200)
