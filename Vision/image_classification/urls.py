# image_classification/urls.py

from django.urls import path
from .views import image_upload

urlpatterns = [
    path('', image_upload, name='image_upload'),
]
