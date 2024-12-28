BUS = {}

def suscribe(event,service):
    event_type = type(event)
    if event in BUS:
        BUS[event_type].append(service)
    else:
        BUS[event_type] = [service]

def emit(event,*args,**kwargs):
    for service in BUS[event]:
        service(*args,**kwargs)