"""Proyecto final de La asignatura Algoritmos y programación

Equipo:
 Michael Gabriel García Ortiz
 Oscar Alejandro Orta Rodriguez
 Diego Camil Picazo Zubiri

==========================================================
 CRUD DE ESTUDIANTES
C = Create (Crear) R = Read (Leer/Buscar)
U = Update (Editar) D = Delete (Eliminar)
==========================================================
"""

from logging import config
from Interfaz import VentanaEstudiantes

import Funciones

import tkinter as tk

#======================================Crear==========================================


#Menú para probar las funciones del proyecto
#Imprime en consola, no es la interfaz final
"""continuar = True
while continuar:
    print()
    opcion = Funciones.menu().strip()

    if opcion == "1":
        Funciones.agregar()
        print(Funciones.estudiantes)  #Por ahora para comprobar que se agregan los estudiantes correctamente(Despues lo borramos)
    elif opcion == "2":
        Funciones.buscar()
    elif opcion == "3":
        Funciones.actualizar()
    elif opcion == "5":
        print("¡Hasta luego!")
        continuar = False
    elif opcion == "4":
        Funciones.eliminar()
    else:
        print("  ⚠ Opción no válida, intenta de nuevo.")"""

#Interfaz final y real del proyecto

Funciones.cargar_estudiantes()

app = VentanaEstudiantes()
app.iniciar()
