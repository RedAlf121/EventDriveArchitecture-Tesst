from models.db import retrieve


def save_model(function,*args,**kwargs):
    def apply():
        model = function(*args,**kwargs)
        model.save()
        return model
    return apply

def update_state(model_type,flightcard,next_state):
    models:list=retrieve(type(model_type))
    for model in models:
        if model.flightCard.id != flightcard.id:
            continue
        model.states = next_state
        break

def state_wrapper(function,model_type,next_state,*args,**kwargs):
    def wrapper():
        flightcard = args[0]
        function(*args,kwargs)
        if model_type is tuple:
            for model in model_type:
                update_state(model,flightcard,next_state)
        else:
            update_state(model_type,flightcard,next_state)
    return wrapper