"""
Aquí se almacenan las funciones que se utilizan para el proyecto CRUD
"""
import json
import os

CARPETA = os.path.dirname(os.path.abspath(__file__))

ARCHIVO_JSON = os.path.join(CARPETA, "estudiantes.json")
ARCHIVO_TXT = os.path.join(CARPETA, "estudiantes.txt")

#Hay que procurar tener siempre alumnos
#para poder hacer pruebas
estudiantes = {
    "A211548": {"correo": "ana.lopez@example.com", 
                "nombre": "Ana López Fernández", 
                "edad": 19, 
                "carrera": "Mecatrónica", 
                "semestre": 5, 
                "promedio": 9.1},
    "A211235": {"correo": "luis.perez@example.com", 
                "nombre": "Luis Pérez García", 
                "edad": 20, 
                "carrera": "Sistemas", 
                "semestre": 4, 
                "promedio": 8.4},
}

campos = ["correo", "nombre", "edad", "carrera", "semestre", "promedio"]

def guardar_estudiantes():
    """Aqui guardamos los estudiantes en un archivo JSON."""
    with open(ARCHIVO_JSON, "w") as archivo:
        json.dump(estudiantes, archivo, indent=4)

def cargar_estudiantes():
    """Aqui cargamos los estudiantes desde un archivo JSON."""
    global estudiantes
    try:
        with open(ARCHIVO_JSON, "r") as archivo:
            estudiantes = json.load(archivo)
    except FileNotFoundError:
        print("  ⚠ No se encontró el archivo de estudiantes. Se creará uno nuevo al guardar.")
    except json.JSONDecodeError:
        print("  ⚠ El archivo de estudiantes está corrupto. Se creará uno nuevo al guardar.")

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
    correo = input("Correo: ").strip()
    nombre = input("Nombre Completo (Nombre/Apellido Paterno/Apellido Materno): ").strip()
    edad = pedir_numero("Edad: ")()
    carrera = input("Carrera: ").strip()
    semestre = pedir_numero("Semestre: ")()
    promedio = pedir_numero("Promedio: ", decimal=True)()

    estudiantes[matricula] = {
        "nombre": nombre,
        "correo": correo,
        "edad": edad,
        "carrera": carrera,
        "semestre": semestre,
        "promedio": promedio
    }
    print("  ✔ Estudiante agregado.")

def mostrar_estudiante(matricula):
    """Imprime los datos de un solo estudiante."""
    datos = estudiantes[matricula]
    print(f"  Matrícula: {matricula}")
    for campo in campos:
        print(f"  {campo.capitalize()}: {datos[campo]}")

def mostrar_en_orden():
    """Mostramos los estudiantes en el ordden elegido por el usuario."""
    print("  Ordenar por: a) Nombre   b) Promedio")
    opcion_campo = input("Campo: ").strip().lower()
    if opcion_campo == "a":
        campo = "nombre"
    elif opcion_campo == "b":
        campo = "promedio"
    else:
        print("  ⚠ Opción no válida.")
        return

    print("  Orden: 1) Ascendente   2) Descendente")
    opcion_orden = input("Orden: ").strip()
    if opcion_orden not in ("1", "2"):
        print("  ⚠ Opción no válida.")
        return
    descendente = opcion_orden == "2"

    lista = []
    for matricula in estudiantes:
        valor = estudiantes[matricula][campo]
        if campo == "nombre":
            valor = valor.lower() 
        lista.append((valor, matricula))
    lista.sort(reverse=descendente)

    for valor, matricula in lista:
        mostrar_estudiante(matricula)
        print("  ---")

