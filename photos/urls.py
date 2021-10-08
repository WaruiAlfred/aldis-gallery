from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#url patterns for the app urls
urlpatterns = [
  path('',views.home,name='home'),
  path('search_id/<int:id>',views.search_by_id,name='get_image_by_id'),
  path('search_category/',views.search_by_category,name='get_image_by_category'),
  path('search_location/',views.search_by_location,name='get_image_by_location'),
]

#configuring uploaded images url
if settings.DEBUG: 
  urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)