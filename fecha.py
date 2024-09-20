class Fecha:
    def __init__(self, dia: int) -> None:
        self._dia = dia

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Fecha):
            return NotImplemented # OJITO CON ESTE
        return self._dia == value._dia

    