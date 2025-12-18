
from ninja import NinjaAPI
from .models import OilField, Well,  Sensor, ProductionReading, WellStatus, SensorType
from django.core.handlers.wsgi import WSGIRequest
from .schemas import OilfieldSchema, WellSchema, SensorSchema, ProductionReadingSchema
from typing import List, Optional
from datetime import date, datetime
from django.db.models import Avg, Sum, Max, Min

api = NinjaAPI()

# OilField endpoints

@api.post('oilfields')
def create_oilfield(request: WSGIRequest, name: str, location: str, operator_company: str, start_date: str = None):
    oil_field = OilField(
        name=name,
        location=location,
        operator_company=operator_company,
        start_date=start_date
    )
    oil_field.save()
    return f"Oil Field with id {oil_field.oil_field_id} has been created successfully!"

@api.get('oilfields', response=List[OilfieldSchema])
def list_oilfields(request: WSGIRequest, created_after: Optional[date] = None):
    oil_fields = OilField.objects.all()

    if created_after:
        oil_fields = oil_fields.filter(start_date__gt=created_after)
        
    return oil_fields

@api.get('oilfields/{oil_field_id}', response=OilfieldSchema)
def get_oilfield(request: WSGIRequest, oil_field_id: int):
    oil_field = OilField.objects.get(oil_field_id=oil_field_id)
    return oil_field

@api.put('oilfields/{oil_field_id}')
def update_oilfield(request: WSGIRequest, oil_field_id: int, name: str = None, location: str = None, operator_company: str = None, start_date: str = None):
    oil_field = OilField.objects.get(oil_field_id=oil_field_id)
    if name:
        oil_field.name = name
    if location:
        oil_field.location = location
    if operator_company:
        oil_field.operator_company = operator_company
    if start_date:
        oil_field.start_date = start_date
    oil_field.save()
    return f"Oil Field with id {oil_field.oil_field_id} has been updated successfully!"

@api.delete('oilfields/{oil_field_id}')
def delete_oilfield(request: WSGIRequest, oil_field_id: int):
    oil_field = OilField.objects.get(oil_field_id=oil_field_id)
    oil_field.delete()
    return f"Oil Field with id {oil_field_id} has been deleted successfully!"


# Well endpoints

@api.post('oilwell')
def create_oilwell(request, name: str, drill_date: str = None, depth_m: float = None, oil_field_id: int = None):
    well = Well(
        name=name,
        drill_date=drill_date,
        depth_m=depth_m,
        oil_field_id=oil_field_id
        )
    
    well.save()
    return f"Well with id {well.well_id} has been created successfully!"

@api.get('oilwells', response=List[WellSchema])
def list_oilwells(request: WSGIRequest, by_status: Optional[WellStatus] = None, active_sensors: Optional[bool] = None):
    wells = Well.objects.all()

    if by_status:
        wells = wells.filter(status=by_status)
    if active_sensors is not None:
        if active_sensors:
            wells = wells.filter(sensors__is_active=True).distinct()
        else:
            wells = wells.exclude(sensors__is_active=True).distinct()

    return wells

@api.get('oilwells/{well_id}', response=WellSchema)
def get_oilwell(request, well_id: int):
    well = Well.objects.get(well_id=well_id)
    return well

@api.put('oilwells/{well_id}')
def update_oilwell(request, well_id: int, name: str = None, drill_date: str = None, depth_m: float = None, status: WellStatus = None):
    well = Well.objects.get(well_id=well_id)
    if name:
        well.name = name
    if drill_date:
        well.drill_date = drill_date
    if depth_m:
        well.depth_m = depth_m
    if status:
        well.status = status
    well.save()
    return f"Well with id {well.well_id} has been updated successfully!"

@api.delete('oilwells/{well_id}')
def delete_oilwell(request, well_id: int):
    well = Well.objects.get(well_id=well_id)
    well.delete()
    return f"Well with id {well_id} has been deleted successfully!"

# Sensor endpoints

@api.post('sensors')
def create_sensor(request, sensor_type: SensorType, install_date: str = None, is_active: bool = True, well_id: int = None):
    sensor = Sensor(
        sensor_type=sensor_type,
        install_date=install_date,
        is_active=is_active,
        well_id=well_id
        )   
    
    sensor.save()
    return f"Sensor with id {sensor.sensor_id} has been created successfully!"

