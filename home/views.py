from django.shortcuts import render
from django.http import HttpResponseRedirect
from PIL import Image
import os
from django.conf import settings


def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        file = request.FILES.get('file')
        img = Image.open(file)
        path = os.path.join(settings.MEDIA_ROOT, file.name)
        img = img.save(path)
        return HttpResponseRedirect("/")
