from django.shortcuts import render

from visitor.models import Category
from visitor.models import Agency

def home(request):
    return render(request, 'visitor/index.html')

def legal_notice(request) :
    return render(request, 'visitor/legal_notice.html')

def todo(request) :
    return render(request, 'visitor/todo.html')

def language_choice(request) :
    return render(request, 'visitor/language_choice.html')

def login(request) :
    return render(request, 'visitor/login.html')

def inscription(request) :
    return render(request, 'visitor/inscription.html')

def tourism_categories(request):
    categories = Category.objects.all()
    context = {'category_list' : categories}
    return render(request, 'visitor/tourism_categories.html', context)

def tourism_category(request, code):
    try:
        category = Category.objects.get(code__exact=code.upper())
    except Category.DoesNotExist:
        raise Http404
    return render(request,'visitor/tourism_category.html', {'category': category})

def agencies(request):
    agencies = Agency.objects.all()
    context = {'agency_list' : agencies}
    return render(request, 'visitor/agencies.html', context)