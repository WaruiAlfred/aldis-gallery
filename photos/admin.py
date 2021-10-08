from django.contrib import admin
from .models import Category,Location,Image

# Registering models
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)