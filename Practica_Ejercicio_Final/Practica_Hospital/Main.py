from src.Funciones_Paciente.Paciente import Paciente
from src.Funciones_Medico.Doctor import Doctor
from src.Funciones_Paciente.Paciente import Consulta 
from src.Funciones_Hospital.Hospital import Hospital

if __name__ == "__main__":
    hospital = Hospital()

    while True:
        print("Bienvenido al sistema del hospital")
        print("1. Soy un paciente")
        print("2. Soy un doctor")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("--- Menú Paciente ---")
            nombre = input("Ingrese su nombre: ")  # Solicita el nombre del paciente
            edad = int(input("Ingrese su edad: "))  # Solicita la edad del paciente
            paciente = Paciente(nombre, edad)
            hospital.registrar_paciente(paciente)

            print("Paciente registrado correctamente.")
            print("1. Ver historial clínico")
            print("2. Salir")
            sub_opcion = input("Seleccione una opción: ")

            if sub_opcion == "1":
                # Muestra el historial clínico del paciente
                if paciente.ver_historial():
                    for consulta in paciente.ver_historial():
                        print(f"Fecha: {consulta.fecha}, Síntomas: {consulta.sintomas}, Diagnóstico: {consulta.diagnostico}, Medicamento: {consulta.medicamento}")
                else:
                    print("No hay historial clínico disponible.")

        elif opcion == "2":
            print("--- Menú Doctor ---")
            nombre = input("Ingrese su nombre: ")  # Solicita el nombre del doctor
            especialidad = input("Ingrese su especialidad: ")  # Solicita la especialidad del doctor
            doctor = Doctor(nombre, especialidad)
            hospital.doctores.append(doctor)

            print("Doctor registrado correctamente.")
            print("1. Registrar consulta")
            print("2. Recetar medicamento")
            print("3. Ver pacientes asignados")
            print("4. Salir")
            sub_opcion = input("Seleccione una opción: ")

            if sub_opcion == "1":
                # Registra una consulta para un paciente
                paciente_nombre = input("Ingrese el nombre del paciente: ")
                paciente_encontrado = next((p for p in hospital.pacientes if p.nombre == paciente_nombre), None)
                if paciente_encontrado:
                    fecha = input("Ingrese la fecha de la consulta (YYYY-MM-DD): ")
                    sintomas = input("Ingrese los síntomas: ")
                    diagnostico = input("Ingrese el diagnóstico: ")
                    medicamento = input("Ingrese el medicamento recetado: ")
                    consulta = Consulta(fecha, sintomas, diagnostico, medicamento)
                    doctor.registrar_consulta(paciente_encontrado, consulta)
                    print("Consulta registrada correctamente.")
                else:
                    print("Paciente no encontrado. ¿Desea intentar nuevamente? (s/n)")
                    retry = input().lower()
                    if retry == 's':
                        continue
                    else:
                        break

            elif sub_opcion == "2":
                # Receta un medicamento a un paciente
                paciente_nombre = input("Ingrese el nombre del paciente: ")
                paciente_encontrado = next((p for p in hospital.pacientes if p.nombre == paciente_nombre), None)
                if paciente_encontrado:
                    medicamento = input("Ingrese el medicamento a recetar: ")
                    doctor.recetar_medicamento(paciente_encontrado, medicamento)
                    print("Medicamento recetado correctamente.")
                else:
                    print("Paciente no encontrado.")

            elif sub_opcion == "3":
                # Ver pacientes asignados al doctor
                pacientes_asignados = hospital.ver_pacientes_asignados(doctor)
                if pacientes_asignados:
                    print("Pacientes asignados:")
                    for paciente in pacientes_asignados:
                        print(f"Nombre: {paciente.nombre}, Edad: {paciente.edad}")
                else:
                    print("No hay pacientes asignados.")

            elif sub_opcion == "4":
                # Salir del menú del doctor
                break

        elif opcion == "3":
            # Finaliza el programa
            print("Saliendo del sistema. ¡Gracias por usar el sistema del hospital!")
            break

        else:
            print("Opción no válida. Por favor, intente nuevamente.")

