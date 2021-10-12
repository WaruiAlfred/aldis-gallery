from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField

  
#Image category model
class Category(models.Model): 
  category_name = models.CharField(max_length=50)
  
  def save_image_category(self): 
    '''Function to save image category to the database'''
    self.save()
    
  def update_category(self): 
    '''Function to update specific model's data'''
    Category.objects.filter(id = self.id).update(category_name = self.category_name)
    
  def delete_category(self): 
    '''Function to delete a specific object'''
    category = Category.objects.get(id = self.id)
    if category: 
      category.delete()
  
  def __str__(self):
    return self.category_name

#location where image was taken model
class Location(models.Model): 
  location = models.CharField(max_length=30)
  date = models.DateTimeField()

  def save_location(self): 
    '''Function to save location image was taken to the database'''
    self.save()
    
  def update_location(self): 
    '''Function to update specific model's data'''
    Location.objects.filter(id = self.id).update(location = self.location,date =  self.date)
    
  def delete_location(self): 
    '''Function to delete a specific object'''
    location = Location.objects.get(id = self.id)
    if location: 
      location.delete()

  def __str__(self):
    return self.location
  
#Image model
class Image(models.Model): 
  image_name = models.CharField(max_length=30)
  image_description = models.TextField()
  image = CloudinaryField('image')
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  location_taken = models.ForeignKey(Location,on_delete=models.CASCADE,default=1)
  
  def save_image(self): 
    '''Function to save image to the database'''
    self.save()
    
  def update_image(self): 
    '''Function to update image object'''
    Image.objects.filter(id = self.id).update(image_name=self.image_name,
                                              image_description=self.image_description,
                                              image=self.image,
                                              category=self.category,
                                              location_taken=self.location_taken)
    
  def delete_image(self): 
    '''Function to delete a specific object'''
    image = Image.objects.get(id = self.id)
    if image: 
      image.delete()
    
  @classmethod
  def search_by_id(cls,search_id):
    '''Function to search an image according to inputted id'''
    image = cls.objects.filter(id__icontains=search_id)
    return image
  
  @classmethod
  def search_by_category(cls,search_id):
    '''Function to search images by category'''
    images = cls.objects.filter(category=search_id)
    return images
  
  @classmethod
  def search_by_location(cls,search_id):
    '''Function to search images according to locations they were taken'''
    images = cls.objects.filter(location_taken=search_id)
    return images
  
  def __str__(self):
    return self.image_name