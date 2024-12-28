from datetime import date
from models.concrete_models.user import User
from models.model import Model

class Flight(Model):
    airline: str
    flight_from: str
    flight_to: str
    time_from: date
    time_to: date