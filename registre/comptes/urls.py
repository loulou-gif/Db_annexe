from django.urls import path
from . import views

# app_name= "comptes"

urlpatterns = [
    path('connexion',views.connexion ,name="connexion"),
    path('registre',views.registre, name="registre"),
    path('index',views.index, name='index'),
    path('deconnexion',views.deconnexion,name="deconnexion"),
    path('profil', views.profil, name="profil"),
    path('<int:person_id>/', views.details, name="details"),
    path('graph', views.graph, name="graph"),
    path('recherche', views.recherche, name="recherche"),
    path('resultats', views.resultats, name="resultats"),
]