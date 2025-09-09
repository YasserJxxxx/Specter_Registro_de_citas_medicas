"""
SISTEMA MODULAR DE CITAS MÉDICAS
Usando match-case y módulos/funciones para cada caso
"""

# ==================== MÓDULOS/FUNCIONES ====================

# Módulo de pacientes
def modulo_pacientes(pacientes, opcion):
    """Gestiona todas las operaciones de pacientes"""
    match opcion:
        case "1":  # Registrar paciente
            print("\n--- REGISTRAR PACIENTE ---")
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            edad = input("Edad: ")
            
            if not nombre or not telefono or not edad:
                print("❌ Todos los campos son obligatorios")
                return pacientes
            
            # Crear paciente (POO simple)
            paciente_id = f"P{len(pacientes)+1:03d}"
            paciente = {
                "id": paciente_id,
                "nombre": nombre,
                "telefono": telefono,
                "edad": edad
            }
            
            pacientes.append(paciente)
            print(f"✅ Paciente {paciente_id} registrado: {nombre}")
            return pacientes
        
        case "2":  # Listar pacientes
            print("\n--- LISTA DE PACIENTES ---")
            if not pacientes:
                print("No hay pacientes registrados")
            else:
                for i, paciente in enumerate(pacientes, 1):
                    print(f"{i}. {paciente['id']}: {paciente['nombre']} - {paciente['telefono']} ({paciente['edad']} años)")
            return pacientes
        
        case _:
            print("❌ Opción no válida")
            return pacientes

# Módulo de doctores
def modulo_doctores(doctores, opcion):
    """Gestiona todas las operaciones de doctores"""
    match opcion:
        case "1":  # Registrar doctor
            print("\n--- REGISTRAR DOCTOR ---")
            nombre = input("Nombre del doctor: ")
            especialidad = input("Especialidad: ")
            
            if not nombre or not especialidad:
                print("❌ Todos los campos son obligatorios")
                return doctores
            
            # Crear doctor
            doctor_id = f"D{len(doctores)+1:03d}"
            doctor = {
                "id": doctor_id,
                "nombre": nombre,
                "especialidad": especialidad
            }
            
            doctores.append(doctor)
            print(f"✅ Doctor {doctor_id} registrado: Dr. {nombre} - {especialidad}")
            return doctores
        
        case "2":  # Listar doctores
            print("\n--- LISTA DE DOCTORES ---")
            if not doctores:
                print("No hay doctores registrados")
            else:
                for i, doctor in enumerate(doctores, 1):
                    print(f"{i}. {doctor['id']}: Dr. {doctor['nombre']} - {doctor['especialidad']}")
            return doctores
        
        case _:
            print("❌ Opción no válida")
            return doctores

