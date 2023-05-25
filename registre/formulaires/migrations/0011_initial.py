# Generated by Django 4.2 on 2023-05-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formulaires', '0010_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('prenoms', models.CharField(default=None, max_length=100)),
                ('email', models.EmailField(max_length=80)),
                ('numero', models.CharField(max_length=20)),
                ('date', models.DateField(default=None, null=True)),
                ('location', models.CharField(max_length=100)),
                ('commune', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=10)),
            ],
        ),
    ]
