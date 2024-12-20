from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def courses(request):
    return render(request,'courses.html')

def bootcamp(request):
    return render(request,'bootcamp.html')

def request_callback(request):
    return render(request,'request_callback.html')