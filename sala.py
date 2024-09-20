from fecha import Fecha
from tiempo import Tiempo
from usuario import Usuario
from reservableprogramado import ReservableProgramado
from reservamanager import SingletonReservaManager

class Sala(ReservableProgramado): #UNA SALA ES UNA SALA. UNA SALA NO DEBE TENER HORARIO. 
    def __init__(self,nombre:str, capacidad_maxima:int):
        self._nombre = nombre #Hacer un super de esto
        self._capacidad_maxima = capacidad_maxima

    def usuario_me_realizo_una_reserva(self,usuario:Usuario, fecha_reserva:Fecha, hora_inicio_reserva: Tiempo, hora_fin_reserva: Tiempo):
        reserva_manager = SingletonReservaManager()
        reserva_manager.crear_reserva(self,
                                      usuario,fecha_reserva,hora_inicio_reserva,hora_fin_reserva)
        

