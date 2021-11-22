from django.shortcuts import render

def home(request):
    """User home page"""
    return render(request, 'visitor/index.html')

def legal_notice(request) :
    return render(request, 'visitor/legal_notice.html')
