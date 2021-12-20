from django.shortcuts import render

from visitor.models import Category

def home(request):
    """User home page"""
    return render(request, 'visitor/index.html')

def legal_notice(request) :
    return render(request, 'visitor/legal_notice.html')

def todo(request) :
    return render(request, 'visitor/todo.html')

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