def buscar():
    """Busca estudiantes por matrícula, nombre o carrera."""
    print("1) Por matrícula   2) Por nombre   3) Por carrera  " \
    " 4) Mostrar todos   5) Mostrarlos en orden  6) Volver")
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
    elif opcion == "4":
        for matricula in estudiantes:
            mostrar_estudiante(matricula)
            print("  ---")
    elif opcion == "5":
        mostrar_en_orden()  
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
        print("1) Nombre   2) Edad   3) Carrera 4)Semestre  5) Promedio   6) Terminar")
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
            semestre_act = pedir_numero("Nuevo semestre: ")()
            if semestre_act < 0:
                print("  ⚠ El semestre no puede ser negativo o quedarse vacío.")
            else:
                datos["semestre"] = semestre_act
                print("  ✔ Semestre actualizado.")
        elif opcion == "5":
            promedio_act = pedir_numero("Nuevo promedio: ", decimal=True)()
            if promedio_act < 0:
                print("  ⚠ El promedio no puede ser negativo o quedarse vacío.")
            else:
                datos["promedio"] = promedio_act
                print("  ✔ Promedio actualizado.")
        elif opcion == "6":
            continuar = False

def eliminar():
    """Elimina un estudiante existente buscandolo por matricula."""
    matricula = input("Matrícula del estudiante a eliminar: ").strip().upper()
    if matricula not in estudiantes:
        print("  ⚠ No se encontró esa matrícula.")
        return

    print(f"El usuario que desea eliminar es: {estudiantes[matricula]['nombre']} ?") 
    input_usuario = input("Ingrese 'si' para continuar o 'no' para cancelar: ").strip().lower()
    if input_usuario != "si":
        print("  ❌ Eliminación cancelada.")
        return

    del estudiantes[matricula]
    print("  ✔ Estudiante eliminado.")

def guardar_en_txt():
    """Guarda los estudiantes en un archivo de texto."""
    with open(ARCHIVO_TXT, "w") as archivo:
        for matricula, datos in estudiantes.items():
            linea = f"{matricula},{datos['correo']},{datos['nombre']},{datos['edad']},{datos['carrera']},{datos['semestre']},{datos['promedio']}\n"
            archivo.write(linea)
    print(f"  ✔ Estudiantes guardados en {ARCHIVO_TXT}.")

#Funciones para el JSON

def comprobar_datos_paraJson(datos):
    """Revisa los datos que registra
    en el archivo JSON e imprime mensajes de errro
    si encuentra algún dato incorrecto
    """
    for clave in datos:
        if datos[clave]=="":
            return "  ⚠ La matrícula no puede estar vacía."
    try:
        edad= int(datos["edad"])
    except ValueError:
        return "  ⚠ La edad debe ser un número entero."
    if edad < 0:
        return "  ⚠ La edad no puede ser negativa."
    try:
        semestre= int(datos["semestre"])
    except ValueError:
        return "  ⚠ El semestre debe ser un número entero."
    if semestre < 0:
        return "  ⚠ El semestre no puede ser negativo."
    
    try:
        promedio= float(datos["promedio"])
    except ValueError:
        return "  ⚠ El promedio debe ser un número decimal entre 1.0 y 10.0."
    if promedio < 1.0 or promedio > 10.0:
        return "  ⚠ El promedio debe estar entre 1.0 y 10.0."

    correo = datos["correo"]
    if "@" not in correo or "." not in correo:
        return "  ⚠ El correo electrónico no es válido."

    return ""

def registrar_estudiante_json(datos):
    """Registra un estudiante en el archivo JSON."""
    matricula = datos["matricula"]
    estudiantes[matricula] = {
        "correo": datos["correo"],
        "nombre": datos["nombre"],
        "edad": int(datos["edad"]),
        "carrera": datos["carrera"],
        "semestre": int(datos["semestre"]),
        "promedio": float(datos["promedio"])
    }
    guardar_estudiantes()
    return "  ✔ Estudiante agregado."

def eliminar_estudiante_json(matricula):
    """Elimina un estudiante del archivo JSON."""
    if matricula not in estudiantes:
        return "  ⚠ No se encontró esa matrícula."
    del estudiantes[matricula]
    guardar_estudiantes()
    return "  ✔ Estudiante eliminado."