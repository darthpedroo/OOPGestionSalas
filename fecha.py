from helpers import is_input_greater_than_zero
from exceptions import NumeroMenorAZero

class Fecha:
    def __init__(self, ano:"Ano",mes:"Mes",dia:"Dia") -> None:
        self._ano = ano
        self._mes = mes
        self._dia = dia

    def __eq__(self, otra_fecha: "Fecha") -> bool:
        if not isinstance(otra_fecha, Fecha):
            return NotImplemented # OJITO CON ESTE
        return self._ano == otra_fecha._ano and self._mes == otra_fecha._mes and self._dia == otra_fecha._dia

class Ano:
    def __init__(self, ano:int) -> None:
        if not is_input_greater_than_zero(ano):
            raise NumeroMenorAZero
        self._ano = ano

    def __eq__(self,otro_ano:"Ano"):
        return self._ano == otro_ano._ano


class Mes:
    def __init__(self, mes) -> None:
        if not is_input_greater_than_zero(mes):
            raise NumeroMenorAZero
        self._mes = mes
    
    def __eq__(self,otro_mes:"Mes"):
        return self._mes == otro_mes._mes

class Dia:
    def __init__(self, dia) -> None:
        if not is_input_greater_than_zero(dia):
            raise NumeroMenorAZero
        self._dia = dia
    
    def __eq__(self, otro_dia: "Dia"):
        return self._dia == otro_dia._dia
     

        