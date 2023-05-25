from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    email = models.EmailField(max_length=80)
    numero = models.CharField(max_length=20)
    date = models.DateField(null=True, default=None)
    location = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    genre = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.name} {self.prenoms} {self.email} {self.numero} {self.date} {self.location} {self.commune} {self.status} {self.genre}"
    
class spirit(models.Model):
    CHOIX = [
        ("oui","oui"),
        ("non","non")
    ]
    DEPARTEMENT = [
        ("ESTER","ESTHER"),
        ("EMMANUEL","EMMANUEL"),
        ("JOSUE","JOSUE"),
        ("OSE","OSE"),
    ]
    COMMIT = [
        ("ORDRE ET ACCEUIL", "ORDRE ET ACCEUIL"),
        ("COMMITE SOCIAL", "COMMITE SOCIAL")
    ]
    person = models.ForeignKey(Person,null=True, blank=True, on_delete=models.CASCADE)
    baptism_water = models.CharField(max_length=3, default=None, choices=CHOIX)
    date = models.DateField(null=True, default=None)
    baptism_spirit = models.CharField(max_length=3, default=None, choices=CHOIX)
    community = models.CharField(max_length=16,null=True, default=None, choices=COMMIT)
    jeunesse = models.CharField(max_length=8,null=True, default=None, choices=DEPARTEMENT)
    
class scolaire(models.Model):
    LEVEL = [
        ("JE CONTINUE LES COURS","JE CONTINUE LES COURS"),
        ("CP1","CP1"),
        ("CP2","CP2"),
        ("CE1","CE1"),
        ("CE2","CE2"),
        ("CM1","CM1"),
        ("CM2","CM2"),
        ("SIXIEME","SIXIEME"),
        ("CINQUIEME","CINQUIEME"),
        ("QUATRIEME","QUATRIEME"),
        ("TROISIEME","TROISIEME"),
        ("SECOND","SECOND"),
        ("PREMIERE","PREMIERE"),
        ("TERMINAL","TERMINAL"),
        ("LICENCE 1","LICENCE 1"),
        ("LICENCE 2","LICENCE 2"),
        ("LICENCE 3","LICENCE 3"),
        ("MASTER 1","MASTER 1"),
        ("MASTER 2","MASTER 2"),
        ("DOCTORAT","DOCTORAT")
    ]
    
    DIPLOME = [
        ("CEPE","CEPE"),
        ("BEPEC","BEPEC"),
        ("BACCALAUREAT","BACCALAUREAT"),
        ("BTS","BTS"),
        ("LICENCE 3","LICENCE 3"),
        ("MASTER","MASTER"),
        ("DOCTORAT","DOCTORAT"),
        ("DUT","DUT"),
    ]
    TYPES = [
        ("A","A"),
        ("B","B"),
        ("C","C"),
        ("D","D"),
        ("E","E"),
        ("F","F"),
        ("G","G"),
    ]
    person = models.ForeignKey(spirit,null=True,default=None, on_delete=models.CASCADE)
    niveau = models.CharField(max_length=21,null=True, choices=LEVEL)
    diplomes = models.CharField(max_length=12,null=True, choices=DIPLOME)
    series = models.CharField(max_length=12,null=True, choices=TYPES)
    filieres = models.CharField(max_length=36, null=True)
    
class professionnal(models.Model):
    CHOIX = [
        ("oui","oui"),
        ("non","non")
    ]
    person = models.ForeignKey(scolaire,null=True, on_delete=models.CASCADE)
    domaine = models.CharField(max_length=80, null=True)
    working = models.CharField(max_length=3,null=True, choices=CHOIX)
    metier= models.CharField(max_length=80, null=True)
    description = models.TextField(null=True, default=None)
    cv = models.FileField(upload_to='PDF/CV/', null=True)
    image_de_profil = models.ImageField(upload_to='Pictures/profil', null=True)
    
# class PersonIdentifier(models.Model):
    
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     form2 = models.ForeignKey(spirit, on_delete=models.CASCADE, null=True, blank=True)
#     form3 = models.ForeignKey(scolaire, on_delete=models.CASCADE, null=True, blank=True)
#     form4 = models.ForeignKey(professionnal, on_delete=models.CASCADE, null=True, blank=True)