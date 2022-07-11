from django.db import models
from django.db.models import Model

# Create your models here.

# class Ship(Model):
#     ship_name = models.CharField('ship_name', max_length=100)
#     deadweight = models.IntegerField('deadweight')
#     built = models.DateField('built', max_length=4)
#     ship_date = models.DateField('ship_date')
#     ship_port = models.CharField('ship_port', max_length=50, null=True, blank=True)


class AaShip(models.Model):
    ship_name = models.CharField(primary_key=True, max_length=100)
    deadweight = models.IntegerField(blank=True, null=True)
    built = models.DateField(blank=True, null=True)
    loa = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    grain = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    beam = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    bale = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    speed = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    consumption = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    eco_speed = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    eco_cons = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    gear = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    ship_date = models.DateField(blank=True, null=True)
    ship_indate = models.DateField(blank=True, null=True)
    ship_broker = models.CharField(max_length=50, blank=True, null=True)
    ship_port = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aa_ship'
