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
    print("2. Buscar estudiante")
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

def mostrar_estudiante(matricula):
    """Imprime los datos de un solo estudiante."""
    datos = estudiantes[matricula]
    print(f"  Matrícula: {matricula}")
    for campo in campos:
        print(f"  {campo.capitalize()}: {datos[campo]}")


def buscar():
    """Busca estudiantes por matrícula, nombre o carrera."""
    print("1) Por matrícula   2) Por nombre   3) Por carrera  " \
    " 4) Mostrar todos   5) Mostrarlos en orden por...   6) Volver")#La opción 5 aun hay que definirla les toca decidir por cual campo se ordena y si es ascendente o descendente
    opcion = input("Opción: ").strip()

    if opcion == "1":
        matricula = input("Matrícula: ").strip().upper()
        if matricula in estudiantes:
            mostrar_estudiante(matricula)
        else:
            print("  ⚠ No se encontró esa matrícula.")

    elif opcion in ("2", "3"):
        # Nombre o carrera, según lo que eligió
        campo = "nombre" if opcion == "2" else "carrera"
        texto = input(f"{campo.capitalize()}: ").strip().lower()
        if texto == "":
            print("  ⚠ Escribe algo para buscar.")
            return

        encontrados = []
        for matricula, datos in estudiantes.items():
            if texto in datos[campo].lower():
                encontrados.append(matricula)

        if len(encontrados) == 0:
            print("  ⚠ No hubo coincidencias.")
        else:
            print(f"  Se encontraron {len(encontrados)} resultado(s):")
            for matricula in encontrados:
                mostrar_estudiante(matricula)
                print("  ---")
    elif opcion in ("4", "5"):
        print("  Esta opción todavía no está disponible.")
    elif opcion == "6":
        return
    else:
        print("  ⚠ Opción no válida.")