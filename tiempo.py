from helpers import is_input_greater_than_zero
from exceptions import NumeroMenorAZero

class Tiempo():
    def __init__(self,hora:"Hora",minuto:"Minuto",segundo:"Segundo") -> None:
        self._hora = hora
        self._minuto = minuto
        self._segundo = segundo
    
    def __eq__(self, otro_tiempo: "Tiempo"):
        return self._hora == otro_tiempo._hora and self._minuto == otro_tiempo._minuto and self._segundo == otro_tiempo._segundo

    def __gt__(self, otro_tiempo: "Tiempo"):
        if self._hora > otro_tiempo._hora:
            return True
        if self._minuto > otro_tiempo._minuto:
            return True
        if self._segundo > otro_tiempo._segundo:
            return True     
        return False
    
    def __ge__(self, otro_tiempo: "Tiempo"):
        if self._hora > otro_tiempo._hora:
            return True
        if self._minuto > otro_tiempo._minuto:
            return True
        if self._segundo > otro_tiempo._segundo:
            return True     
        return False

class Hora:
    def __init__(self,hora) -> None:
        if not is_input_greater_than_zero(hora):
            raise NumeroMenorAZero
        self._hora = hora
    
    def __eq__(self, other_hora: "Hora") -> bool:
        return self._hora == other_hora._hora

    def __gt__(self, otra_hora: "Hora"):
        return self._hora > otra_hora._hora

    def __ge__(self, otra_hora: "Hora"):
        return self._hora >= otra_hora._hora
    
class Minuto:
    def __init__(self,minuto) -> None:
        if not is_input_greater_than_zero(minuto):
            raise NumeroMenorAZero
        self._minuto = minuto
    
    def __eq__(self, otro_minuto: "Minuto") -> bool:
        return self._minuto == otro_minuto._minuto

    def __gt__(self, otro_minuto:"Minuto"):
        return self._minuto > otro_minuto._minuto

    def __ge__(self, otro_minuto:"Minuto"):
        return self._minuto >= otro_minuto._minuto

class Segundo:
    def __init__(self,segundo) -> None:
        if not is_input_greater_than_zero(segundo):
            raise NumeroMenorAZero
        self._segundo = segundo
    
    def __eq__(self, otro_segundo: "Segundo") -> bool:
        return self._segundo == otro_segundo._segundo
    
    def __gt__(self, otro_segundo: "Segundo"):
        return self._segundo > otro_segundo._segundo
    
    def __ge__(self, otro_segundo: "Segundo"):
        return self._segundo >= otro_segundo._segundo
