from EventBus import suscribe
from events import *
from models.db import DB
from services.flightcontrol import *
from test_instances import create_test
from services.emisors import *

def suscribe_functions():
    suscribe(SecurityDone,check_luggage)
    suscribe(SecurityDone,check_arrive)
    suscribe(Arrive,user_arrive)
    suscribe(PostCheck,post_check_luggage)
    suscribe(PostCheck,post_check_arrive)

suscribe_functions()
user1, user2, user3, flight1, flight2, flight3, flight_card1, flight_card2, flight_card3, luggage1, luggage2, luggage3,arrive1,arrive2,arrive3,arrive4,arrive5,arrive6,arrive7,arrive8,arrive9 = create_test()


make_card(flight_card1)
make_card(flight_card2)
make_card(flight_card3)

flight_arrived(flight2)
flight_arrived(flight3)


user_checked(user2)
user_checked(user3)


print(DB[Luggage])

