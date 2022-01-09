from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import Http404
from visitor.models import Vehicle, Booking, Agency
from .forms import GetAgencyForm, VehicleAddForm

class LoginManager(LoginView):
    template_name = 'manager/login.html'


def role_check(user):
    return user.groups.filter(name='manager').exists()

"""
@login_required(login_url='manager:login')
@permission_required('rental.change_agency', raise_exception=True)
def agencies_home(request):
    return render(request, 'manager/index.html')

def logged_out(request):
    return render(request, 'manager/logged_out.html')
from django.shortcuts import render
"""

@login_required(login_url='manager:login')
#@user_passes_test(role_check, login_url='manager:forbidden')
def home(request):
    return render(request, 'manager/index.html')

#@login_required(login_url='manager:login')
def vehicles_availability_agency_choice(request):
    if request.method == 'POST':
         agency = request.POST.get('name')
         return redirect('manager:vehicles_availability', agency)
    get_agency_form=GetAgencyForm()
    context= {'form': get_agency_form}
    return render(request, 'manager/vehicles_availability_agency_choice.html', context)

#@login_required(login_url='manager:login')
def vehicles_availability(request, id) :
    try:
        agency = Agency.objects.get(id__exact=id.upper())
    except Agency.DoesNotExist:
        raise Http404
    vehicle = Vehicle.objects.filter(is_active=True, agency_id=agency.id)
    context = {'vehicle_list' : vehicle,
               'agency': agency
               }
    return render(request, 'manager/vehicles_availability.html', context)
#Affiche tous les véhicules affectés à l'agence, pas de filtre sur les dates de réservations

#@login_required(login_url='manager:login')
def vehicles_management_agency_choice(request):
    get_agency_form=GetAgencyForm()
    context= {'form': get_agency_form}
    return render(request, 'manager/vehicles_management_agency_choice.html', context)

#@login_required(login_url='manager:login')
def vehicles_management(request, id) :
    try:
        agency = Agency.objects.get(id__exact=id.upper())
    except Agency.DoesNotExist:
        raise Http404
    vehicle = Vehicle.objects.filter(is_active=True, agency_id=agency.id)
    context = {'vehicle_list' : vehicle,
               'agency': agency
               }
    return render(request, 'manager/vehicles_management.html', context)

#@login_required(login_url='manager:login')
def vehicles_management_vehicle_add(request):
    vehicle_add_form=VehicleAddForm()
    if request.method == 'POST':
        vehicle_add_form = VehicleAddForm(request.POST)
        if vehicle_add_form.is_valid():
            vehicle_add_form.save()
            return redirect('manager:vehicles_management')
    context= {'form': vehicle_add_form}
    return render(request, 'manager/vehicles_management_vehicle_add.html', context)
