import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import sqlite3

def open_database():
    # Abrir diálogo para seleccionar el archivo de base de datos
    file_path = filedialog.askopenfilename(title="Seleccionar archivo de base de datos", filetypes=[("SQLite files", "*.db"), ("All files", "*.*")])
    if not file_path:
        return  # Salir de la función si no se selecciona archivo

    try:
        # Conectar a la base de datos
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()  # Crear un cursor para ejecutar comandos SQL

        # Obtener el nombre de las tablas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        if not tables:
            messagebox.showwarning("Advertencia", "La base de datos no contiene tablas.")
            return

        # Seleccionar la primera tabla encontrada
        table_name = tables[0][0]

        # Obtener todos los registros de la tabla seleccionada
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()  # Recuperar todos los registros
        conn.close()  # Cerrar la conexión a la base de datos

        if not rows:
            messagebox.showwarning("Advertencia", "La tabla está vacía.")
            return  # Salir de la función si la tabla está vacía

        # Crear una nueva ventana para mostrar los resultados
        result_window = tk.Toplevel(root)
        result_window.title("Contenido de la Base de Datos")

        # Crear un Treeview para mostrar los registros
        tree = ttk.Treeview(result_window, show='headings')

        # Configurar las columnas del Treeview utilizando los primeros valores de cada columna como nombres de columnas
        columns = ["Columna " + str(i + 1) for i in range(len(rows[0]))]
        tree["columns"] = columns

        for i, column_name in enumerate(columns):
            tree.heading(column_name, text=rows[0][i])
            tree.column(column_name, width=100)

        # Añadir los registros al Treeview (excluyendo la primera fila que contiene los nombres de columnas)
        for row in rows[1:]:
            tree.insert("", tk.END, values=row)

        tree.pack(fill=tk.BOTH, expand=True)
    except sqlite3.Error as e:  # Capturar errores de SQLite
        messagebox.showerror("Error", f"Ocurrió un error: {e}")  # Mostrar mensaje de error

# Crear la ventana principal
root = tk.Tk()
root.title("Abrir y Mostrar Base de Datos SQLite")

# Botón para abrir y mostrar el contenido de la base de datos
open_button = tk.Button(root, text="Seleccionar y Mostrar Base de Datos", command=open_database)
open_button.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
