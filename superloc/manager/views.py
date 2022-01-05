from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render

TODO = 'manager/todo.html'


class LoginManager(LoginView):
    template_name = 'manager/login.html'


def role_check(user):
    return user.groups.filter(name='manager').exists()


@login_required(login_url='manager:login')
@user_passes_test(role_check, login_url='manager:forbidden')
def home(request):
    """ Manager home page"""
    return render(request, 'manager/index.html')


@login_required(login_url='manager:login')
def vehicles_home(request):
    return render(request, TODO)


@login_required(login_url='manager:login')
def customers_home(request):
    return render(request, TODO)


@login_required(login_url='manager:login')
@permission_required('rental.change_agency', raise_exception=True)
def agencies_home(request):
    return render(request, 'manager/todo.html')


def logged_out(request):
    return render(request, 'manager/logged_out.html')
from django.shortcuts import render

# Create your views here.
