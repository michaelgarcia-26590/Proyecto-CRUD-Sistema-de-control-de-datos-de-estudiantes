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

import Funciones

import tkinter as tk

#======================================Crear==========================================



continuar = True
while continuar:
    print()
    opcion = Funciones.menu().strip()

    if opcion == "1":
        Funciones.agregar()
        print(Funciones.estudiantes)  #Por ahora para comprobar que se agregan los estudiantes correctamente(Despues lo borramos)
    elif opcion in ("2", "3", "4"):
        print("  Esta opción todavía no está disponible.")
    elif opcion == "5":
        print("¡Hasta luego!")
        continuar = False
    else:
        print("  ⚠ Opción no válida, intenta de nuevo.")


