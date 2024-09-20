class Hora:
    def __init__(self,hora) -> None:
        self._hora = hora
    
    def __eq__(self, other_hora: "Hora") -> bool:
        return self._hora == other_hora._hora