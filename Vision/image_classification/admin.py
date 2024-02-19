from django.contrib import admin
from .models import Image
import os

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'uploaded_at', 'category', 'is_correct', 'created_at']
    actions = ['delete_true', 'delete_false', 'delete_none']

    def delete_model(self, request, obj):
        # If the model has a file field and it is not empty, delete the file
        if obj.image and os.path.isfile(obj.image.path):
            os.remove(obj.image.path)
        obj.delete()

    def delete_queryset(self, request, queryset):
        # Similar to delete_model, but for deleting multiple objects
        for obj in queryset:
            self.delete_model(request, obj)

    def delete_true(self, request, queryset):
        # We delete all images with is_correct=True
        for obj in queryset.filter(is_correct=True):
            self.delete_model(request, obj)
    delete_true.short_description = "Delete images with true feedback (True)"

    def delete_false(self, request, queryset):
        # We delete all images with is_correct=False
        for obj in queryset.filter(is_correct=False):
            self.delete_model(request, obj)
    delete_false.short_description = "Delete images with true feedback (False)"

    def delete_none(self, request, queryset):
        # We delete all images with is_correct=None
        for obj in queryset.filter(is_correct__isnull=True):
            self.delete_model(request, obj)
    delete_none.short_description = "Delete image without feedback (None)"
