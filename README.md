Sistema de Gestion de Citas Medicas
Un sistema modular para la gestion de citas medicas desarrollado en Python, utilizando programacion orientada a objetos, estructuras de control y modularidad.

Características
Gestion de Pacientes: Registro y listado de pacientes

Gestion de Doctores: Registro y listado de medicos por especialidad

Gestion de Citas: Programacion, listado y cancelacion de citas

Sistema de Reportes: Estadisticas y consultas del sistema

Interfaz de Consola: Menus interactivos faciles de usar

Persistencia en Memoria: Datos almacenados durante la ejecucion

Requisitos del Sistema
Python 3.10 o superior (necesario para match case)

Sistema Operativo: Windows, macOS o Linux

Espacio en disco: Menos de 1MB

Memoria RAM: Minimo 512MB

Instalacion
Metodo 1: Clonar y Ejecutar
Descargar el archivo:

bash
# Si tienes git
git clone https://github.com/YasserJxxxx/Specter_Registro_de_citas_medicas

# O descarga directa del archivo .py
Navegar al directorio:

bash
cd sistema-citas-medicas
Verificar version de Python:

bash
python --version
# Debe mostrar: Python 3.10.x o superior
Metodo 2: Ejecucion Directa
Guardar el codigo en un archivo llamado sistema_citas.py

Abrir terminal en la ubicacion del archivo

Ejecucion del Programa
En Windows
bash
# Metodo 1: Desde la terminal
python sistema_citas.py

# Metodo 2: Doble clic en el archivo (si Python esta configurado correctamente)
En macOS/Linux
bash
# Metodo 1: Ejecucion directa
python3 sistema_citas.py

# Metodo 2: Hacer ejecutable y correr
chmod +x sistema_citas.py
python3 sistema_citas.py
En Visual Studio Code
Abrir VS Code

Abrir el archivo sistema_citas.py

Abrir terminal integrada (Ctrl + `)

Ejecutar:

bash
python sistema_citas.py
O usar el boton de ejecucion en la esquina superior derecha

Uso del Programa
Flujo Principal
Al iniciar el programa mostrara un menu principal con 5 opciones

Seleccionar opcion ingresando el numero correspondiente

Seguir submenus para operaciones especificas

Los datos se mantienen en memoria durante la ejecucion

Opciones del Menu Principal
Opcion	Funcion	Descripcion
1	Gestion de Pacientes	Registrar y listar pacientes
2	Gestion de Doctores	Registrar y listar medicos
3	Gestion de Citas	Programar, listar y cancelar citas
4	Reportes y Estadisticas	Ver reportes del sistema
5	Salir	Terminar el programa
Submenus Disponibles
Gestion de Pacientes
1 - Registrar nuevo paciente

2 - Listar pacientes existentes

3 - Volver al menu principal

Gestion de Doctores
1 - Registrar nuevo doctor

2 - Listar doctores existentes

3 - Volver al menu principal

Gestion de Citas
1 - Programar nueva cita

2 - Listar citas existentes

3 - Cancelar cita

4 - Volver al menu principal

Reportes
1 - Citas por doctor

2 - Citas por paciente

3 - Estadisticas generales

4 - Volver al menu principal

Caracteristicas Tecnicas
Estructura del Codigo
python
# Organizacion modular por funcionalidades
def modulo_pacientes()    # Gestion de pacientes
def modulo_doctores()     # Gestion de doctores  
def modulo_citas()        # Gestion de citas
def modulo_reportes()     # Sistema de reportes
Tecnologias Utilizadas
Python 3.10+: Para uso de match case

Estructuras de datos: Listas y diccionarios

POO: Programacion Orientada a Objetos

Modularidad: Funciones separadas por responsabilidad

Manejo de errores: Try-except para entradas invalidas

Datos de Ejemplo
El sistema incluye datos pre-cargados para testing:

2 pacientes de ejemplo

2 doctores de ejemplo

Facil de probar sin registro manual

Solucion de Problemas
Error: Version de Python incompatible
Sintoma:

bash
SyntaxError: invalid syntax (referencia a match case)
Solucion:

bash
# Actualizar Python
# Windows: https://www.python.org/downloads/
# macOS: brew install python@3.10
# Linux: sudo apt update && sudo apt install python3.10
Error: Archivo no encontrado
Solucion:

bash
# Navegar al directorio correcto
cd ruta/del/archivo

# Verificar que el archivo existe
ls sistema_citas.py  # Linux/macOS
dir sistema_citas.py # Windows
Error: Permisos denegados (Linux/macOS)
Solucion:

bash
chmod +x sistema_citas.py
Ejemplos de Uso
Registrar un Paciente
text
Seleccione: 1 (Pacientes)
 luego: 1 (Registrar paciente)

Nombre: Maria Gonzalez
Telefono: 555-9876
Edad: 42
Programar una Cita
text
Seleccione: 3 (Citas)
 luego: 1 (Programar cita)

Seleccione paciente: 1
Seleccione doctor: 1
Fecha: 15/12/2024
Hora: 10:30
Flujo de Trabajo Recomendado
Registrar doctores primero (Opcion 2 -> 1)

Registrar pacientes (Opcion 1 -> 1)

Programar citas (Opcion 3 -> 1)

Ver reportes (Opcion 4) para estadisticas

Notas Importantes
Los datos se pierden al cerrar el programa (estan en memoria)

Ideal para aprendizaje de Python y conceptos de programacion

Facil de extender para agregar persistencia en base de datos

Codigo documentado para facil comprension y modificacion

Para Estudiantes
Este proyecto es excelente para aprender:

Estructuras de control en Python

Programacion Orientada a Objetos

Manejo de listas y diccionarios

Modularidad y organizacion de codigo

Interfaz de linea de comandos

Soporte
Si encuentras problemas:

Verifica que tienes Python 3.10+

Revisa la sintaxis del codigo

Ejecuta en una terminal para ver mensajes de error

Disfruta aprendiendo Python con este sistema de citas medicas!