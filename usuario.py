from reservableprogramado import ReservableProgramado, ReservableSinHora,Reservable
from reservamanager import SingletonReservaManager
from reserva import Reserva
from fecha import Fecha
from tiempo import Tiempo

class Usuario:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre

    def __eq__(self, value: "Usuario") -> bool:
        if not isinstance(value, Usuario):
            raise NotImplementedError
        return self.__nombre == value.__nombre
    

    #PROBLEMA ! SI QUIERO REALIZAR UN RESERVABLE NO PROGRAMADO VOY A TENER MAS FUNCIONES
    #pregunarle al prof 
    def realizar_reserva_programada(self, reservable_programado: ReservableProgramado, fecha_reserva:Fecha, hora_inicio_reserva: Tiempo, hora_fin_reserva: Tiempo):
        return reservable_programado.usuario_me_realizo_una_reserva(self,fecha_reserva,hora_inicio_reserva,hora_fin_reserva)

    def cancelar_reserva_programada(self,reserva: Reserva):
        reserva_manager = SingletonReservaManager()
        reserva_manager.cancelar_reserva(self, reserva)



        
    

