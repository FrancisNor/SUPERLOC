from django.shortcuts import render
from django.http import Http404

from visitor.models import Category, Agency

def home(request):
    return render(request, 'visitor/index.html')

def legal_notice(request) :
    return render(request, 'visitor/legal_notice.html')

def todo(request) :
    return render(request, 'visitor/todo.html')

def language_choice(request) :
    return render(request, 'visitor/language_choice.html')

def login(request) :
    return render(request, 'registration/login.html')

def inscription(request) :
    return render(request, 'registration/inscription.html')

def inscription_done(request) :
   return render(request, 'registration/inscription_done.html')

def tourism_categories(request):
    categories = Category.objects.filter(is_active=True)
    context = {'category_list' : categories}
    return render(request, 'visitor/tourism_categories.html', context)

def tourism_category(request, code):
    try:
        category = Category.objects.get(code__exact=code.upper())
    except Category.DoesNotExist:
        raise Http404
    return render(request,'visitor/tourism_category.html', {'category': category})

def agencies(request):
    agencies = Agency.objects.filter(is_active=True)
    context = {'agency_list' : agencies}
    return render(request, 'visitor/agencies.html', context)

def register(request):
    next_page = request.GET.get('next', '')
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user but do not save it yet. The password has to be set with
            # the set_password method to ensure that it will be recorded as a hash in the
            # database
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Customer.objects.create(user=new_user)
            return render(request, 'registration/inscription_done.html',
                          {'new_user': new_user, 'next': next_page})
        else:
            messages.error(request, "Error")
            return render(request, 'registration/inscription.html',
                          {'user_form': user_form, 'next': next_page})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'registration/inscription.html',
                      {'user_form': user_form, 'next': next_page})