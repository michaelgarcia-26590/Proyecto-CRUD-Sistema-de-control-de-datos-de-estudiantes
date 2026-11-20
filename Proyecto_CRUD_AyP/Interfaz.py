"""
Aqui construimos la interfaz de usuario para el proyecto CRUD
"""

import tkinter as tk
from tkinter import ttk, messagebox
 
import Funciones
 

CAMPOS_FORMULARIO = [
    ("ID IEST", "matricula"),
    ("Nombre", "nombre"),
    ("Correo", "correo"),
    ("Edad", "edad"),
    ("Carrera", "carrera"),
    ("Semestre", "semestre"),
    ("Promedio", "promedio"),
]
 
 
class VentanaEstudiantes:
    """Ventana principal del programa."""
 
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Registro y control de datos de estudiantes")
 

        self.entradas = {}
 
        self.crear_formulario()
        self.crear_botones()
        self.crear_tabla()
        self.mostrar_tabla()
 
    # ----------Ventana----------
    def crear_formulario(self):
        formulario = tk.Frame(self.ventana)
        formulario.pack(padx=20, pady=30)
 
        fila = 0
        for texto, clave in CAMPOS_FORMULARIO:
            tk.Label(formulario, text=texto + ":").grid(row=fila, column=0, sticky="e", padx=5, pady=3)
            entrada = tk.Entry(formulario, width=35)
            entrada.grid(row=fila, column=1, padx=5, pady=3)
            self.entradas[clave] = entrada
            fila = fila + 1
 
    def crear_botones(self):
        botones = tk.Frame(self.ventana)
        botones.pack(pady=10)
 
        tk.Button(botones, text="Guardar", width=12, command=self.guardar).grid(row=0, column=0, padx=5)
        tk.Button(botones, text="Buscar", width=12, command=self.buscar).grid(row=0, column=1, padx=5)
        tk.Button(botones, text="Eliminar", width=12, command=self.eliminar).grid(row=0, column=2, padx=5)
        tk.Button(botones, text="Imprimir", width=12, command=self.imprimir).grid(row=0, column=3, padx=5)
        tk.Button(botones, text="Limpiar", width=12, command=self.limpiar_campos).grid(row=0, column=4, padx=5)
 
    def crear_tabla(self):
        columnas = ("matricula", "nombre", "correo", "edad", "carrera", "semestre", "promedio")
        self.tabla = ttk.Treeview(self.ventana, columns=columnas, show="headings", height=8)
 
        self.tabla.heading("matricula", text="ID IEST")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("correo", text="Correo")
        self.tabla.heading("edad", text="Edad")
        self.tabla.heading("carrera", text="Carrera")
        self.tabla.heading("semestre", text="Semestre")
        self.tabla.heading("promedio", text="Promedio")
 
        self.tabla.column("matricula", width=80)
        self.tabla.column("nombre", width=180)
        self.tabla.column("correo", width=190)
        self.tabla.column("edad", width=50)
        self.tabla.column("carrera", width=110)
        self.tabla.column("semestre", width=70)
        self.tabla.column("promedio", width=70)
 
        self.tabla.pack(padx=20, pady=10)
        self.tabla.bind("<<TreeviewSelect>>", self.al_seleccionar)

    def leer_campos(self):
        """Regresa un diccionario con lo que hay en el formulario"""
        datos = {}
        for clave in self.entradas:
            datos[clave] = self.entradas[clave].get().strip()
        datos["matricula"] = datos["matricula"].upper()
        return datos
 
    def limpiar_campos(self):
        for clave in self.entradas:
            self.entradas[clave].delete(0, tk.END)
        self.entradas["matricula"].focus()
 
    def mostrar_datos(self, matricula):
        """Pone en el formulario los datos del estudiante con esa matrícula."""
        datos = Funciones.estudiantes[matricula]
        self.limpiar_campos()
        self.entradas["matricula"].insert(0, matricula)
        for clave in self.entradas:
            if clave != "matricula":
                self.entradas[clave].insert(0, str(datos[clave]))
 
    def mostrar_tabla(self):
        """Vacía la tabla y la vuelve a llenar con todos los estudiantes."""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for matricula in Funciones.estudiantes:
            datos = Funciones.estudiantes[matricula]
            self.tabla.insert("", tk.END, values=(matricula,
                                                  datos["nombre"],
                                                  datos["correo"],
                                                  datos["edad"],
                                                  datos["carrera"],
                                                  datos["semestre"],
                                                  datos["promedio"]))
 
    # ---------- Operaciones (botones) ----------
    def guardar(self):
        datos = self.leer_campos()
 
        error = Funciones.comprobar_datos_paraJson(datos)
        if error != "":
            messagebox.showwarning("Datos incorrectos", error)
            return
 
        # Hay que hacer que si la matrícula ya existe le pregunte si se quiere actualizar los datos
        if datos["matricula"] in Funciones.estudiantes:
            pregunta = f"La matrícula {datos['matricula']} ya existe. ¿Deseas actualizar sus datos?"
            if not messagebox.askyesno("Confirmar", pregunta):
                return
 
        resultado = Funciones.registrar_estudiante_json(datos)
        self.mostrar_tabla()
        self.limpiar_campos()
        messagebox.showinfo("Listo", f"Estudiante {resultado}.")
 
    def buscar(self):
        matricula = self.entradas["matricula"].get().strip().upper()
        if matricula == "":
            messagebox.showwarning("Falta la matrícula", "Escribe el ID IEST que quieres buscar.")
            return
 
        if matricula not in Funciones.estudiantes:
            messagebox.showerror("No encontrado", f"No existe ningún estudiante con el ID {matricula}.")
            return
 
        self.mostrar_datos(matricula)
 
    def eliminar(self):
        matricula = self.entradas["matricula"].get().strip().upper()
        if matricula == "":
            messagebox.showwarning("Falta la matrícula", "Escribe el ID IEST (o selecciona una fila de la tabla).")
            return
 
        if matricula not in Funciones.estudiantes:
            messagebox.showerror("No encontrado", f"No existe ningún estudiante con el ID {matricula}.")
            return
 
        nombre = Funciones.estudiantes[matricula]["nombre"]
        if messagebox.askyesno("Confirmar", f"¿Eliminar a {nombre}?"):
            Funciones.eliminar_estudiante_json(matricula)
            self.mostrar_tabla()
            self.limpiar_campos()
            messagebox.showinfo("Listo", "Estudiante eliminado.")
 
    def imprimir(self):
        if len(Funciones.estudiantes) == 0:
            messagebox.showwarning("Sin datos", "No hay estudiantes para imprimir.")
            return
 
        Funciones.guardar_en_txt()
        messagebox.showinfo("Listo", f"Estudiantes guardados en {Funciones.ARCHIVO_TXT}.")
 
    # ---------- Evento de la tabla ----------
    def al_seleccionar(self, evento):
        """Al hacer clic en una fila, sus datos pasan al formulario."""
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        indice = self.tabla.index(seleccion[0])
        matricula = list(Funciones.estudiantes)[indice]
        self.mostrar_datos(matricula)
 
    def iniciar(self):
        self.ventana.mainloop()
 
