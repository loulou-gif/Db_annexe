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
    if not request.user.is_authenticated:
        return redirect('connexion')
    logout(request)
    return redirect('connexion')


# page de connexion
# 
def index(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    if not request.user.is_authenticated:
        return redirect('connexion')
    membres = Person.objects.all()
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
def change(request):
    return render(request, 'pages/change.html')

# page graph

def graph(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    hommes = Person.objects.filter(genre="masculin")
    femmes = Person.objects.filter(genre="feminin")
    employer = professionnal.objects.filter(working="oui")
    chomeur = professionnal.objects.filter(working="non")
    Nbremployer = employer.count()
    Nbrechomeur = chomeur.count()
    Nbrehommes = hommes.count()
    Nbrefemmes = femmes.count()
    total = Nbrehommes + Nbrefemmes
    pour_employer = (Nbremployer / total )* 100
    pour_chomeur = (Nbrechomeur / total )* 100 
    pour_hommes = (Nbrehommes / total )* 100
    pour_femmes = (Nbrefemmes / total )* 100
    context={
        'hommes': hommes,
        'femmes': femmes,
        'Nbrehommes': Nbrehommes,
        'Nbrefemmes': Nbrefemmes,
        'pour_hommes': pour_hommes,
        'pour_femmes': pour_femmes,
        'total': total,
        'pour_employer': pour_employer,
        'pour_chomeur': pour_chomeur,
        'Nbremployer': Nbremployer,
        'Nbrechomeur': Nbrechomeur,
        'employer' : employer,
        'chomeur' : chomeur
    }
    return render(request, 'pages/graph.html', context)


def recherche(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    query = request.GET.get('q')
    if query:
        context = {
            'results' : Person.objects.filter(Q(name__icontains=query) | Q(prenoms__icontains=query)),
            'resultats' : professionnal.objects.filter(Q(domaine__icontains=query | Q(metier__icontains=query)))
        }
    else:
        context ={
            'results' : [],
            'resultats' : []
        }
    return render(request, 'pages/index.html', context)


def resultats(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    query = request.GET.get('q')
    if query:
        context = {
            'results' : Person.objects.filter(Q(name__icontains=query) | Q(prenoms__icontains=query)),
            'resultats' : professionnal.objects.filter(Q(domaine__icontains=query | Q(metier__icontains=query)))
        }
    else:
        context ={
            'results' : [],
            'resultats' : []
        }
    return render(request, 'pages/resultats.html', context)