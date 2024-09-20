from reservamanager import SingletonReservaManager
from usuario import Usuario
from sala import Sala
from fecha import Fecha
from hora import Hora
from reserva import Reserva
from exceptions import ReservableYaReservado
import unittest

class TestReserva(unittest.TestCase):

    def setUp(self):
        self._reserva_manager = SingletonReservaManager()
        self._usuario_porky = Usuario("Porky")
        self._sala_papu = Sala(nombre="Salita" ,capacidad_maxima=10)
        


    def test_02_reservar_sala_que_ya_se_reservo_tira_errror(self):
        print("test_02_reservar_sala_que_ya_se_reservo_tira_errror")
        fecha_reserva = Fecha(14)
        fecha_reserva_2 = Fecha(14)
        hora_reserva = Hora(2)
        
        self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva_2,hora_reserva,hora_reserva)
        print("poop")
        print(self._reserva_manager.get_reservas_activas_dia_especifico(fecha_reserva))

        with self.assertRaises(ReservableYaReservado):
            self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva_2,hora_reserva,hora_reserva)
            print("wee")
            print(self._reserva_manager.get_reservas_activas_dia_especifico(fecha_reserva))
            self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva_2,hora_reserva,hora_reserva)
  

    


    
if __name__ == "__main__":
    unittest.main()
