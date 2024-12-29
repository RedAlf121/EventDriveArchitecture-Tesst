from EventBus import emit
from events import Arrive, PostCheck, SecurityDone
from models.concrete_models.flight import Flight
from models.concrete_models.flightcard import FlightCard
from models.concrete_models.user import User
from models.db import retrieve
from services.create import create_flight_card

def update_flightcards(flight):
    flightcards = retrieve(FlightCard)
    for flightcard in flightcards:
        if flightcard.flight.id == flight.id:
            emit(Arrive,flightcard)

def update_user_checked(user):
    flightcards = retrieve(FlightCard)
    for flightcard in flightcards:
        if flightcard.user.id == user.id:
            emit(PostCheck,flightcard)

def flight_arrived(flight):
    flights = retrieve(Flight)
    for flight_item in flights:
        if flight.id == flight_item.id:
            update_flightcards(flight)

def user_checked(user):
    users = retrieve(User)
    for user_item in users:
        if user.id == user_item.id:
            update_user_checked(user)


def make_card(flightcard):
    if flightcard:
        emit(SecurityDone,flightcard)
    else:
        raise Exception('Error al crear la tarjeta')