from django.test import TestCase
from .models import Category,Location,Image

# Test classes
class CategoryTestClass(TestCase): #category test class
  
  def setUp(self): 
    '''Function that runs before every test'''
    self.new_category = Category(category_name = "Food")
    
  def test_instance(self): 
    '''Function testing that an instance of the object exists'''
    self.assertTrue(isinstance(self.new_category,Category))
    
  def test_save_method(self): 
    '''Function testing the save method'''
    self.new_category.save_image_category()
    categories = Category.objects.all()
    self.assertTrue(len(categories)>0)
    
  def test_update_method(self): 
    '''Function testing the update method'''
    self.new_category.save_image_category()
    Category.objects.filter(category_name = "Food").update(category_name = "Travel")
    update = Category.objects.get(category_name = "Travel")
    self.assertEqual(self.new_category,update)
    
  def test_delete_method(self):
    '''Function testing the delete method''' 
    self.new_category.save_image_category()
    self.new_category.delete_category()
    categories = Category.objects.all()
    self.assertTrue(len(categories)==0)
    
