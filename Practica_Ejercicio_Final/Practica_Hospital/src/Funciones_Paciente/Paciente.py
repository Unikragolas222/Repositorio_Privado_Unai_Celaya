class Consulta:
    def __init__(self, fecha, sintomas, diagnostico, medicamento):
        # Inicializa una consulta con fecha, sintomas, diagnostico y medicamento recetado
        self.fecha = fecha
        self.sintomas = sintomas
        self.diagnostico = diagnostico
        self.medicamento = medicamento

class Paciente:
    def __init__(self, nombre, edad):
        # Inicializa un paciente con su nombre y edad
        self.nombre = nombre
        self.edad = edad
        self.historial_clinico = []  # Lista vacía para almacenar consultas

    def agregar_consulta(self, consulta):
        # Agrega un objeto Consulta al historial clínico si es válido
        if isinstance(consulta, Consulta):
            self.historial_clinico.append(consulta)

    def ver_historial(self):
        # Devuelve la lista de consultas en el historial clínico
        return self.historial_clinico
