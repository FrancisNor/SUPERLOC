from django.shortcuts import render

def home(request):
    """User home page"""
    return render(request, 'visitor/index.html')
