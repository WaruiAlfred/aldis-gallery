from django.db import models
import datetime as dt

#Image model
class Image(models.Model): 
  image_name = models.CharField(max_length=30)
  image_description = models.TextField()
  image = models.ImageField(upload_to = 'pictures/')
  
  def __str__(self):
    return self.image_name