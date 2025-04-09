from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Files


def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        file = request.FILES.get('file')
        img = Files(name="my_img", url=file)
        img.save()
        return HttpResponseRedirect("/")
