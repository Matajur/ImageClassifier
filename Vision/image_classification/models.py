from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)  # Category field
    is_correct = models.BooleanField(null=True)  # Field to indicate whether the answer is correct
    created_at = models.DateTimeField(auto_now_add=True)  # Request creation time

    def __str__(self):
        return f"{self.category} - {'Correct' if self.is_correct else 'Incorrect'}"
