from src.Funciones_Paciente.Paciente import Paciente, Consulta

class Doctor:
    def __init__(self, nombre, especialidad):
        # Inicializa un doctor con su nombre y especialidad
        self.nombre = nombre
        self.especialidad = especialidad
        self.pacientes_asignados = []  # Lista vacía para almacenar pacientes asignados

    def registrar_consulta(self, paciente, consulta):
        # Registra una consulta para un paciente dado
        if isinstance(paciente, Paciente) and isinstance(consulta, Consulta):
            paciente.agregar_consulta(consulta)

    def recetar_medicamento(self, paciente, medicamento):
        # Actualiza el medicamento recetado en la última consulta del historial clínico del paciente
        if paciente.historial_clinico:  # Verifica que haya consultas en el historial
            ultima_consulta = paciente.historial_clinico[-1]  # Obtiene la última consulta
            ultima_consulta.medicamento = medicamento
