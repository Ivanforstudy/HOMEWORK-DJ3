from django.shortcuts import render, redirect

def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

# Create your views here.
