from models.concrete_models.states import ArriveStates
from models.db import retrieve
from models.model import Model


def save_model(function):
    def apply(*args,**kwargs):
        model = function(*args,**kwargs)
        model.save()
        return model
    return apply

def update_state(model_type,flightcard,next_state):
    models:list=retrieve(model_type)
    for model in models:
        if model.flightCard.id != flightcard.id:
            continue
        model.state = next_state
        break

def state_wrapper(model_type=Model,next_state=ArriveStates.NotChecked):
    def func(function):
        def wrapper(*args,**kwargs):
            flightcard = args[0]
            function(*args,**kwargs)
            if type(model_type) is tuple:
                for model in model_type:
                    update_state(model,flightcard,next_state)
            else:
                update_state(model_type,flightcard,next_state)
        return wrapper
    return func