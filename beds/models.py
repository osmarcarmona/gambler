# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

#je pense que usuario deja gerer danse  la base comment ajouter des entrees ?
class Equipo(models.Model):
    nombreEquipo = models.TextField()

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('beds:apuesta_detail', kwargs={'pk': self.pk})


class Resultado(models.Model):
    #partido = models.ForeignKey(Partido)
    golLocal = models.IntegerField()
    golVisitante = models.IntegerField()

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('beds:apuesta_detail', kwargs={'pk': self.pk})

class Partido(models.Model):
    jornada = models.IntegerField()
    equipoLocal = models.ForeignKey(Equipo)
    equipoVisitante = models.ForeignKey(Equipo)
    fecha = models.DateField(default=date.today)
    resultado = models.ForeignKey(Resultado)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('beds:apuesta_detail', kwargs={'pk': self.pk})

class Apuesta(models.Model):
    user = models.ForeignKey(User, default=1)
    partido = models.ForeignKey(Partido)
    apuesta = models.DecimalField(max_digits=11, decimal_places=2)
    cuota = models.DecimalField(max_digits=3, decimal_places=2)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('beds:apuesta_detail', kwargs={'pkr': self.apuesta.pk, 'pk': self.pk})

    class Meta:
        abstract = True

#class ApuestaReview(Review):
    #apuesta = models.ForeignKey(Apuesta)