from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#url patterns for the app urls
urlpatterns = [
  path('',views.home,name='home')
]

#configuring uploaded images url
if settings.DEBUG: 
  urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)