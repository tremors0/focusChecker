from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render

from .services.analyzers import detect_faces, classify_images
from .services.image_processor import crop_faces


def index(request):
    return render(request, 'index.html')


def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)


def upload_image(request):
    if 'image' not in request.FILES:
        return JsonResponse({'status': 'Image was not uploaded successfully'})

    image = request.FILES['image']
    faces_data = detect_faces(image)
    cropped_faces = crop_faces(image, faces_data)

    # for every face check if person pays attention
    result = classify_images(cropped_faces)
    return JsonResponse(result, safe=False)


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
