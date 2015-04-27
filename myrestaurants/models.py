# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

//je pense que usuario deja gerer danse  la base comment ajouter des entrees ?

class Apuestas(models.Model):
    //idApuesta = models.IntegerField(primary_key=True)
    idUsuario = models.ForeignKey(Usuario)
    idPartido = models.ForeignKey(Partido)
    apuesta = models.DecimalField(max_digits=11, decimal_places=2)
    cuota = models.DecimalField(max_digits=3, decimal_places=2)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('myrestaurants:dish_detail', kwargs={'pkr': self.restaurant.pk, 'pk': self.pk})

class Partido(models.Model):
    //idPartido = models.IntegerField(primary_key=True)
    idJornada = models.IntegerField()
    idEquipoLocal = models.ForeignKey(Equipo)
    idEquipoVist = models.ForeignKey(Equipo)
    fecha = models.DateField(default=date.today)
    idResultado = models.ForeignKey(Resultado)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('myrestaurants:restaurant_detail', kwargs={'pk': self.pk})

class Resultado(models.Model):
    //idResultado = models.IntegerField(primary_key=True)
    idPartido = models.ForeignKey(Partido)
    golLocal = models.IntegerField()
    golVisitante = models.IntegerField()

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('myrestaurants:restaurant_detail', kwargs={'pk': self.pk})

class Equipo(models.Model):
    //idREquipo = models.IntegerField(primary_key=True)
    nombreEquipo = models.TextField()


    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('myrestaurants:restaurant_detail', kwargs={'pk': self.pk})

    class Meta:
        abstract = True

class ApuestasReview(Review):
    restaurant = models.ForeignKey(Restaurant)