from django.db import models
from django.db.models import Model

from django.db import models
from django_google_maps import fields as map_fields

# Create your models here.

class AaPort(models.Model):
    port = models.CharField(primary_key=True, max_length=100)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aa_port'


class AaCargo(models.Model):
    cargo_name = models.CharField(max_length=100)
    cargo_quantity = models.IntegerField(blank=True, null=True)
    cargo_loadingport = models.CharField(max_length=100, blank=True, null=True)
    cargo_dischargingport = models.CharField(max_length=100, blank=True, null=True)
    cargo_loadingrate = models.CharField(max_length=100, blank=True, null=True)
    cargo_dischargingrate = models.CharField(max_length=100, blank=True, null=True)
    cargo_laydate = models.DateField(blank=True, null=True)
    cargo_canceldate = models.DateField(blank=True, null=True)
    cargo_indate = models.DateField(blank=True, null=True)
    cargo_comm = models.FloatField(blank=True, null=True)
    cargo_broker = models.CharField(max_length=100, blank=True, null=True)
    cargo_charterers = models.CharField(max_length=100, blank=True, null=True)
    cargo_seq = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'aa_cargo'


class AaCargo(models.Model):
    cargo_name = models.CharField(max_length=100)
    cargo_quantity =  models.IntegerField(blank=True, null=True)
    cargo_loadingport = models.CharField(max_length=100, blank=True, null=True)
    cargo_dischargingport = models.CharField(max_length=100, blank=True, null=True)
    cargo_loadingrate = models.CharField(max_length=100, blank=True, null=True)
    cargo_dischargingrate = models.CharField(max_length=100, blank=True, null=True)
    cargo_laydate = models.DateField(blank=True, null=True)
    cargo_canceldate = models.DateField(blank=True, null=True)
    cargo_indate = models.DateField(blank=True, null=True)
    cargo_comm = models.FloatField(blank=True, null=True)
    cargo_broker = models.CharField(max_length=100, blank=True, null=True)
    cargo_charterers = models.CharField(max_length=100, blank=True, null=True)
    cargo_seq = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'aa_cargo'


class AaOrder(models.Model):
    order_cargo = models.CharField(max_length=100)
    order_quantity =  models.IntegerField(blank=True, null=True)
    order_loading_area = models.CharField(max_length=100, blank=True, null=True)
    order_discharging_area = models.CharField(max_length=100, blank=True, null=True)
    order_laydate = models.DateField(blank=True, null=True)
    order_canceldate = models.DateField(blank=True, null=True)
    order_comm = models.FloatField(blank=True, null=True)
    order_broker = models.CharField(max_length=100, blank=True, null=True)
    order_indate = models.DateField(blank=True, null=True)
    order_charterers = models.CharField(max_length=100, blank=True, null=True)
    order_seq = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'aa_order'

