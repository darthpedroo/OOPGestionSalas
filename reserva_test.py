from reservamanager import SingletonReservaManager
from usuario import Usuario
from sala import Sala
from fecha import Fecha, Ano, Mes,Dia
from tiempo import Tiempo, Hora,Minuto,Segundo
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
        
        ano_reserva = Ano(2024)
        mes_reserva = Mes(9)
        dia_reserva = Dia(12)
        fecha_reserva = Fecha(ano_reserva, mes_reserva, dia_reserva)

        hora_reserva = Hora(3)
        minuto_reserva = Minuto(0)
        segundo_reserva = Segundo(0)
        horario_inicio_reserva = Tiempo(hora_reserva,minuto_reserva,segundo_reserva)

        hora2_reserva = Hora(5)
        minuto2_reserva = Minuto(0)
        segundo2_reserva = Segundo(0)
        horario_fin_reserva = Tiempo(hora2_reserva,minuto2_reserva,segundo2_reserva)
        
        self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva,horario_inicio_reserva,horario_fin_reserva)

    def test_02_reservar_sala_que_ya_se_reservo_en_un_horario_determinado_tira_errror(self):
        print("test_02_reservar_sala_que_ya_se_reservo_tira_errror")
        ano_reserva = Ano(2024)
        mes_reserva = Mes(9)
        dia_reserva = Dia(12)
        fecha_reserva = Fecha(ano_reserva, mes_reserva, dia_reserva)
        hora_reserva = Hora(1)
        minuto_reserva = Minuto(0)
        segundo_reserva = Segundo(0)
        horario_inicio_reserva = Tiempo(hora_reserva,minuto_reserva,segundo_reserva)

        hora2_reserva = Hora(2)
        minuto2_reserva = Minuto(0)
        segundo2_reserva = Segundo(0)
        horario_fin_reserva = Tiempo(hora2_reserva,minuto2_reserva,segundo2_reserva)
        
        self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva,horario_inicio_reserva,horario_fin_reserva)
        print(self._reserva_manager._todas_las_reservas)
        with self.assertRaises(ReservableYaReservado):
            self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva,horario_inicio_reserva,horario_fin_reserva)
            self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva,horario_inicio_reserva,horario_fin_reserva)
            print(self._reserva_manager._todas_las_reservas)

    def test_03_borrar_reserva(self):
        ano_reserva = Ano(2024)
        mes_reserva = Mes(9)
        dia_reserva = Dia(12)
        fecha_reserva = Fecha(ano_reserva, mes_reserva, dia_reserva)
        hora_reserva = Hora(10)
        minuto_reserva = Minuto(0)
        segundo_reserva = Segundo(0)
        horario_inicio_reserva = Tiempo(hora_reserva,minuto_reserva,segundo_reserva)
        hora2_reserva = Hora(11)
        minuto2_reserva = Minuto(0)
        segundo2_reserva = Segundo(0)
        horario_fin_reserva = Tiempo(hora2_reserva,minuto2_reserva,segundo2_reserva)

        reserva = Reserva(self._sala_papu, self._usuario_porky,fecha_reserva,horario_inicio_reserva,horario_fin_reserva)
        self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva,horario_inicio_reserva,horario_fin_reserva)
        cantidad_reservas_antes = len(self._reserva_manager.get_reservas_activas_dia_especifico(fecha_reserva))
        self._usuario_porky.cancelar_reserva_programada(reserva)
        cantidad_reservas_despues = len(self._reserva_manager.get_reservas_activas_dia_especifico(fecha_reserva))
        self.assertEqual(cantidad_reservas_antes-1 , cantidad_reservas_despues)
    
    def test_04_borrar_reserva_que_no_existe_tira_error(self):
        ano_reserva = Ano(2024)
        mes_reserva = Mes(9)
        dia_reserva = Dia(12)
        fecha_reserva = Fecha(ano_reserva, mes_reserva, dia_reserva)
        hora_reserva = Hora(0)
        minuto_reserva = Minuto(0)
        segundo_reserva = Segundo(1)
        horario_inicio_reserva = Tiempo(hora_reserva,minuto_reserva,segundo_reserva)

        hora2_reserva = Hora(0)
        minuto2_reserva = Minuto(0)
        segundo2_reserva = Segundo(3)
        horario_fin_reserva = Tiempo(hora2_reserva,minuto2_reserva,segundo2_reserva)
        reserva = Reserva(self._sala_papu, self._usuario_porky,fecha_reserva,horario_inicio_reserva,horario_fin_reserva)
        with self.assertRaises(NoExisteLaReserva):
            self._usuario_porky.cancelar_reserva_programada(reserva)

    def test_05_borrar_reserva_de_otra_persona_tira_error(self):
        ano_reserva = Ano(2024)
        mes_reserva = Mes(9)
        dia_reserva = Dia(12)
        fecha_reserva = Fecha(ano_reserva, mes_reserva, dia_reserva)
        hora_reserva = Hora(0)
        minuto_reserva = Minuto(0)
        segundo_reserva = Segundo(10)
        horario_inicio_reserva = Tiempo(hora_reserva,minuto_reserva,segundo_reserva)

        hora2_reserva = Hora(0)
        minuto2_reserva = Minuto(0)
        segundo2_reserva = Segundo(20)
        horario_fin_reserva = Tiempo(hora2_reserva,minuto2_reserva,segundo2_reserva)

        self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva,horario_inicio_reserva,horario_fin_reserva)
        reserva_de_porky = Reserva(self._sala_papu, self._usuario_porky,fecha_reserva,horario_inicio_reserva,horario_fin_reserva)
        
        usuario_no_dueño_de_la_reserva = Usuario("Ronnie Coleman")
        with self.assertRaises(ReservaPerteneceOtroUsuario):
            usuario_no_dueño_de_la_reserva.cancelar_reserva_programada(reserva_de_porky)

    
if __name__ == "__main__":
    unittest.main()
