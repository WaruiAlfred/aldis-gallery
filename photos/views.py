from django.shortcuts import render
from .models import Image,Category,Location

# Create your views here.
def home(request): 
  '''Home view function'''
  images = Image.objects.all()
  return render(request,'home.html',{"images":images})

def search_by_id(request,id): 
  '''Function to search images by id'''
  found_image = Image.search_by_id(id)
  output_info = f"{id}"
  return render(request,'picture.html',{"message":output_info,"id_image":found_image})
  
def search_by_category(request): 
  '''Function to search images by category'''
  
  #confirm that the query exists and it actually contains a value
  if 'image_category' in request.GET and request.GET["image_category"]: 
    search_term = request.GET.get("image_category")
    image_category = Category.objects.filter(category_name = search_term )
    found_images = Image.search_by_category(image_category[0])
    output_info = f"{search_term}"
    
    return render(request,'search.html',{"category_message":output_info,"category_images":found_images})
  
  else: 
    output_info = "You haven't inputted a search value"
    return render(request,'search.html',{"category_message":output_info})
  
def search_by_location(request): 
  '''Function to search images by location they were taken'''
  
  #confirm that the query exists and it actually contains a value
  if 'image_location' in request.GET and request.GET["image_location"]: 
    search_term = request.GET.get("image_location")
    image_location = Location.objects.filter(location = search_term)
    found_images = Image.search_by_location(image_location[0])
    output_info = f"{search_term}"
    
    return render(request,'search.html',{"location_message":output_info,"location_images":found_images})
  
  else: 
    output_info = "You haven't inputted a search value"
    return render(request,'search.html',{"location_message":output_info})
  
def picture(request,picture_id): 
  '''Function to render'''