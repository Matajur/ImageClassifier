from django.contrib import admin
from .models import Image
import os

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'uploaded_at', 'category', 'is_correct', 'created_at']
    actions = ['delete_true', 'delete_false', 'delete_none']

    def delete_model(self, request, obj):
        # Якщо у моделі є файлове поле і воно не пусте, видаляємо файл
        if obj.image and os.path.isfile(obj.image.path):
            os.remove(obj.image.path)
        obj.delete()

    def delete_queryset(self, request, queryset):
        # Подібно delete_model, але для видалення кількох об'єктів
        for obj in queryset:
            self.delete_model(request, obj)

    def delete_true(self, request, queryset):
        # Видаляємо всі зображення з is_correct=True
        for obj in queryset.filter(is_correct=True):
            self.delete_model(request, obj)
    delete_true.short_description = "Видалити зображення з вірним відгуком (True)"

    def delete_false(self, request, queryset):
        # Видаляємо всі зображення з is_correct=False
        for obj in queryset.filter(is_correct=False):
            self.delete_model(request, obj)
    delete_false.short_description = "Видалити зображення з невірним відгуком (False)"

    def delete_none(self, request, queryset):
        # Видаляємо всі зображення з is_correct=None
        for obj in queryset.filter(is_correct__isnull=True):
            self.delete_model(request, obj)
    delete_none.short_description = "Видалити зображення без відгуку (None)"
