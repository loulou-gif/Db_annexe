# Generated by Django 3.1.14 on 2023-05-22 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulaires', '0019_auto_20230522_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='professionnal',
            name='metier',
            field=models.CharField(max_length=80, null=True),
        ),
    ]