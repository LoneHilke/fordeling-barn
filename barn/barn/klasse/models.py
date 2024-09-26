from django.db import models

# Create your models here.
class Barn(models.Model):
    navn = models.CharField(max_length=50)
    klasse = models.ManyToManyField('Klasse', related_name='item')
    niveau = models.Choices()

class Personale(models.Model):
    navn = models.CharField(max_length=100)
    klasse = models.ManyToManyField('Klasse', related_name='item')
    stilling = models.CharField(max_length=50)
    