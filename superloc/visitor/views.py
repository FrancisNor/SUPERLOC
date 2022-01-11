from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from visitor.models import Category, Agency, Customer
from visitor.forms import UserRegistrationForm, UserEditForm, CustomerEditForm

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
'''
def vehicle_availability_list(category, agency, )
'''
'''
def liste_vehicules_disponibles(categorie, agence, reservation_date_depart, reservation_date_retour):​
    liste_contrats_conclus_bloquants_sur_la_periode_demandee = (​
        Contrat.objects.all() # On part de la liste de tous les contrats puis on va la filtrer​
        .filter(agence=agence) # on retient ceux signés dans l'agence concernée par la recherche​
        .filter(date_fin__gte=reservation_date_depart) # si la date de retour d'un contrat existant est postérieur à notre date de départ​
        .filter(date_debut__lte=reservation_date_retour) # et si la date de début d'un contrat existant est antérieur à notre date de retour​
    )​
​
    vehicules_disponibles = (​
        Vehicule.objects.all() # On part de la liste de tous les véhicules puis on va la filtrer​
        #.filter(active=True) # à condition qu'ils soient actifs​
        .filter(categorie=categorie) # à condition que la catégorie corresponde à celle demandée dans le formulaire​
        .filter(agence=agence)  #à condition que l'agence corresponde à celle demandée dans le formulaire​
        .exclude(id__in=Subquery(liste_contrats_conclus_bloquants_sur_la_periode_demandee.values('vehicule'))) #à condition que le véhicule ne figure pas dans un contrat déjà conclu aux dates souhaitées​
    )​
    return vehicules_disponibles​
'''

'''
# Fonction de sélection de véhicule disponibles
# (appelée à partir du moment où le formulaire agence / dates de réservations) est valide

# En fonction des données soumies et de leue validité, affiche un template ou un autre :
#       confirm-reservation-infos-vehicule.html
#  ou   enregistrement-contrat.html
def selection_vehicule(request, reservation, reservation_form):
    #Récupération des informations soumies par le formualire
    categorie = reservation.get('categorie')​
    agence = reservation.get('agence_depart')​
    date_depart = reservation.get('date_depart')​
    date_retour = reservation.get('date_retour')​
    vehicule_id = request.POST.get('vehicule_id')​
    reservation_step = request.POST.get('reservation-step')​
​
    if (vehicule_id):​
        client_form = ClientForm()​
        if (request.user.client):​
            client_form = ClientForm(instance=request.user.client)​
        if (reservation_step and reservation_step == 'infos-client'):​
            client_form = ClientForm(request.POST, instance=request.user.client or None)​
            if (client_form.is_valid()):​
                client = client_form.save(commit=False)​
                if (not client.user):​
                    client.user = request.user​
                client.save()​
​
                vehicule = Vehicule.objects.get(id=vehicule_id)​
                already_contracted = (​
                    Contrat.objects.all()​
                        .filter(agence=agence)​
                        .filter(vehicule=vehicule)​
                        .filter(date_fin__gte=date_depart)​
                        .filter(date_debut__lte=date_retour)​
                )​
​
                error = ''​
                if already_contracted.count() > 0:​
                    ctr_error = 'Impossible de réserver à partir des choix transmis. Le véhicule demandé n\'est plus disponible.'​
                    context = {'ctr_error': ctr_error}​
                    return render(request, 'enregistrement-contrat.html', context)​
                elif not error:​
                    # création du contrat​
                    ctr_error = ''​
                    contrat = Contrat(vehicule=vehicule, client=client, agence=agence, date_debut=date_depart, date_fin=date_retour)​
                    contrat.save()​
​
                    # context​
                    context = {​
                        'ctr_error': ctr_error,​
                        'agence': agence,​
                        'vehicule': vehicule,​
                        'date_debut': date_depart,​
                        'date_fin': date_retour,​
                        'client': client,​
                        'contrat': contrat,​
                    }​
                    return render(request, 'enregistrement-contrat.html', context)​
                elif(error):​
                    ctr_error = error​
                    context = {'ctr_error': ctr_error}​
                    return render(request, 'enregistrement-contrat.html', context)​
​
        context = {'vehicule_id': vehicule_id, 'reservation': reservation, 'client_form': client_form}​
        return render(request, 'confirm-reservation-infos-client.html', context)​
​
    #Récupération de la liste des véhicules disponibles​
    vehicules = liste_vehicules_disponibles(categorie, agence, date_depart, date_retour)​
​
    context = {'vehicules': vehicules, 'reservation': reservation, 'reservation_form': reservation_form}​
    return render(request, 'confirm-reservation-infos-vehicule.html', context)​
'''