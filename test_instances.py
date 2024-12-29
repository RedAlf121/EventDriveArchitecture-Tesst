from services.create import *
def create_test():
    user1 = create_user("alice", "alice@example\.com")
    user2 = create_user("bob", "bob@example\.com")
    user3 = create_user("charlie", "charlie@example\.com")

# Creando vuelos de prueba
    flight1 = create_flight("Airline A", "New York", "Los Angeles", "2024-12-28T10:00:00", "2024-12-28T13:00:00")
    flight2 = create_flight("Airline B", "Chicago", "Miami", "2024-12-29T14:00:00", "2024-12-29T17:00:00")
    flight3 = create_flight("Airline C", "San Francisco", "Tokyo", "2024-12-30T08:00:00", "2024-12-31T08:00:00")

# Creando tarjetas de vuelo de prueba
    flight_card1 = create_flight_card(user1, flight1)
    flight_card2 = create_flight_card(user2, flight2)
    flight_card3 = create_flight_card(user3, flight3)

# Creando equipajes de prueba
    luggage1 = create_luggage(flight_card1,20)  # Peso en kg
    luggage2 = create_luggage(flight_card2,25)
    luggage3 = create_luggage(flight_card3,15)

    arrive1 = create_arrive(flight_card1)
    arrive2 = create_arrive(flight_card1)
    arrive3 = create_arrive(flight_card1)
    arrive4 = create_arrive(flight_card1)
    arrive5 = create_arrive(flight_card2)
    arrive6 = create_arrive(flight_card2)
    arrive7 = create_arrive(flight_card2)
    arrive8 = create_arrive(flight_card3)
    arrive9 = create_arrive(flight_card3)
    return user1,user2,user3,flight1,flight2,flight3,flight_card1,flight_card2,flight_card3,luggage1,luggage2,luggage3,arrive1,arrive2,arrive3,arrive4,arrive5,arrive6,arrive7,arrive8,arrive9
