BUS = {}

def suscribe(event,service):
    if event in BUS:
        BUS[event].append(service)
    else:
        BUS[event] = [service]

def emit(event,*args,**kwargs):
    for service in BUS[event]:
        service(*args,**kwargs)