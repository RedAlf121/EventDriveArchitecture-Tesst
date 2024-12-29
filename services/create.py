from models.concrete_models.arrives import Arrive
from models.concrete_models.flight import Flight
from models.concrete_models.flightcard import FlightCard
from models.concrete_models.luggage import Luggage
from models.concrete_models.user import User
from services.generic import save_model

@save_model
def create_user(username, email):
    return User(username=username, email=email)

@save_model
def create_flight(airline, flight_from, flight_to, time_from, time_to):
    return Flight(airline=airline, flight_from=flight_from, flight_to=flight_to, time_from=time_from, time_to=time_to)

@save_model
def create_flight_card(user, flight):
    return FlightCard(user=user, flight=flight)

@save_model
def create_luggage(flightcard,weight):
    return Luggage(flightCard=flightcard,weight=weight)

@save_model
def create_arrive(flightcard):
    return Arrive(flightCard=flightcard)