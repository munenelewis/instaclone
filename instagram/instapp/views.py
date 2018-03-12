from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Profile
from django.http import Http404


def index(request):
    all_images = Image.objects.all()
    return render(request, 'insta/index.html', {'all_images':all_images})

def detail(request, image_id):
    try:
        image = Image.objects.get(pk=image_id)
    except Image.DoesNotExist:
        raise Http404('bye')
    return render(request, 'insta/details.html', {'image':image})
