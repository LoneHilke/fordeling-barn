from django.db import models

# Create your models here.
class Barn(models.Model):
    navn = models.CharField(max_length=50)
    klasse = models.ManyToManyField('Klasse', related_name='item')
    niveau = models.Choices()
    klas_trin = models.CharField(max_length=10)

class Personale(models.Model):
    navn = models.CharField(max_length=100)
    klasse = models.ManyToManyField('Klasse', related_name='item')
    stilling = models.CharField(max_length=50)
    timer = models.CharField(max_length=10)
