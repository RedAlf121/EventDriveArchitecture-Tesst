

from dataclasses import field
from models.concrete_models.flightcard import FlightCard
from models.concrete_models.states import ArriveStates
from models.model import Model



class Arrive(Model):
    flightCard: FlightCard
    state: ArriveStates = field(repr=False,default=ArriveStates.NotChecked)
