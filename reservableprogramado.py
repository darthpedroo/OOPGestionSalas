from fecha import Fecha
from hora import Hora
from abc import ABC, abstractmethod

class Reservable(ABC):
    def __init__(self,nombre):
        self._nombre = nombre
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Reservable):
            return NotImplemented # OJITO CON ESTE
        return self._nombre == value._nombre
    
    def usuario_me_realizo_una_reserva(self):
        pass

class ReservableProgramado(Reservable):
    def __init__(self,nombre):
        self._nombre = nombre

    @abstractmethod
    def usuario_me_realizo_una_reserva(self,usuario:"Usuario", fecha_reserva:Fecha, hora_inicio_reserva: Hora, hora_fin_reserva: Hora):
        pass

class ReservableSinHora(Reservable):
    def __init__(self,nombre):
        self._nombre = nombre

    @abstractmethod
    def usuario_me_realizo_una_reserva(self,usuario:"Usuario", fecha_reserva:Fecha):
        pass
        

