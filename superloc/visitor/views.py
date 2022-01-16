from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.db.models import Subquery

from visitor.models import Category, Agency, Customer, vehicle_availability_list, Vehicle, Contrat
from visitor.forms import UserRegistrationForm, UserEditForm, CustomerEditForm, AvailabilityForm, ReservationVehiculeForm, ClientForm

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

@login_required(login_url='visitor:login')
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
            context = {'agency':agency_departure,
                       'vehicle_list':vehicle_list,
                       'date_departure':date_departure,
                       'date_back':date_back,
                       }
            return render(request, 'visitor/vehicles_availability.html', context)
    availability_form=AvailabilityForm()
    context = {'form': availability_form}
    return render(request, 'visitor/vehicles_availability_form.html', context)

@login_required(login_url='visitor:login')
def vehicles_availability(request, id) :
    try:
        agency = Agency.objects.get(id__exact=id.upper())
    except Agency.DoesNotExist:
        raise Http404
    vehicle = Vehicle.objects.filter(is_active=True, agency_id=agency.id)
    context = {'vehicle_list' : vehicle,
               'agency': agency
               }
    return render(request, 'visitor/vehicles_availability.html', context)

@login_required(login_url='visitor:login')
def booking(request):
    return render(request, 'visitor/booking.html')

###################################################################################################



def role_customers_check(user):
    return user.groups.filter(name='customers').exists()

def liste_vehicules_disponibles(category, agency, reservation_date_depart, reservation_date_retour):
    liste_contrats_conclus_bloquants_sur_la_periode_demandee = (
        Contrat.objects.all() # On part de la liste de tous les contrats puis on va la filtrer
        .filter(agency=agency) # on retient ceux signés dans l'agence concernée par la recherche
        .filter(date_fin__gte=reservation_date_depart) # si la date de retour d'un contrat existant est postérieur à notre date de départ
        .filter(date_debut__lte=reservation_date_retour) # et si la date de début d'un contrat existant est antérieur à notre date de retour
    )

    vehicules_disponibles = (
        Vehicle.objects.all() # On part de la liste de tous les véhicules puis on va la filtrer
        #.filter(active=True) # à condition qu'ils soient actifs
        .filter(category=category) # à condition que la catégorie corresponde à celle demandée dans le formulaire
        .filter(agency=agency)  #à condition que l'agence corresponde à celle demandée dans le formulaire
        .exclude(id__in=Subquery(liste_contrats_conclus_bloquants_sur_la_periode_demandee.values('vehicle'))) #à condition que le véhicule ne figure pas dans un contrat déjà conclu aux dates souhaitées
    )
    return vehicules_disponibles

def selection_vehicule(request, reservation, reservation_form):
    #Récupération des informations soumies par le formualire
    category = reservation.get('category')
    agency = reservation.get('agence_depart')
    date_depart = reservation.get('date_depart')
    date_retour = reservation.get('date_retour')
    vehicle_id = request.POST.get('vehicle_id')
    reservation_step = request.POST.get('reservation-step')

    if (vehicle_id):
        client_form = ClientForm()
        print(1)
        if (request.user.customer):
            print(2)
            client_form = ClientForm(instance=request.user.customer)

        print(3)
        if (reservation_step and reservation_step == 'infos-client'):
            print(4)
            client_form = ClientForm(request.POST, instance=(request.user.customer or None))
            if (client_form.is_valid()):
                print(5)
                client = client_form.save(commit=False)
                if (not Customer.user):
                    Customer.user = request.user
                Customer.save()

                vehicle = Vehicle.objects.get(id=vehicle_id)
                already_contracted = (
                    Contrat.objects.all()
                        .filter(agency=agency)
                        .filter(vehicle=vehicle)
                        .filter(date_fin__gte=date_depart)
                        .filter(date_debut__lte=date_retour)
                )

                error = ''
                if already_contracted.count() > 0:
                    ctr_error = 'Impossible de réserver à partir des choix transmis. Le véhicule demandé n\'est plus disponible.'
                    context = {'ctr_error': ctr_error}
                    return render(request, 'visitor/enregistrement-contrat.html', context)
                elif not error:
                    # création du contrat
                    ctr_error = ''
                    contrat = Contrat(vehicle=vehicle, customer=customer, agency=agency, date_debut=date_depart, date_fin=date_retour)
                    contrat.save()

                    # context
                    context = {
                        'ctr_error': ctr_error,
                        'agency': agency,
                        'vehicle': vehicle,
                        'date_debut': date_depart,
                        'date_fin': date_retour,
                        'customer': customer,
                        'contrat': contrat,
                    }
                    return render(request, 'visitor/enregistrement-contrat.html', context)
                elif(error):
                    ctr_error = error
                    context = {'ctr_error': ctr_error}
                    return render(request, 'visitor/enregistrement-contrat.html', context)

        context = {'vehicle_id': vehicle_id, 'reservation': reservation, 'client_form': client_form}
        return render(request, 'visitor/confirm-reservation-infos-client.html', context)

    #Récupération de la liste des véhicules disponibles
    vehicles = liste_vehicules_disponibles(category, agency, date_depart, date_retour)

    context = {'vehicles': vehicles, 'reservation': reservation, 'reservation_form': reservation_form}
    return render(request, 'visitor/confirm-reservation-infos-vehicule.html', context)

@login_required(login_url='visitor:login')
def reservation(request):
    reservation_form = ReservationVehiculeForm() #Appel du formulaire
    if request.method == 'POST':
        # Alimentation de la classe formulaire à partir des informations soulises dans le formulaire
        reservation_form = ReservationVehiculeForm(request.POST) 

        #Si le formulaire est valide (Agence, date de départ, date de retour)
        if reservation_form.is_valid():
            reservation = reservation_form.cleaned_data
            # On fait appel à la fonction de selection des véhicules qui va elle même rechercher les véhicules disponibles
            return selection_vehicule(request, reservation, reservation_form)

    #si formulaire invalide ou non soumis : affichage du template avec le formualire Agence/date départ / date retour
    context = {'reservation_form': reservation_form}
    return render(request, 'visitor/reservation.html', context)