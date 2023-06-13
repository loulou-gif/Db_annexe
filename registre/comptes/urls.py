from django.urls import path
from . import views


urlpatterns = [
    path('connexion',views.connexion ,name="connexion"),
    path('registre',views.registre, name="registre"),
    path('index',views.index, name='index'),
    path('deconnexion',views.deconnexion,name="deconnexion"),
    path('profil', views.profil, name="profil"),
    path('<int:person_id>/', views.details, name="details"),
    path('graph', views.graph, name="graph"),
    # path('change',views.change, name="change"),
]