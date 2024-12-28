# Servicios

Este modulo de servicios es con el fin de probar la arquitectura orientada a eventos. Desglocemos script por script.

## Generic
Contiene funciones genericas, closures en su mayoria. Esto debido a que muchas funciones del resto de modulos comparten la misma logica, por lo que es posible evitar repetir lo mismo.
- save_model: Para guardar los modelos ya que todos heredan de una misma clase(Model)

- state_wrapper: Para cambiar los estados esta tiene la funcion de englobar el como se cambian los estados. Casi que se puede prescindir del resto de funciones que tienen que ver con eso, pero se mantuvo para mejor legibilidad

## Create

Este script contiene las funciones para guardar los modelos, no se hicieron el resto de funciones del CRUD por no ser necesarios para la practica de la arquitectura. Estos usan un decorador llamado save_model que se encuentra en el script generics. Esto se hizo porque todos los modelos heredan de Model por lo que fue posible generalizar siendo solo necesario crear la instancia.

## FlightControl
Este script en su mayoria son las funciones que estarian suscritas a un evento. Estas usan el decorador @state_wrapper para evitar repetir codigo, aqui se mantiene para que se vea como el EventBus suscribe diferentes eventos a diferentes funciones. En los parametros del decorador esta que modelo utiliza(puede mandarse una tupla tambien) y a que estado cambia

## Emisors
Este script contiene las funciones que emiten un metodo:
- make_card: cuando se crea una carta y ya se esta listo para el vuelo
- flight_arrived: cuando un vuelo acaba de llegar a su destino
- user_checked: cuando un usuario pasa su chequeo luego de aterrizar