from django.shortcuts import render
from django.http import HttpResponseRedirect


def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        file = request.FILES
        print(file)
        return HttpResponseRedirect("/")
