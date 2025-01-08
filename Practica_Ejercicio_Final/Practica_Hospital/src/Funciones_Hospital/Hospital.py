from src.Funciones_Paciente.Paciente import Paciente
from src.Funciones_Medico.Doctor import Doctor
from src.Funciones_Paciente.Paciente import Consulta

class Hospital:
    def __init__(self):
        # Inicializa las listas de doctores y pacientes
        self.doctores = []
        self.pacientes = []

    def registrar_paciente(self, paciente):
        # Registra un paciente en el hospital
        if isinstance(paciente, Paciente):
            self.pacientes.append(paciente)

    def asignar_paciente_a_doctor(self, paciente, doctor):
        # Asigna un paciente a un doctor
        if paciente in self.pacientes and isinstance(doctor, Doctor):
            doctor.pacientes_asignados.append(paciente)

    def ver_pacientes_asignados(self, doctor):
        # Ver pacientes asignados a un doctor
        if isinstance(doctor, Doctor):
            return doctor.pacientes_asignados
        return []