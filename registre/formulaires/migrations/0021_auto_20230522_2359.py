# Generated by Django 3.1.14 on 2023-05-22 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulaires', '0020_professionnal_metier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professionnal',
            old_name='scol',
            new_name='person',
        ),
        migrations.RenameField(
            model_name='scolaire',
            old_name='esprit',
            new_name='person',
        ),
    ]
