import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3

def save_to_database():
    # Abrir diálogo para guardar el archivo de base de datos
    file_path = filedialog.asksaveasfilename(defaultextension=".db", filetypes=[("SQLite files", "*.db"), ("All files", "*.*")])
    if not file_path:
        return  # Salir de la función si no se selecciona archivo

    try:
        # Conectar a la base de datos (se crea si no existe)
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()  # Crear un cursor para ejecutar comandos SQL

        # Crear la tabla
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS data_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                column1 TEXT,
                column2 TEXT,
                column3 TEXT,
                column4 TEXT,
                column5 TEXT
            )
        """)

        # Insertar los datos de la tabla en la base de datos
        for i in range(5):
            row_data = [entries[i][j].get() for j in range(5)]
            cursor.execute("INSERT INTO data_table (column1, column2, column3, column4, column5) VALUES (?, ?, ?, ?, ?)", row_data)

        conn.commit()  # Confirmar los cambios
        conn.close()  # Cerrar la conexión a la base de datos

        messagebox.showinfo("Éxito", "Datos guardados exitosamente en la base de datos.")
    except sqlite3.Error as e:  # Capturar errores de SQLite
        messagebox.showerror("Error", f"Ocurrió un error: {e}")  # Mostrar mensaje de error

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz Gráfica para Base de Datos 5x5")

# Crear una lista para almacenar las entradas de la tabla
entries = []

# Crear etiquetas de encabezado de columna
for j in range(5):
    tk.Label(root, text=f"column{j+1}", padx=5, pady=5).grid(row=0, column=j)

# Crear entradas para la tabla 5x5
for i in range(5):
    row_entries = []
    for j in range(5):
        entry = tk.Entry(root, width=10)
        entry.grid(row=i+1, column=j, padx=1, pady=1)
        row_entries.append(entry)
    entries.append(row_entries)

# Botón para guardar los datos en la base de datos
save_button = tk.Button(root, text="Guardar en Base de Datos", command=save_to_database)
save_button.grid(row=6, column=0, columnspan=5, pady=10)

# Ejecutar la aplicación
root.mainloop()

