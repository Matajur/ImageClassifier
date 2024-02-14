from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)  # Поле для категорії
    is_correct = models.BooleanField(null=True)  # Поле для позначення, чи вірна відповідь
    created_at = models.DateTimeField(auto_now_add=True)  # Час створення запиту

    def __str__(self):
        return f"{self.category} - {'Correct' if self.is_correct else 'Incorrect'}"
