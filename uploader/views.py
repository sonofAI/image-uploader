from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from .models import UploadedImage
from .forms import ImageUploadForm

# Create your views here.

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            image_url = request.build_absolute_uri(uploaded_image.image.url)
            return JsonResponse({'success': True, 'image_url': image_url})
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def view_image(request, image_id):
    image = get_object_or_404(UploadedImage, id=image_id)
    return HttpResponse(f'<img src="{image.image.url}" alt="Uploaded Image">')