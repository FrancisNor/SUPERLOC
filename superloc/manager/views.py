from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from visitor.models import Category, Vehicle, Booking, Agency, vehicle_availability_list
from .forms import GetAgencyForm, VehicleAddForm, AvailabilityForm


class LoginManager(LoginView):
    template_name = 'manager/login.html'

def role_check(user):
    return user.groups.filter(name='manager').exists()

def logged_out(request):
    return render(request, 'manager/logged_out.html')

@login_required(login_url='manager:login')
@user_passes_test(role_check, login_url='manager:forbidden')
def home(request):
    return render(request, 'manager/index.html')

@login_required(login_url='manager:login')
def vehicles_availability_form(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():        
            agency_id = request.POST.get('agency')
            category_id = request.POST.get('category')
            date_departure = request.POST.get('date_departure')
            date_back= request.POST.get('date_back')
            agency_departure = Agency.objects.get(id=agency_id)
            category = Category.objects.get(id=category_id)
            vehicle_list=vehicle_availability_list(category, agency_departure, date_departure, date_back)
            date_departure_day = date_departure[8:10]
            date_departure_month = date_departure[5:7]
            date_departure_year = date_departure[0:4]
            date_departure_time = date_departure[11:]
            date_back_day = date_back[8:10]
            date_back_month = date_back[5:7]
            date_back_year = date_back[0:4]
            date_back_time = date_back[11:]
            if date_back<date_departure:
                return HttpResponse('La date de retour doit être postérieure à la date de départ.')
            else:
                context = {'agency':agency_departure,
                            'vehicle_list':vehicle_list,
                            'date_departure':date_departure,
                            'date_back':date_back,
                            'date_departure_day':date_departure_day,
                            'date_departure_month':date_departure_month,
                            'date_departure_year':date_departure_year,
                            'date_departure_time':date_departure_time,
                            'date_back_day':date_back_day,
                            'date_back_month':date_back_month,
                            'date_back_year':date_back_year,
                            'date_back_time':date_back_time,
                }       
            return render(request, 'manager/vehicles_availability.html', context)
    availability_form=AvailabilityForm()
    context = {'form': availability_form}
    return render(request, 'manager/vehicles_availability_form.html', context)

@login_required(login_url='manager:login')
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

@login_required(login_url='manager:login')
def booking(request):
    return render(request, 'manager/booking.html')

@login_required(login_url='manager:login')
def vehicles_management_agency_choice(request):
    if request.method == 'POST':
        agency = request.POST.get('name')
        return redirect('manager:vehicles_management', agency)
    get_agency_form = GetAgencyForm()
    context = {'form': get_agency_form}
    return render(request, 'manager/vehicles_management_agency_choice.html', context)

@login_required(login_url='manager:login')
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

@login_required(login_url='manager:login')
@permission_required('visitor.change_vehicle', raise_exception=True)
def vehicle_delete(request, id) :
    try:
        vehicle = Vehicle.objects.get(id__exact=id.upper())
    except Vehicle.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        vehicle=Vehicle.objects.get(id=id)
        vehicle.is_active = False
        vehicle.save()
        agency=Agency.objects.get(id=vehicle.agency_id)
        agency_nbr=agency.id
        return redirect(f'/manager/vehicles_management/{agency_nbr}')
    return render(request, 'manager/vehicle_delete.html', {'vehicle': vehicle})

@login_required(login_url='manager:login')
@permission_required('visitor.change_vehicle', raise_exception=True)
def vehicle_add(request,id):
    try:
        agency = Agency.objects.get(id__exact=id.upper())
    except Agency.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        vehicle = Vehicle(agency=agency)
        form= VehicleAddForm(request.POST, instance=vehicle)
        if form.is_valid():
            vehicle=form.save()
            agency = Agency.objects.get(id=vehicle.agency_id)
            agency_nbr = agency.id
            return redirect(f'/manager/vehicles_management/{agency_nbr}')
    else:
        form = VehicleAddForm()
    context = {'form': form,'agency': agency}
    return render(request, 'manager/vehicle_add.html', context)
