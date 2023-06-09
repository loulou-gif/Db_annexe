# Generated by Django 3.1.14 on 2023-06-16 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulaires', '0024_auto_20230616_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='commune',
            field=models.CharField(blank=True, choices=[('abobo', 'Abobo'), ('adjame', 'Adjamé'), ('anyama', 'Anyama'), ('attecoube', 'Attécoubé'), ('bingerville', 'Bingerville'), ('cocody', 'Cocody'), ('koumassi', 'Koumassi'), ('marcory', 'Marcory'), ('plateau', 'Plateau'), ('port-bouet', 'Port-Bouët'), ('treichville', 'Treichville'), ('yopougon', 'Yopougon')], max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='location',
            field=models.CharField(blank=True, choices=[('Abengourou', 'Abengourou'), ('Abidjan', 'Abidjan'), ('Aboisso', 'Aboisso'), ('Adzopé', 'Adzopé'), ('Agboville', 'Agboville'), ('Akoupé', 'Akoupé'), ('Anyama', 'Anyama'), ('Bingerville', 'Bingerville'), ('Bondoukou', 'Bondoukou'), ('Bouaflé', 'Bouaflé'), ('Bouaké', 'Bouaké'), ('Boundiali', 'Boundiali'), ('Dabou', 'Dabou'), ('Daloa', 'Daloa'), ('Daoukro', 'Daoukro'), ('Dimbokro', 'Dimbokro'), ('Divo', 'Divo'), ('Ferkessédougou', 'Ferkessédougou'), ('Gagnoa', 'Gagnoa'), ('Grand-Bassam', 'Grand-Bassam'), ('Guiglo', 'Guiglo'), ('Issia', 'Issia'), ('Katiola', 'Katiola'), ('Korhogo', 'Korhogo'), ('Lakota', 'Lakota'), ('Man', 'Man'), ('Odienné', 'Odienné'), ('San-Pédro', 'San-Pédro'), ('Sassandra', 'Sassandra'), ('Séguéla', 'Séguéla'), ('Soubré', 'Soubré'), ('Tiassalé', 'Tiassalé'), ('Toumodi', 'Toumodi'), ('Yamoussoukro', 'Yamoussoukro'), ('Zuénoula', 'Zuénoula')], max_length=100),
        ),
    ]
