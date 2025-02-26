from events import *
from models.concrete_models.arrives import Arrive
from models.concrete_models.luggage import Luggage
from models.concrete_models.states import ArriveStates
from services.generic import state_wrapper


@state_wrapper(model_type=Luggage,next_state=ArriveStates.Travelling)
def check_luggage(flightcard):
    pass

@state_wrapper(model_type=Arrive,next_state=ArriveStates.Travelling)
def check_arrive(flightcard):
    pass

@state_wrapper(model_type=(Luggage,Arrive),next_state=ArriveStates.NotPostChecked)
def user_arrive(flightcard):
    pass

@state_wrapper(model_type=Luggage,next_state=ArriveStates.Checked)
def post_check_luggage(flightcard):
    pass

@state_wrapper(model_type=Luggage,next_state=ArriveStates.Checked)
def post_check_arrive(flightcard):
    pass