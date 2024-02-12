from django.shortcuts import render
from django.http import JsonResponse
from .forms import ImageUploadForm
from .models import Image
import random

def image_upload(request):
    form = ImageUploadForm()
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Визначаємо категорію і зберігаємо зображення
            categories = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
            random_category = random.choice(categories)
            uploaded_image = form.save(commit=False)
            uploaded_image.category = random_category
            uploaded_image.save()
            return JsonResponse({'category': random_category, 'image_id': uploaded_image.id})
    return render(request, 'image_classification/image_upload.html', {'form': form})

def save_feedback(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        is_correct = request.POST.get('feedback') == 'true'
        
        try:
            # Тут ми оновлюємо лише поле is_correct
            image = Image.objects.get(id=image_id)
            image.is_correct = is_correct
            image.save(update_fields=['is_correct'])
            return JsonResponse({'status': 'success'})
        except Image.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Image not found'}, status=404)

    return JsonResponse({'status': 'error'}, status=400)
