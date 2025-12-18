from ninja import Schema
import datetime

class OilfieldSchema(Schema):
    oil_field_id: int
    name: str
    location: str
    operator_company: str
    start_date: datetime.date | None = None

class WellSchema(Schema):
    well_id: int
    name: str
    drill_date: datetime.date | None = None
    depth_m: float | None = None
    status: str
    oil_field_id: int

class SensorSchema(Schema):
    sensor_id: int
    sensor_type: str
    install_date: datetime.date | None = None
    is_active: bool
    well_id: int

class ProductionReadingSchema(Schema):
    reading_id: int
    sensor_id: int
    timestamp: datetime.datetime
    value: float
    unit: str