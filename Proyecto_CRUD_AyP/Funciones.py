"""
Aquí se almacenan las funciones que se utilizan para el proyecto CRUD
"""

estudiantes = {
    "A211548": {"nombre": "Ana López Fernández", "edad": 19, "carrera": "Mecatrónica", "promedio": 9.1},
    "A211235": {"nombre": "Luis Pérez García", "edad": 20, "carrera": "Sistemas", "promedio": 8.4},
}

campos = ["nombre", "edad", "carrera", "promedio"]

class pedir_numero:
    """
    Clase para pedir un número 
    """
    def __init__(self, mensaje, decimal=False):
        self.mensaje = mensaje
        self.decimal = decimal

    def __call__(self):
     while True:
        texto = input(self.mensaje).strip()
        try:
            if self.decimal:
                return float(texto)
            return int(texto)
        except ValueError:
            print("  ⚠ Escribe un número válido.")

def menu():
    """
    Función para mostrar el menú principal del programa.
    """
    print("=== Menú Principal ===")
    print("1. Crear estudiante")
    print("2. Buscar estudiante")
    print("3. Modificar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")
    return input("Seleccione una opción: ")

def agregar():
    """Pide los datos de un estudiante y los guarda."""
    matricula = input("Matrícula: ").strip().upper()
    if matricula in estudiantes:
        print("  ⚠ Esa matrícula ya existe.")
        return
    nombre = input("Nombre Completo (Nombre/Apellido Paterno/Apellido Materno): ").strip()
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

def actualizar():
    """Actualiza los datos de un estudiante existente buscandolo por matricula."""
    matricula = input("Matrícula del estudiante a actualizar: ").strip().upper()
    if matricula not in estudiantes:
        print("  ⚠ No se encontró esa matrícula.")
        return

    print(f"El usuario que desea actualizar es: {estudiantes[matricula]['nombre']} ?") 
    input_usuario = input("Ingrese 'si' para continuar o 'no' para cancelar: ").strip().lower()
    if input_usuario != "si":
        print("  ❌ Actualización cancelada.")
        return
    datos = estudiantes[matricula]
    continuar = True
    while continuar:
        print("  ¿Qué campo desea actualizar?")
        print("1) Nombre   2) Edad   3) Carrera   4) Promedio   5) Terminar")
        opcion = input("Tu elección: ").strip()

        if opcion == "1":
            nuevo = input("Nuevo nombre: ").strip()
            if nuevo == "":
                print("  ⚠ No se puede dejar vacío.")
            else:
                datos["nombre"] = nuevo
                print("  ✔ Nombre actualizado.")
        elif opcion == "2":
            edad_act = pedir_numero("Nueva edad: ")()
            if edad_act < 0:
                print("  ⚠ La edad no puede ser negativa o quedarse vacía.")
            else:
                datos["edad"] = edad_act
                print("  ✔ Edad actualizada.")
        elif opcion == "3":
            nuevo = input("Nueva carrera: ").strip()
            if nuevo == "":
                print("  ⚠ No se puede dejar vacío.")
            else:
                datos["carrera"] = nuevo
                print("  ✔ Carrera actualizada.")
        elif opcion == "4":
            promedio_act = pedir_numero("Nuevo promedio: ", decimal=True)()
            if promedio_act < 0:
                print("  ⚠ El promedio no puede ser negativo o quedarse vacío.")
            else:
                datos["promedio"] = promedio_act
                print("  ✔ Promedio actualizado.")
        elif opcion == "5":
            continuar = False