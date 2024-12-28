
from models.concrete_models.flight import Flight
from models.concrete_models.user import User
from models.model import Model


class FlightCard(Model):
    user: User
    flight: Flight