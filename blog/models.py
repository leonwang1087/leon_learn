from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to="images/")
    contents = models.TextField(max_length=500)
    description = models.TextField(max_length=50)
