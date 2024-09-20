from reservamanager import SingletonReservaManager
from usuario import Usuario
from sala import Sala
from fecha import Fecha
from hora import Hora
from reserva import Reserva
from exceptions import ReservableYaReservado, NoExisteLaReserva, ReservaPerteneceOtroUsuario
import unittest

class TestReserva(unittest.TestCase):

    def setUp(self):
        self._reserva_manager = SingletonReservaManager()
        self._usuario_porky = Usuario("Porky")
        self._sala_papu = Sala(nombre="Salita" ,capacidad_maxima=10)
        

    def test_01_test_reservar_sala(self):
        print("test_01_test_reservar_sala")
        fecha_reserva = Fecha(1)
        hora_reserva = Hora(1)
        self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva,hora_reserva,hora_reserva)

    def test_02_reservar_sala_que_ya_se_reservo_en_un_horario_determinado_tira_errror(self):
        print("test_02_reservar_sala_que_ya_se_reservo_tira_errror")
        fecha_reserva = Fecha(14)
        fecha_reserva_2 = Fecha(14)
        hora_reserva = Hora(2)
        
        self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva_2,hora_reserva,hora_reserva)

        with self.assertRaises(ReservableYaReservado):
            self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva_2,hora_reserva,hora_reserva)
            self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva_2,hora_reserva,hora_reserva)
  
    def test_03_borrar_reserva(self):
        fecha_reserva_2 = Fecha(14)
        hora_reserva = Hora(1)
        reserva = Reserva(self._sala_papu, self._usuario_porky,fecha_reserva_2,hora_reserva,hora_reserva)
        self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva_2,hora_reserva,hora_reserva)
        cantidad_reservas_antes = len(self._reserva_manager.get_reservas_activas_dia_especifico(fecha_reserva_2))
        self._usuario_porky.cancelar_reserva_programada(reserva)
        cantidad_reservas_despues = len(self._reserva_manager.get_reservas_activas_dia_especifico(fecha_reserva_2))
        self.assertEqual(cantidad_reservas_antes-1 , cantidad_reservas_despues)

    def test_04_borrar_reserva_que_no_existe_tira_error(self):
        fecha_reserva_2 = Fecha(14)
        hora_reserva = Hora(1)
        reserva = Reserva(self._sala_papu, self._usuario_porky,fecha_reserva_2,hora_reserva,hora_reserva)
        with self.assertRaises(NoExisteLaReserva):
            self._usuario_porky.cancelar_reserva_programada(reserva)
    
    def test_05_borrar_reserva_de_otra_persona_tira_error(self):
        fecha_reserva_2 = Fecha(14)
        hora_reserva = Hora(1)
        self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva_2,hora_reserva,hora_reserva)
        reserva_de_porky = Reserva(self._sala_papu, self._usuario_porky,fecha_reserva_2,hora_reserva,hora_reserva)
        
        usuario_no_dueño_de_la_reserva = Usuario("Ronnie Coleman")
        with self.assertRaises(ReservaPerteneceOtroUsuario):
            usuario_no_dueño_de_la_reserva.cancelar_reserva_programada(reserva_de_porky)

    def test_06_obtener_reservas_de_un_dia_especificO(self):
        pass
    


if __name__ == "__main__":
    unittest.main()
