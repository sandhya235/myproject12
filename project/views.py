from django.shortcuts import render

# Create your views here.
def mywebsite(request):
    return render(request,'mywebsite.html')
def home(request):
    return render(request,'home.html')
def courses(request):
    return render(request,'courses.html')
def bootcamp(request):
    return render(request,'bootcamp.html')
def requested(request):
    return render(request,'requested.html')
def signin(request):
    return render(request,'signin.html')

