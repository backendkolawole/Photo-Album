from django.urls import path

from . import views

urlpatterns = [
    
    # view all photos
    path('', views.gallery, name='gallery'),
    
    # view a particular photo
    path('photo/<str:pk>/', views.photo, name='photo'),
    
    # add photos to gallery
    path('add/', views.add, name='add'),
]