# Módulo de citas
def modulo_citas(citas, pacientes, doctores, opcion):
    """Gestiona todas las operaciones de citas"""
    match opcion:
        case "1":  # Programar cita
            print("\n--- PROGRAMAR CITA ---")
            
            # Verificar que existan pacientes y doctores
            if not pacientes:
                print("❌ No hay pacientes registrados")
                return citas
            
            if not doctores:
                print("❌ No hay doctores registrados")
                return citas
            
            # Seleccionar paciente
            print("Pacientes disponibles:")
            for i, paciente in enumerate(pacientes, 1):
                print(f"{i}. {paciente['nombre']}")
            
            try:
                opcion_paciente = int(input("Seleccione el paciente: ")) - 1
                paciente = pacientes[opcion_paciente]
            except:
                print("❌ Selección inválida")
                return citas
            
            # Seleccionar doctor
            print("Doctores disponibles:")
            for i, doctor in enumerate(doctores, 1):
                print(f"{i}. Dr. {doctor['nombre']} - {doctor['especialidad']}")
            
            try:
                opcion_doctor = int(input("Seleccione el doctor: ")) - 1
                doctor = doctores[opcion_doctor]
            except:
                print("❌ Selección inválida")
                return citas
            
            # Fecha y hora
            fecha = input("Fecha (DD/MM/AAAA): ")
            hora = input("Hora (HH:MM): ")
            
            if not fecha or not hora:
                print("❌ Fecha y hora son obligatorios")
                return citas
            
            # Crear cita
            cita_id = f"C{len(citas)+1:03d}"
            cita = {
                "id": cita_id,
                "paciente_id": paciente["id"],
                "paciente_nombre": paciente["nombre"],
                "doctor_id": doctor["id"],
                "doctor_nombre": doctor["nombre"],
                "especialidad": doctor["especialidad"],
                "fecha": fecha,
                "hora": hora,
                "estado": "Programada"
            }
            
            citas.append(cita)
            print(f"✅ Cita {cita_id} programada: {paciente['nombre']} con Dr. {doctor['nombre']} el {fecha} a las {hora}")
            return citas
        
        case "2":  # Listar citas
            print("\n--- LISTA DE CITAS ---")
            if not citas:
                print("No hay citas programadas")
            else:
                for i, cita in enumerate(citas, 1):
                    estado = "✅" if cita["estado"] == "Programada" else "❌"
                    print(f"{i}. {cita['id']}: {cita['paciente_nombre']} con Dr. {cita['doctor_nombre']} ({cita['especialidad']})")
                    print(f"   📅 {cita['fecha']} {cita['hora']} - Estado: {cita['estado']}")
                    print("   " + "-" * 30)
            return citas
        
        case "3":  # Cancelar cita
            print("\n--- CANCELAR CITA ---")
            
            if not citas:
                print("❌ No hay citas programadas")
                return citas
            
            # Mostrar solo citas activas
            citas_activas = [c for c in citas if c["estado"] == "Programada"]
            
            if not citas_activas:
                print("❌ No hay citas activas para cancelar")
                return citas
            
            print("Citas activas:")
            for i, cita in enumerate(citas_activas, 1):
                print(f"{i}. {cita['id']}: {cita['paciente_nombre']} con Dr. {cita['doctor_nombre']} - {cita['fecha']} {cita['hora']}")
            
            try:
                opcion_cita = int(input("Seleccione la cita a cancelar: ")) - 1
                if 0 <= opcion_cita < len(citas_activas):
                    citas_activas[opcion_cita]["estado"] = "Cancelada"
                    print("✅ Cita cancelada exitosamente")
                else:
                    print("❌ Opción inválida")
            except:
                print("❌ Selección inválida")
            
            return citas
        
        case _:
            print("❌ Opción no válida")
            return citas

# Módulo de reportes
def modulo_reportes(citas, pacientes, doctores, opcion):
    """Genera reportes del sistema"""
    match opcion:
        case "1":  # Citas por doctor
            print("\n--- CITAS POR DOCTOR ---")
            if not citas:
                print("No hay citas programadas")
                return
            
            # Agrupar citas por doctor
            citas_por_doctor = {}
            for cita in citas:
                doctor_key = f"{cita['doctor_nombre']} ({cita['especialidad']})"
                if doctor_key not in citas_por_doctor:
                    citas_por_doctor[doctor_key] = []
                citas_por_doctor[doctor_key].append(cita)
            
            for doctor, citas_doc in citas_por_doctor.items():
                print(f"\n👨‍⚕️ Dr. {doctor}:")
                for cita in citas_doc:
                    estado = "✅" if cita["estado"] == "Programada" else "❌"
                    print(f"   {estado} {cita['fecha']} {cita['hora']} - {cita['paciente_nombre']}")
        
        case "2":  # Citas por paciente
            print("\n--- CITAS POR PACIENTE ---")
            if not citas:
                print("No hay citas programadas")
                return
            
            # Agrupar citas por paciente
            citas_por_paciente = {}
            for cita in citas:
                if cita['paciente_nombre'] not in citas_por_paciente:
                    citas_por_paciente[cita['paciente_nombre']] = []
                citas_por_paciente[cita['paciente_nombre']].append(cita)
            
            for paciente, citas_pac in citas_por_paciente.items():
                print(f"\n👥 {paciente}:")
                for cita in citas_pac:
                    estado = "✅" if cita["estado"] == "Programada" else "❌"
                    print(f"   {estado} {cita['fecha']} {cita['hora']} - Dr. {cita['doctor_nombre']}")
        
        case "3":  # Estadísticas
            print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
            print(f"📊 Total pacientes: {len(pacientes)}")
            print(f"📊 Total doctores: {len(doctores)}")
            print(f"📊 Total citas: {len(citas)}")
            
            if citas:
                citas_activas = len([c for c in citas if c["estado"] == "Programada"])
                citas_canceladas = len([c for c in citas if c["estado"] == "Cancelada"])
                print(f"📊 Citas activas: {citas_activas}")
                print(f"📊 Citas canceladas: {citas_canceladas}")
        
        case _:
            print("❌ Opción no válida")

