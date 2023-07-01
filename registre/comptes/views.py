from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from .forms import registreForm
from django.contrib.auth.models import User
from formulaires.models import Person, spirit, scolaire, professionnal
# Create your views here.

# formulaire de connexion

def connexion(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
        
        user =authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Mots de passe ou Username incorrecte")
        
    return render(request,'connexion.html')

# formulaire de création de compte
def registre(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = registreForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            redirect('connexion')
        else:
            messages.info(request, "Mots de passe ou Username incorrecte")
    
    form = registreForm()
    context = {
        'form': form
    }         
    return render(request, 'registre.html',context)

# vue de modification de parametre



# déconnexion d'un compte

def deconnexion(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    logout(request)
    return redirect('connexion')


# page de connexion
# 
def index(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    membres = Person.objects.all().order_by('name')
    context={
        'membres': membres
    }
    return render(request, 'pages/index.html', context)


def details(request, person_id):
    if not request.user.is_authenticated:
        return redirect('connexion')
    context = {
        'person': get_object_or_404(Person, pk=person_id),
        'spirit': get_object_or_404(spirit, pk=person_id),
        'scolaire': get_object_or_404(scolaire, pk=person_id),
        'professionnal': get_object_or_404(professionnal, pk=person_id),
    }
    return render(request, 'pages/details.html', context)

# page profil et de modification de mail ou de nom

def profil(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    
    # obj = get_object_or_404(User, pk=pk)
    # if request.method == 'POST':
    #     nom = request.POST.get("Nom")
    #     prenoms = request.POST.get("Prenoms")
    #     description = request.POST.get("Description")
    #     email = request.POST.get("email")
        
    #     obj.last_name = nom
    #     obj.first_name = prenoms
    #     obj.email = email
        
    
    user = request.user
    context = {
        'user': user,
        # 'obj': obj
    }
    
        
    return render(request, 'pages/profil.html', context)



# change le mot de passe
# def change(request):
#     return render(request, 'pages/change.html')

# page graph

def graph(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    hommes = Person.objects.filter(genre="masculin")
    femmes = Person.objects.filter(genre="feminin")
    employer = professionnal.objects.filter(working="oui")
    chomeur = professionnal.objects.filter(working="non")
    number_employer = employer.count()
    number_chomeur = chomeur.count()
    number_hommes = hommes.count()
    number_femmes = femmes.count()
    total = number_hommes + number_femmes
    pour_employer = (number_employer / total )* 100
    pour_chomeur = (number_chomeur / total )* 100 
    pour_hommes = (number_hommes / total )* 100
    pour_femmes = (number_femmes / total )* 100
    context={
        'hommes': hommes,
        'femmes': femmes,
        'Nbrehommes': number_hommes,
        'Nbrefemmes': number_femmes,
        'pour_hommes': pour_hommes,
        'pour_femmes': pour_femmes,
        'total': total,
        'pour_employer': pour_employer,
        'pour_chomeur': pour_chomeur,
        'Nbremployer': number_employer,
        'Nbrechomeur': number_chomeur,
        'employer' : employer,
        'chomeur' : chomeur
    }
    return render(request, 'pages/graph.html', context)


def stat2(request):
    men = Person.objects.filter(genre="masculin")
    women = Person.objects.filter(genre="feminin")
    baptised = spirit.objects.filter(baptism_spirit="oui")
    not_baptised = spirit.objects.filter(baptism_spirit="non")  
    born_again = spirit.objects.filter(baptism_water="oui")
    not_born_again = spirit.objects.filter(baptism_water="non")
    number_baptised = baptised.count()
    number_not_baptised = not_baptised.count()
    number_born_again = born_again.count()
    number_not_born_again = not_born_again.count()
    number_men = men.count()
    number_women = women.count()
    total = number_men + number_women
    pourcent_baptised = (number_baptised / total )* 100
    pourcent_not_baptised = (number_not_baptised / total )* 100
    pourcent_born_again = (number_born_again / total )* 100
    pourcent_not_born_again = (number_not_born_again / total )* 100
    context = {
        'number_men': number_men,
        'number_women': number_women,
        'number_baptised': number_baptised,
        'number_not_baptised': number_not_baptised,
        'number_born_again': number_born_again,
        'number_not_born_again': number_not_born_again,
        'pourcent_baptised': pourcent_baptised,
        'pourcent_not_baptised': pourcent_not_baptised,
        'pourcent_born_again': pourcent_born_again,
        'pourcent_not_born_again': pourcent_not_born_again,
        'total': total
    }
    return render(request, 'pages/stat2.html', context)

def stat3(request):
    men = Person.objects.filter(genre="masculin")
    women = Person.objects.filter(genre="feminin")
    not_diplomed = scolaire.objects.filter(series="Aucun")
    number_men = men.count()
    number_women = women.count()
    total = number_men + number_women
    number_not_diplomed = not_diplomed.count()
    number_diplomed = total - number_not_diplomed
    pourcent_diplomed = (number_not_diplomed / total )* 100
    pourcent_not_diplomed = (number_diplomed / total )* 100
    context = {
        'number_men': number_men,
        'number_women': number_women,
        'number_diplomed': number_diplomed,
        'number_not_diplomed': number_not_diplomed,
        'pourcent_diplomed': pourcent_diplomed,
        'pourcent_not_diplomed': pourcent_not_diplomed,
        'total': total
    }
    return render(request, 'pages/stat3.html', context)

def stat4(request):
    men = Person.objects.filter(genre="masculin")
    women = Person.objects.filter(genre="feminin")
    maried = Person.objects.filter(status="Marié")
    fianced = Person.objects.filter(status="Fiancé")
    widow = Person.objects.filter(status="Veuf")
    celibataire = Person.objects.filter(status="Celibataire")
    number_men = men.count()
    number_women = women.count()
    total = number_men + number_women
    number_maried = maried.count()
    number_celibataire = celibataire.count()
    number_fianced = fianced.count()
    number_widow = widow.count()
    pourcent_maried = (number_maried / total )* 100
    pourcent_celibataire = (number_celibataire / total )* 100
    pourcent_fianced = (number_fianced / total )* 100
    pourcent_widow = (number_widow / total )* 100
    context = {
        'number_men': number_men,
        'number_women': number_women,
        'number_maried': number_maried,
        'number_celibataire': number_celibataire,
        'number_fianced': number_fianced,
        'number_widow': number_widow,
        'pourcent_maried': pourcent_maried,
        'pourcent_celibataire': pourcent_celibataire,
        'pourcent_fianced': pourcent_fianced,
        'pourcent_widow': pourcent_widow,
        'total': total
    }    
    return render(request, 'pages/stat4.html', context)