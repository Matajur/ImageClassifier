from django.shortcuts import render
from django.http import JsonResponse
from .forms import ImageUploadForm
from .models import Image
from .model.classifier import predict_img

def image_upload(request):
    form = ImageUploadForm()
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            file_path = uploaded_image.image.path
            
            # Визначення категорії за допомогою моделі
            category = predict_img(file_path)
            
            uploaded_image.category = category
            uploaded_image.save()
            return JsonResponse({'category': category, 'image_id': uploaded_image.id})
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
