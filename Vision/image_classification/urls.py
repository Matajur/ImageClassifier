from django.urls import path
from .views import image_upload, save_feedback

urlpatterns = [
    path('', image_upload, name='image_upload'),
    path('save_feedback', save_feedback, name='save_feedback'),
]