# Módulo de utilidades
def mostrar_menu_principal():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("🏥 SISTEMA DE CITAS MÉDICAS (MODULAR)")
    print("="*50)
    print("1. 👥 Gestión de Pacientes")
    print("2. 👨‍⚕️ Gestión de Doctores")
    print("3. 📅 Gestión de Citas")
    print("4. 📊 Reportes y Estadísticas")
    print("5. 🚪 Salir")
    print("="*50)

def mostrar_submenu(titulo, opciones):
    """Muestra un submenú genérico"""
    print(f"\n--- {titulo} ---")
    for key, value in opciones.items():
        print(f"{key}. {value}")
    return input("Seleccione una opción: ")

# ==================== PROGRAMA PRINCIPAL ====================
def main():
    """Función principal con match-case"""
    
    # Datos en memoria (listas como "base de datos")
    pacientes = []
    doctores = []
    citas = []
    
    # Datos de ejemplo
    pacientes.append({"id": "P001", "nombre": "Ana García", "telefono": "555-1234", "edad": "35"})
    pacientes.append({"id": "P002", "nombre": "Carlos López", "telefono": "555-5678", "edad": "28"})
    doctores.append({"id": "D001", "nombre": "Rodríguez", "especialidad": "Cardiología"})
    doctores.append({"id": "D002", "nombre": "Martínez", "especialidad": "Pediatría"})
    
    print("🚀 Sistema Modular de Citas Médicas")
    print("💡 Datos de ejemplo cargados automáticamente")
    
    # Bucle principal
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Seleccione una opción: ")
        
        # MATCH-CASE principal (Python 3.10+)
        match opcion_principal:
            case "1":  # Gestión de Pacientes
                opcion = mostrar_submenu("GESTIÓN DE PACIENTES", {
                    "1": "Registrar paciente",
                    "2": "Listar pacientes",
                    "3": "Volver"
                })
                if opcion != "3":
                    pacientes = modulo_pacientes(pacientes, opcion)
            
            case "2":  # Gestión de Doctores
                opcion = mostrar_submenu("GESTIÓN DE DOCTORES", {
                    "1": "Registrar doctor",
                    "2": "Listar doctores",
                    "3": "Volver"
                })
                if opcion != "3":
                    doctores = modulo_doctores(doctores, opcion)
            
            case "3":  # Gestión de Citas
                opcion = mostrar_submenu("GESTIÓN DE CITAS", {
                    "1": "Programar cita",
                    "2": "Listar citas",
                    "3": "Cancelar cita",
                    "4": "Volver"
                })
                if opcion != "4":
                    citas = modulo_citas(citas, pacientes, doctores, opcion)
            
            case "4":  # Reportes
                opcion = mostrar_submenu("REPORTES Y ESTADÍSTICAS", {
                    "1": "Citas por doctor",
                    "2": "Citas por paciente",
                    "3": "Estadísticas generales",
                    "4": "Volver"
                })
                if opcion != "4":
                    modulo_reportes(citas, pacientes, doctores, opcion)
            
            case "5":  # Salir
                print("👋 ¡Hasta pronto!")
                break
            
            case _:
                print("❌ Opción no válida. Intente de nuevo.")

# Punto de entrada
if __name__ == "__main__":
    main()