from django.db import models

# Create your models here.
class Barn(models.Model):
    navn = models.CharField(max_length=50)
    klasse = models.ManyToManyField('Klasse', related_name='item')
    #niveau = models.Choices(value= [(1,1),(2,2),(3,3)] )
    klas_trin = models.CharField(max_length=10)

    def __str__(self):
        return self.navn

class Personale(models.Model):
    navn = models.CharField(max_length=100)
    klasse = models.ManyToManyField('Klasse')
    stilling = models.CharField(max_length=50)
    timer = models.CharField(max_length=10)

    def __str__(self):
        return self.navn

class Klasse(models.Model):
    klasse = models.CharField(max_length=25)

    def __str__(self):
        return self.klasse
