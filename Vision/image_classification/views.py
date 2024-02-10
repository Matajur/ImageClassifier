from django.shortcuts import render
from django.http import HttpResponse
import random
from .forms import ImageUploadForm
from django.http import JsonResponse

from django.shortcuts import redirect

def image_upload(request):
    form = ImageUploadForm()
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.cleaned_data['image']
            categories = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
            random_category = random.choice(categories)
            return JsonResponse({'category': random_category})
    return render(request, 'image_classification/image_upload.html', {'form': form})

def image_classification(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.cleaned_data['image']
            categories = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
            random_category = random.choice(categories)
            return JsonResponse({'category': random_category})
    return redirect('image_upload')
