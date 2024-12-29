DB = {}

def retrieve(model_type):
    if model_type in DB.keys():
        return DB[model_type]
    else:
        raise Exception(f'{model_type} no esta en la base de datos')