import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3

# Función para guardar los datos en la base de datos
def save_to_database():
    db_name = filedialog.asksaveasfilename(defaultextension=".db", filetypes=[("SQLite files", "*.db"), ("All files", "*.*")])
    if not db_name:
        return  # Salir de la función si no se selecciona archivo

    data = []
    for i in range(5):
        row_data = []
        for j in range(5):
            cell_value = entries[i][j].get()
            row_data.append(cell_value)
        data.append(tuple(row_data))

    try:
        # Conectar a la base de datos
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()  # Crear un cursor para ejecutar comandos SQL

        # Crear la tabla con 5 columnas
        cursor.execute("CREATE TABLE IF NOT EXISTS my_table (col1 TEXT, col2 TEXT, col3 TEXT, col4 TEXT, col5 TEXT)")

        # Insertar los datos en la tabla
        cursor.executemany("INSERT INTO my_table (col1, col2, col3, col4, col5) VALUES (?, ?, ?, ?, ?)", data)
        conn.commit()  # Confirmar los cambios
        conn.close()  # Cerrar la conexión a la base de datos

        messagebox.showinfo("Éxito", "Datos guardados exitosamente en la base de datos.")
    except sqlite3.Error as e:  # Capturar errores de SQLite
        messagebox.showerror("Error", f"Ocurrió un error: {e}")  # Mostrar mensaje de error

# Crear la ventana principal
root = tk.Tk()
root.title("Tabla de Datos 5x5")

# Crear una matriz de entradas
entries = []
for i in range(5):
    row_entries = []
    for j in range(5):
        entry = tk.Entry(root, width=10)
        entry.grid(row=i, column=j, padx=5, pady=5)
        row_entries.append(entry)
    entries.append(row_entries)

# Botón para guardar los datos en la base de datos
save_button = tk.Button(root, text="Guardar en Base de Datos", command=save_to_database)
save_button.grid(row=5, column=0, columnspan=5, pady=10)

# Ejecutar la aplicación
root.mainloop()
