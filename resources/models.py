from django.db import models
from datetime import date, datetime

class WellStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    SHUT_IN = "shut-in", "Shut-In"
    ABANDONED = "abandoned", "Abandoned"

class SensorType(models.TextChoices):
    PRESSURE = "pressure", "Pressure"
    TEMPERATURE = "temperature", "Temperature"
    FLOW_RATE = "flow_rate", "Flow Rate"



class OilField(models.Model):
    oil_field_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=512)
    operator_company = models.CharField(max_length=256)
    start_date = models.DateField(blank=True, null=True)


class Well(models.Model):
    well_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256) 
    drill_date = models.DateField(blank=True, null=True)
    depth_m = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=WellStatus.choices, default=WellStatus.ACTIVE)
    oil_field = models.ForeignKey(OilField, on_delete=models.CASCADE, related_name="wells")


class Sensor(models.Model):
    sensor_id = models.BigAutoField(primary_key=True)
    sensor_type = models.CharField(max_length=20, choices=SensorType.choices)
    install_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    well = models.ForeignKey(Well, on_delete=models.CASCADE, related_name="sensors")


class ProductionReading(models.Model):

    reading_id = models.BigAutoField(primary_key=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="readings")
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
    unit = models.CharField(max_length=32)