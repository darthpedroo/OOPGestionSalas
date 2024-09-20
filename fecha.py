from helpers import is_input_greater_than_zero
from exceptions import NumeroMenorAZero

class Fecha:
    def __init__(self, ano:"Ano",mes:"Mes",dia:"Dia") -> None:
        self._ano = ano
        self._mes = mes
        self._dia = dia

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Fecha):
            return NotImplemented # OJITO CON ESTE
        return self._dia == value._dia

class Ano:
    def __init__(self, ano:int) -> None:
        if not is_input_greater_than_zero(ano):
            raise NumeroMenorAZero
        self._ano = ano
class Mes:
    def __init__(self, mes) -> None:
        if not is_input_greater_than_zero(mes):
            raise NumeroMenorAZero
        self._mes = mes    

class Dia:
    def __init__(self, dia) -> None:
        if not is_input_greater_than_zero(dia):
            raise NumeroMenorAZero
        self._dia = dia

        