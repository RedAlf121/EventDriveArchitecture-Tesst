
# Ejercicio: 
## Sistema de gestión de vuelos en un aeropuerto

## Contexto:
Sistema para gestionar los vuelos en un aeropuerto. El sistema debe manejar diferentes procesos relacionados con la operación de los vuelos, desde el momento en que se programa un vuelo hasta que los pasajeros desembarcan y se recogen las maletas.

## Aclaracion:
Realizado en python Vanilla. Por lo que se va a simular el EventBus y la base de datos.

## Solucion
Para la solucion de este ejercicio primero se tuvo que identificar los modelos, eventos y servicios que fueran necesarios. A continuacion estan los enlaces a cada modulo con su explicacion de como fueron identificados

[Eventos](./events/Readme.md)
[Modelos](./models/Readme.md)
[Servicios](./services/Readme.md)

## EventBus:
EventBus es un patron de diseño inspirado en el patron Observer. En el cual se va a tener varias funciones suscritas a un evento, cuando este evento es emitido, las funciones suscritas al evento se ejecutan. Existen tecnologias como Kafka y RabbitMQ que aplican este patron a nivel de infraestructura.
En este proyecto se aplica utilizando un diccionario que revisa si ya esa funcion esta suscrita; si es el caso lo agrega en la lista de suscriptores del evento, sino la crea con la lista con la funcion.