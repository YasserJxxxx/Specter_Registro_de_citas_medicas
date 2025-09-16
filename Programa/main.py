"""
SISTEMA DE GESTIÓN DE CITAS MÉDICAS CON PROGRAMACIÓN ORIENTADA A OBJETOS
Implementación completa con clases, herencia, encapsulación y polimorfismo
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict, Optional
import re

# ==================== CLASES BASE Y ENTIDADES ====================

class Persona(ABC):
    """Clase abstracta que representa a una persona"""
    
    def __init__(self, id: str, nombre: str, telefono: str, email: str = ""):
        self._id = id
        self._nombre = nombre
        self._telefono = telefono
        self._email = email
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def telefono(self) -> str:
        return self._telefono
    
    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, value: str):
        if self._validar_email(value):
            self._email = value
        else:
            raise ValueError("Email no válido")
    
    def _validar_email(self, email: str) -> bool:
        """Valida el formato del email"""
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None
    
    @abstractmethod
    def mostrar_info(self) -> str:
        pass
    
    def __str__(self) -> str:
        return self.mostrar_info()


class Paciente(Persona):
    """Clase que representa a un paciente"""
    
    def __init__(self, id: str, nombre: str, telefono: str, edad: int, 
                 historial_medico: str = "", email: str = ""):
        super().__init__(id, nombre, telefono, email)
        self._edad = edad
        self._historial_medico = historial_medico
        self._citas: List[Cita] = []
    
    @property
    def edad(self) -> int:
        return self._edad
    
    @property
    def historial_medico(self) -> str:
        return self._historial_medico
    
    @historial_medico.setter
    def historial_medico(self, value: str):
        self._historial_medico = value
    
    @property
    def citas(self) -> List['Cita']:
        return self._citas
    
    def agregar_cita(self, cita: 'Cita'):
        """Agrega una cita al historial del paciente"""
        self._citas.append(cita)
    
    def mostrar_info(self) -> str:
        return f"Paciente {self._id}: {self._nombre} ({self._edad} años) - Tel: {self._telefono}"
    
    def obtener_citas_activas(self) -> List['Cita']:
        """Retorna las citas activas del paciente"""
        return [cita for cita in self._citas if cita.estado == "Programada"]


class Doctor(Persona):
    """Clase que representa a un doctor"""
    
    def __init__(self, id: str, nombre: str, telefono: str, especialidad: str, 
                 email: str = "", horario: Dict[str, List[str]] = None):
        super().__init__(id, nombre, telefono, email)
        self._especialidad = especialidad
        self._horario = horario or self._generar_horario_default()
        self._citas: List[Cita] = []
    
    @property
    def especialidad(self) -> str:
        return self._especialidad
    
    @property
    def horario(self) -> Dict[str, List[str]]:
        return self._horario
    
    @property
    def citas(self) -> List['Cita']:
        return self._citas
    
    def _generar_horario_default(self) -> Dict[str, List[str]]:
        """Genera un horario por defecto"""
        return {
            "Lunes": ["09:00-17:00"],
            "Martes": ["09:00-17:00"],
            "Miércoles": ["09:00-17:00"],
            "Jueves": ["09:00-17:00"],
            "Viernes": ["09:00-17:00"]
        }
    
    def agregar_cita(self, cita: 'Cita'):
        """Agrega una cita al historial del doctor"""
        self._citas.append(cita)
    
    def mostrar_info(self) -> str:
        return f"Doctor {self._id}: Dr. {self._nombre} - {self._especialidad}"
    
    def obtener_citas_activas(self) -> List['Cita']:
        """Retorna las citas activas del doctor"""
        return [cita for cita in self._citas if cita.estado == "Programada"]


class Cita:
    """Clase que representa una cita médica"""
    
    def __init__(self, id: str, paciente: Paciente, doctor: Doctor, 
                 fecha: str, hora: str, motivo: str, estado: str = "Programada"):
        self._id = id
        self._paciente = paciente
        self._doctor = doctor
        self._fecha = fecha
        self._hora = hora
        self._motivo = motivo
        self._estado = estado
        
        # Agregar la cita al paciente y doctor
        paciente.agregar_cita(self)
        doctor.agregar_cita(self)
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def paciente(self) -> Paciente:
        return self._paciente
    
    @property
    def doctor(self) -> Doctor:
        return self._doctor
    
    @property
    def fecha(self) -> str:
        return self._fecha
    
    @property
    def hora(self) -> str:
        return self._hora
    
    @property
    def motivo(self) -> str:
        return self._motivo
    
    @property
    def estado(self) -> str:
        return self._estado
    
    @estado.setter
    def estado(self, value: str):
        if value in ["Programada", "Cancelada", "Completada"]:
            self._estado = value
        else:
            raise ValueError("Estado no válido")
    
    def mostrar_info(self) -> str:
        estado_icono = "✅" if self._estado == "Programada" else "❌"
        return (f"Cita {self._id}: {self._paciente.nombre} con Dr. {self._doctor.nombre}\n"
                f"   📅 {self._fecha} {self._hora} - {self._motivo}\n"
                f"   Estado: {estado_icono} {self._estado}")
    
    def __str__(self) -> str:
        return self.mostrar_info()


# ==================== GESTIÓN Y CONTROLADORES ====================

class GestorIDs:
    """Clase para la gestión y generación de IDs únicos"""
    
    _contadores = {
        "paciente": 1,
        "doctor": 1,
        "cita": 1
    }
    
    @classmethod
    def generar_id(cls, tipo: str) -> str:
        """Genera un ID único para el tipo especificado"""
        if tipo not in cls._contadores:
            raise ValueError("Tipo de ID no válido")
        
        contador = cls._contadores[tipo]
        cls._contadores[tipo] += 1
        
        if tipo == "paciente":
            return f"P{contador:03d}"
        elif tipo == "doctor":
            return f"D{contador:03d}"
        elif tipo == "cita":
            return f"C{contador:03d}"


class SistemaCitasMedicas:
    """Clase principal que gestiona todo el sistema de citas"""
    
    def __init__(self):
        self._pacientes: List[Paciente] = []
        self._doctores: List[Doctor] = []
        self._citas: List[Cita] = []
        self._cargar_datos_ejemplo()
    
    @property
    def pacientes(self) -> List[Paciente]:
        return self._pacientes
    
    @property
    def doctores(self) -> List[Doctor]:
        return self._doctores
    
    @property
    def citas(self) -> List[Cita]:
        return self._citas
    
    def _cargar_datos_ejemplo(self):
        """Carga datos de ejemplo para testing"""
        try:
            # Pacientes de ejemplo
            paciente1 = Paciente(
                GestorIDs.generar_id("paciente"), 
                "Ana García", "555-1234", 35, "Hipertensión"
            )
            paciente2 = Paciente(
                GestorIDs.generar_id("paciente"),
                "Carlos López", "555-5678", 28, "Asma"
            )
            
            # Doctores de ejemplo
            doctor1 = Doctor(
                GestorIDs.generar_id("doctor"),
                "Rodríguez", "555-1111", "Cardiología"
            )
            doctor2 = Doctor(
                GestorIDs.generar_id("doctor"),
                "Martínez", "555-2222", "Pediatría"
            )
            
            self.agregar_paciente(paciente1)
            self.agregar_paciente(paciente2)
            self.agregar_doctor(doctor1)
            self.agregar_doctor(doctor2)
            
        except Exception as e:
            print(f"Error al cargar datos de ejemplo: {e}")
    
    def agregar_paciente(self, paciente: Paciente) -> bool:
        """Agrega un nuevo paciente al sistema"""
        if any(p.id == paciente.id for p in self._pacientes):
            return False
        self._pacientes.append(paciente)
        return True
    
    def agregar_doctor(self, doctor: Doctor) -> bool:
        """Agrega un nuevo doctor al sistema"""
        if any(d.id == doctor.id for d in self._doctores):
            return False
        self._doctores.append(doctor)
        return True
    
    def agregar_cita(self, cita: Cita) -> bool:
        """Agrega una nueva cita al sistema"""
        if any(c.id == cita.id for c in self._citas):
            return False
        self._citas.append(cita)
        return True
    
    def buscar_paciente_por_id(self, paciente_id: str) -> Optional[Paciente]:
        """Busca un paciente por su ID"""
        for paciente in self._pacientes:
            if paciente.id == paciente_id:
                return paciente
        return None
    
    def buscar_doctor_por_id(self, doctor_id: str) -> Optional[Doctor]:
        """Busca un doctor por su ID"""
        for doctor in self._doctores:
            if doctor.id == doctor_id:
                return doctor
        return None
    
    def buscar_cita_por_id(self, cita_id: str) -> Optional[Cita]:
        """Busca una cita por su ID"""
        for cita in self._citas:
            if cita.id == cita_id:
                return cita
        return None
    
    def obtener_citas_por_paciente(self, paciente_id: str) -> List[Cita]:
        """Obtiene todas las citas de un paciente"""
        paciente = self.buscar_paciente_por_id(paciente_id)
        return paciente.citas if paciente else []
    
    def obtener_citas_por_doctor(self, doctor_id: str) -> List[Cita]:
        """Obtiene todas las citas de un doctor"""
        doctor = self.buscar_doctor_por_id(doctor_id)
        return doctor.citas if doctor else []
    
    def obtener_citas_activas(self) -> List[Cita]:
        """Obtiene todas las citas activas"""
        return [cita for cita in self._citas if cita.estado == "Programada"]
    
    def cancelar_cita(self, cita_id: str) -> bool:
        """Cancela una cita existente"""
        cita = self.buscar_cita_por_id(cita_id)
        if cita:
            cita.estado = "Cancelada"
            return True
        return False


# ==================== MÓDULOS DE INTERFAZ ====================

class ModuloPacientes:
    """Módulo para gestionar la interfaz de pacientes"""
    
    def __init__(self, sistema: SistemaCitasMedicas):
        self._sistema = sistema
    
    def ejecutar(self, opcion: str):
        """Ejecuta la operación seleccionada"""
        match opcion:
            case "1":  # Registrar paciente
                self._registrar_paciente()
            case "2":  # Listar pacientes
                self._listar_pacientes()
            case _:
                print("Opción no válida")
    
    def _registrar_paciente(self):
        """Registra un nuevo paciente"""
        print("\n--- REGISTRAR PACIENTE ---")
        
        try:
            nombre = input("Nombre: ").strip()
            telefono = input("Teléfono: ").strip()
            edad_str = input("Edad: ").strip()
            email = input("Email (opcional): ").strip()
            historial = input("Historial médico (opcional): ").strip()
            
            if not nombre or not telefono or not edad_str:
                print("Error: Nombre, teléfono y edad son obligatorios")
                return
            
            edad = int(edad_str)
            paciente_id = GestorIDs.generar_id("paciente")
            
            paciente = Paciente(
                id=paciente_id,
                nombre=nombre,
                telefono=telefono,
                edad=edad,
                historial_medico=historial,
                email=email
            )
            
            if self._sistema.agregar_paciente(paciente):
                print(f"✅ Paciente {paciente_id} registrado: {nombre}")
            else:
                print("❌ Error al registrar el paciente")
                
        except ValueError:
            print("❌ Error: La edad debe ser un número válido")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    def _listar_pacientes(self):
        """Lista todos los pacientes"""
        print("\n--- LISTA DE PACIENTES ---")
        
        if not self._sistema.pacientes:
            print("No hay pacientes registrados")
            return
        
        for i, paciente in enumerate(self._sistema.pacientes, 1):
            print(f"{i}. {paciente.mostrar_info()}")
            if paciente.historial_medico:
                print(f"   Historial: {paciente.historial_medico}")


class ModuloDoctores:
    """Módulo para gestionar la interfaz de doctores"""
    
    def __init__(self, sistema: SistemaCitasMedicas):
        self._sistema = sistema
    
    def ejecutar(self, opcion: str):
        """Ejecuta la operación seleccionada"""
        match opcion:
            case "1":  # Registrar doctor
                self._registrar_doctor()
            case "2":  # Listar doctores
                self._listar_doctores()
            case _:
                print("Opción no válida")
    
    def _registrar_doctor(self):
        """Registra un nuevo doctor"""
        print("\n--- REGISTRAR DOCTOR ---")
        
        try:
            nombre = input("Nombre del doctor: ").strip()
            especialidad = input("Especialidad: ").strip()
            telefono = input("Teléfono: ").strip()
            email = input("Email (opcional): ").strip()
            
            if not nombre or not especialidad or not telefono:
                print("Error: Nombre, especialidad y teléfono son obligatorios")
                return
            
            doctor_id = GestorIDs.generar_id("doctor")
            
            doctor = Doctor(
                id=doctor_id,
                nombre=nombre,
                telefono=telefono,
                especialidad=especialidad,
                email=email
            )
            
            if self._sistema.agregar_doctor(doctor):
                print(f"✅ Doctor {doctor_id} registrado: Dr. {nombre} - {especialidad}")
            else:
                print("❌ Error al registrar el doctor")
                
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    def _listar_doctores(self):
        """Lista todos los doctores"""
        print("\n--- LISTA DE DOCTORES ---")
        
        if not self._sistema.doctores:
            print("No hay doctores registrados")
            return
        
        for i, doctor in enumerate(self._sistema.doctores, 1):
            print(f"{i}. {doctor.mostrar_info()}")


class ModuloCitas:
    """Módulo para gestionar la interfaz de citas"""
    
    def __init__(self, sistema: SistemaCitasMedicas):
        self._sistema = sistema
    
    def ejecutar(self, opcion: str):
        """Ejecuta la operación seleccionada"""
        match opcion:
            case "1":  # Programar cita
                self._programar_cita()
            case "2":  # Listar citas
                self._listar_citas()
            case "3":  # Cancelar cita
                self._cancelar_cita()
            case _:
                print("Opción no válida")
    
    def _programar_cita(self):
        """Programa una nueva cita"""
        print("\n--- PROGRAMAR CITA ---")
        
        # Verificar que existan pacientes y doctores
        if not self._sistema.pacientes:
            print("❌ No hay pacientes registrados")
            return
        
        if not self._sistema.doctores:
            print("❌ No hay doctores registrados")
            return
        
        try:
            # Seleccionar paciente
            print("Pacientes disponibles:")
            for i, paciente in enumerate(self._sistema.pacientes, 1):
                print(f"{i}. {paciente.nombre}")
            
            opcion_paciente = int(input("Seleccione el paciente: ")) - 1
            if not (0 <= opcion_paciente < len(self._sistema.pacientes)):
                print("❌ Selección inválida")
                return
            
            paciente = self._sistema.pacientes[opcion_paciente]
            
            # Seleccionar doctor
            print("Doctores disponibles:")
            for i, doctor in enumerate(self._sistema.doctores, 1):
                print(f"{i}. Dr. {doctor.nombre} - {doctor.especialidad}")
            
            opcion_doctor = int(input("Seleccione el doctor: ")) - 1
            if not (0 <= opcion_doctor < len(self._sistema.doctores)):
                print("❌ Selección inválida")
                return
            
            doctor = self._sistema.doctores[opcion_doctor]
            
            # Fecha, hora y motivo
            fecha = input("Fecha (DD/MM/AAAA): ").strip()
            hora = input("Hora (HH:MM): ").strip()
            motivo = input("Motivo de la consulta: ").strip()
            
            if not fecha or not hora or not motivo:
                print("❌ Fecha, hora y motivo son obligatorios")
                return
            
            # Crear cita
            cita_id = GestorIDs.generar_id("cita")
            cita = Cita(
                id=cita_id,
                paciente=paciente,
                doctor=doctor,
                fecha=fecha,
                hora=hora,
                motivo=motivo
            )
            
            if self._sistema.agregar_cita(cita):
                print(f"✅ Cita {cita_id} programada exitosamente")
                print(f"   {paciente.nombre} con Dr. {doctor.nombre} el {fecha} a las {hora}")
            else:
                print("❌ Error al programar la cita")
                
        except ValueError:
            print("❌ Error: Selección inválida")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    def _listar_citas(self):
        """Lista todas las citas"""
        print("\n--- LISTA DE CITAS ---")
        
        if not self._sistema.citas:
            print("No hay citas programadas")
            return
        
        for i, cita in enumerate(self._sistema.citas, 1):
            print(f"{i}. {cita.mostrar_info()}")
            print("   " + "-" * 50)
    
    def _cancelar_cita(self):
        """Cancela una cita existente"""
        print("\n--- CANCELAR CITA ---")
        
        citas_activas = self._sistema.obtener_citas_activas()
        
        if not citas_activas:
            print("❌ No hay citas activas para cancelar")
            return
        
        print("Citas activas:")
        for i, cita in enumerate(citas_activas, 1):
            print(f"{i}. {cita.id}: {cita.paciente.nombre} con Dr. {cita.doctor.nombre} - {cita.fecha} {cita.hora}")
        
        try:
            opcion = int(input("Seleccione la cita a cancelar: ")) - 1
            if 0 <= opcion < len(citas_activas):
                cita = citas_activas[opcion]
                if self._sistema.cancelar_cita(cita.id):
                    print("✅ Cita cancelada exitosamente")
                else:
                    print("❌ Error al cancelar la cita")
            else:
                print("❌ Opción inválida")
        except ValueError:
            print("❌ Error: Ingrese un número válido")


class ModuloReportes:
    """Módulo para generar reportes del sistema"""
    
    def __init__(self, sistema: SistemaCitasMedicas):
        self._sistema = sistema
    
    def ejecutar(self, opcion: str):
        """Ejecuta la operación seleccionada"""
        match opcion:
            case "1":  # Citas por doctor
                self._citas_por_doctor()
            case "2":  # Citas por paciente
                self._citas_por_paciente()
            case "3":  # Estadísticas
                self._estadisticas_generales()
            case _:
                print("Opción no válida")
    
    def _citas_por_doctor(self):
        """Muestra citas agrupadas por doctor"""
        print("\n--- CITAS POR DOCTOR ---")
        
        if not self._sistema.citas:
            print("No hay citas programadas")
            return
        
        for doctor in self._sistema.doctores:
            citas_doctor = self._sistema.obtener_citas_por_doctor(doctor.id)
            if citas_doctor:
                print(f"\nDr. {doctor.nombre} - {doctor.especialidad}:")
                for cita in citas_doctor:
                    estado = "✅" if cita.estado == "Programada" else "❌"
                    print(f"   {estado} {cita.fecha} {cita.hora} - {cita.paciente.nombre}")
    
    def _citas_por_paciente(self):
        """Muestra citas agrupadas por paciente"""
        print("\n--- CITAS POR PACIENTE ---")
        
        if not self._sistema.citas:
            print("No hay citas programadas")
            return
        
        for paciente in self._sistema.pacientes:
            citas_paciente = self._sistema.obtener_citas_por_paciente(paciente.id)
            if citas_paciente:
                print(f"\n{paciente.nombre}:")
                for cita in citas_paciente:
                    estado = "✅" if cita.estado == "Programada" else "❌"
                    print(f"   {estado} {cita.fecha} {cita.hora} - Dr. {cita.doctor.nombre}")
    
    def _estadisticas_generales(self):
        """Muestra estadísticas generales del sistema"""
        print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
        print(f"Total pacientes: {len(self._sistema.pacientes)}")
        print(f"Total doctores: {len(self._sistema.doctores)}")
        print(f"Total citas: {len(self._sistema.citas)}")
        
        if self._sistema.citas:
            citas_activas = len(self._sistema.obtener_citas_activas())
            citas_canceladas = len([c for c in self._sistema.citas if c.estado == "Cancelada"])
            print(f"Citas activas: {citas_activas}")
            print(f"Citas canceladas: {citas_canceladas}")


# ==================== INTERFAZ PRINCIPAL ====================

class InterfazUsuario:
    """Clase principal para la interfaz de usuario"""
    
    def __init__(self):
        self._sistema = SistemaCitasMedicas()
        self._modulo_pacientes = ModuloPacientes(self._sistema)
        self._modulo_doctores = ModuloDoctores(self._sistema)
        self._modulo_citas = ModuloCitas(self._sistema)
        self._modulo_reportes = ModuloReportes(self._sistema)
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal"""
        print("\n" + "="*50)
        print("SISTEMA DE GESTION DE CITAS MEDICAS")
        print("="*50)
        print("1. Gestion de Pacientes")
        print("2. Gestion de Doctores")
        print("3. Gestion de Citas")
        print("4. Reportes y Estadisticas")
        print("5. Salir")
        print("="*50)
    
    def mostrar_submenu(self, titulo: str, opciones: Dict[str, str]) -> str:
        """Muestra un submenú y retorna la opción seleccionada"""
        print(f"\n--- {titulo} ---")
        for key, value in opciones.items():
            print(f"{key}. {value}")
        return input("Seleccione una opción: ").strip()
    
    def ejecutar(self):
        """Ejecuta el sistema principal"""
        print("Sistema de Gestion de Citas Medicas")
        print("Datos de ejemplo cargados automaticamente")
        
        while True:
            self.mostrar_menu_principal()
            opcion_principal = input("Seleccione una opción: ").strip()
            
            match opcion_principal:
                case "1":  # Gestión de Pacientes
                    opcion = self.mostrar_submenu("GESTION DE PACIENTES", {
                        "1": "Registrar paciente",
                        "2": "Listar pacientes",
                        "3": "Volver"
                    })
                    if opcion != "3":
                        self._modulo_pacientes.ejecutar(opcion)
                
                case "2":  # Gestión de Doctores
                    opcion = self.mostrar_submenu("GESTION DE DOCTORES", {
                        "1": "Registrar doctor",
                        "2": "Listar doctores",
                        "3": "Volver"
                    })
                    if opcion != "3":
                        self._modulo_doctores.ejecutar(opcion)
                
                case "3":  # Gestión de Citas
                    opcion = self.mostrar_submenu("GESTION DE CITAS", {
                        "1": "Programar cita",
                        "2": "Listar citas",
                        "3": "Cancelar cita",
                        "4": "Volver"
                    })
                    if opcion != "4":
                        self._modulo_citas.ejecutar(opcion)
                
                case "4":  # Reportes
                    opcion = self.mostrar_submenu("REPORTES Y ESTADISTICAS", {
                        "1": "Citas por doctor",
                        "2": "Citas por paciente",
                        "3": "Estadisticas generales",
                        "4": "Volver"
                    })
                    if opcion != "4":
                        self._modulo_reportes.ejecutar(opcion)
                
                case "5":  # Salir
                    print("Hasta pronto!")
                    break
                
                case _:
                    print("Opcion no valida. Intente de nuevo.")


# ==================== PROGRAMA PRINCIPAL ====================

def main():
    """Función principal del programa"""
    try:
        interfaz = InterfazUsuario()
        interfaz.ejecutar()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()