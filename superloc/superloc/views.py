from django.shortcuts import redirect

def home(request):
    # redirect to /visitor
    response = redirect('/visitor/')
    return response
