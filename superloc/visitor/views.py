from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from visitor.models import Category, Agency, Customer, Booking, Vehicle, vehicle_availability_list
from visitor.forms import UserRegistrationForm, UserEditForm, CustomerEditForm, BookingForm

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

def inscription(request):
    next_page = request.GET.get('next', '')
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        customer_form = CustomerEditForm(request.POST)
        if user_form.is_valid() and customer_form.is_valid() :
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.username = new_user.email
            new_user.save()
            Customer.objects.create(user=new_user)
            customer_form.save()
            return render(request, 'registration/inscription_done.html',
                          {'new_user': new_user, 'next': next_page})
        else:
            messages.error(request, "Error")
            return render(request, 'registration/inscription.html',
                          {'user_form': user_form, 'customer_form': customer_form, 'next': next_page})
    else:
        user_form = UserRegistrationForm()
        customer_form = CustomerEditForm()
        return render(request, 'registration/inscription.html',
                      {'user_form': user_form, 'customer_form': customer_form, 'next': next_page})


@login_required
def edit_customer(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        customer_form = CustomerEditForm(request.POST, instance=request.user.customer, files=request.FILES)
        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            next_page = request.GET.get('next')
            return redirect(next_page)
    else:
        user_form = UserEditForm(instance=request.user)
        customer_form = CustomerEditForm(instance=request.user.customer)
        next_page = request.GET.get('next')
        return render(request, 'visitor/edit_customer.html',
                      {'user_form': user_form, 'customer_form': customer_form, 'next': next_page})

@login_required
def reservation(request):
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
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
            return render(request, 'visitor/reservation_vehicle_choice.html', context)
    booking_form=BookingForm()
    context = {'form': booking_form}
    return render(request, 'visitor/reservation.html', context)

def reservation_vehicle_choice(request) :
    if request.method == 'POST':
        booking_vehicle = request.POST.get('car')
        agency_departure = request.POST.get('agency')
        date_departure= request.POST.get('date_departure')
        date_back = request.POST.get('date_back')
        vehicle = Vehicle.objects.get(registration_number=booking_vehicle)
        agency = Agency.objects.get(id=agency_departure)
        customer = Customer.objects.get(user_id=request.user.id)
        booking = Booking(vehicle=vehicle,
                          date_start=date_departure,
                          date_end=date_back,
                          agency=agency,
                          customer=customer,
                          confirm=True)
        booking.save()
        date_departure_day = date_departure[8:10]
        date_departure_month = date_departure[5:7]
        date_departure_year = date_departure[0:4]
        date_departure_time = date_departure[11:]
        date_back_day = date_back[8:10]
        date_back_month = date_back[5:7]
        date_back_year = date_back[0:4]
        date_back_time = date_back[11:]
        context = {'agency': agency,
                   'booking':booking,
                   'vehicle': vehicle,
                   'date_departure': date_departure,
                   'date_back': date_back,
                   'date_departure_day': date_departure_day,
                   'date_departure_month': date_departure_month,
                   'date_departure_year': date_departure_year,
                   'date_departure_time': date_departure_time,
                   'date_back_day': date_back_day,
                   'date_back_month': date_back_month,
                   'date_back_year': date_back_year,
                   'date_back_time': date_back_time,
                   }
        return render(request, 'visitor/index.html', context)
    return render(request, 'visitor/reservation_confirmation')

@login_required(login_url='visitor:login')
def booking_management(request):
    user=request.user
    customer=Customer.objects.get(user_id=user.id)
    booking_list=Booking.objects.filter(customer_id=customer.id)
    context = {'booking_list': booking_list, 'user' : user}
    return render(request, 'visitor/booking_management.html', context)