@api.get('sensors', response=List[SensorSchema])
def list_sensors(request: WSGIRequest):
    sensors = Sensor.objects.all()
    return sensors

@api.get('sensors/{sensor_id}', response=SensorSchema)
def get_sensor(request: WSGIRequest, sensor_id: int):
    sensor = Sensor.objects.get(sensor_id=sensor_id)
    return sensor

@api.put('sensors/{sensor_id}')
def update_sensor(request: WSGIRequest, sensor_id: int, sensor_type: SensorType = None, install_date: str = None, is_active: bool = None):
    sensor = Sensor.objects.get(sensor_id=sensor_id)
    if sensor_type:
        sensor.sensor_type = sensor_type
    if install_date:
        sensor.install_date = install_date
    if is_active is not None:
        sensor.is_active = is_active
    sensor.save()
    return f"Sensor with id {sensor.sensor_id} has been updated successfully!"

@api.delete('sensors/{sensor_id}')
def delete_sensor(request: WSGIRequest, sensor_id: int):
    sensor = Sensor.objects.get(sensor_id=sensor_id)
    sensor.delete()
    return f"Sensor with id {sensor_id} has been deleted successfully!"

# ProductionReading endpoints

@api.post('readings')
def create_production_reading(request, sensor_id: int, value: float, unit: str):
    reading = ProductionReading(
        sensor_id=sensor_id,
        value=value,
        unit=unit
        )
    
    reading.save()
    return f"Production Reading with id {reading.reading_id} has been created successfully!"

@api.get('readings', response=List[ProductionReadingSchema])
def list_production_readings(request: WSGIRequest):
    readings = ProductionReading.objects.all()
    return readings

@api.get('readings/{reading_id}', response=ProductionReadingSchema)
def get_production_reading(request: WSGIRequest, reading_id: int):
    reading = ProductionReading.objects.get(reading_id=reading_id)
    return reading

@api.put('readings/{reading_id}')
def update_production_reading(request: WSGIRequest, reading_id: int, value: float = None, unit: str = None):
    reading = ProductionReading.objects.get(reading_id=reading_id)
    if value:
        reading.value = value
    if unit:
        reading.unit = unit
    reading.save()
    return f"Production Reading with id {reading.reading_id} has been updated successfully!"

@api.delete('readings/{reading_id}')
def delete_production_reading(request: WSGIRequest, reading_id: int):
    reading = ProductionReading.objects.get(reading_id=reading_id)
    reading.delete()
    return f"Production Reading with id {reading_id} has been deleted successfully!"


# New task endpoints

@api.get('average_reading_for_sensor/{sensor_id}', response=float)
def average_reading_for_sensor(request: WSGIRequest, sensor_id: int):
    readings = ProductionReading.objects.filter(sensor_id=sensor_id)
    if not readings.exists():
        return 0.0
    total = sum(reading.value for reading in readings)
    average = total / readings.count()
    return average

@api.get('oilfields/{oilfield_id}/wells', response=List[WellSchema])
def get_wells_for_oilfield(request: WSGIRequest, oilfield_id: int):
    wells = Well.objects.filter(oil_field_id=oilfield_id)
    return wells

@api.get('wells/{well_id}/sensors', response=List[SensorSchema])
def get_sensors_for_well(request: WSGIRequest, well_id: int):
    sensors = Sensor.objects.filter(well_id=well_id)
    return sensors

@api.get('sensors/{sensor_id}/readings', response=List[ProductionReadingSchema])
def get_readings_for_sensor(request: WSGIRequest, sensor_id: int):
    readings = ProductionReading.objects.filter(sensor_id=sensor_id)
    return readings

@api.get('well_production_summary/{well_id}')
def well_production_summary(request: WSGIRequest, well_id: int):
    readings = ProductionReading.objects.filter(sensor__well_id=well_id)
    summary = readings.aggregate(
        total=Sum('value'),
        average=Avg('value'),
        maximum=Max('value'),
        minimum=Min('value')
    )
    return summary

@api.get('oilfields_with_no_wells', response=List[OilfieldSchema])
def oilfields_with_no_wells(request: WSGIRequest):
    oilfields = OilField.objects.filter(wells__isnull=True)
    return oilfields