from django.urls import path
from . import views

#url patterns for the app urls
urlpatterns = [
  path('',views.home,name='home')
]
