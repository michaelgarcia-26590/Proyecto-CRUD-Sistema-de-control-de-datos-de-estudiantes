"""
Aquí se almacenan las funciones que se utilizan para el proyecto CRUD
"""

estudiantes = {}

campos = ["nombre", "edad", "carrera", "promedio"]

class pedir_numero:
    """
    Clase para pedir un número al usuario y validarlo.
    """
    def __init__(self, mensaje, decimal=False):
        self.mensaje = mensaje
        self.decimal = decimal

    def __call__(self):
        while True:
            try:
                valor = input(self.mensaje)
                if self.decimal:
                    return float(valor)
                else:
                    return int(valor)
            except ValueError:
                print("  ⚠ Por favor, ingrese un número válido.")

def menu():
    """
    Función para mostrar el menú principal del programa.
    """
    print("=== Menú Principal ===")
    print("1. Crear estudiante")
    print("2. Leer estudiante")
    print("3. Actualizar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")
    return input("Seleccione una opción: ")

def agregar():
    """Pide los datos de un estudiante y los guarda."""
    matricula = input("Matrícula: ").strip().upper()
    if matricula in estudiantes:
        print("  ⚠ Esa matrícula ya existe.")
        return
    nombre = input("Nombre: ").strip()
    edad = pedir_numero("Edad: ")()
    carrera = input("Carrera: ").strip()
    promedio = pedir_numero("Promedio: ", decimal=True)()

    estudiantes[matricula] = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "promedio": promedio,
    }
    print("  ✔ Estudiante agregado.")