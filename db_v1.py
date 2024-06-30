import tkinter as tk  # Importar el módulo tkinter para la interfaz gráfica
from tkinter import messagebox  # Importar messagebox para mostrar mensajes emergentes
import sqlite3  # Importar el módulo sqlite3 para manejar bases de datos SQLite

# Función para crear la base de datos y la tabla
def create_database():
    db_name = entry_db_name.get()  # Obtener el nombre de la base de datos del campo de entrada
    table_name = entry_table_name.get()  # Obtener el nombre de la tabla del campo de entrada
    column1 = entry_column1.get()  # Obtener el nombre de la primera columna del campo de entrada
    column2 = entry_column2.get()  # Obtener el nombre de la segunda columna del campo de entrada

    # Verificar si todos los campos están llenos
    if not db_name or not table_name or not column1 or not column2:
        messagebox.showwarning("Advertencia", "Todos los campos deben ser llenados.")  # Mostrar advertencia si faltan campos
        return  # Salir de la función si faltan campos

    try:
        # Conectar a la base de datos (se crea si no existe)
        conn = sqlite3.connect(f"{db_name}.db")  
        cursor = conn.cursor()  # Crear un cursor para ejecutar comandos SQL

        # Crear la tabla con las columnas especificadas
        cursor.execute(f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {column1} TEXT, {column2} TEXT)")
        conn.commit()  # Confirmar los cambios
        conn.close()  # Cerrar la conexión a la base de datos

        messagebox.showinfo("Éxito", f"Base de datos '{db_name}.db' y tabla '{table_name}' creadas exitosamente.")  # Mostrar mensaje de éxito
    except sqlite3.Error as e:  # Capturar errores de SQLite
        messagebox.showerror("Error", f"Ocurrió un error: {e}")  # Mostrar mensaje de error

# Crear la ventana principal
root = tk.Tk()  # Crear una instancia de Tk
root.title("Creador de Base de Datos SQLite")  # Establecer el título de la ventana

# Etiquetas y entradas de texto
tk.Label(root, text="Nombre de la base de datos:").grid(row=0, column=0, padx=10, pady=5)  # Etiqueta para el nombre de la base de datos
entry_db_name = tk.Entry(root)  # Campo de entrada para el nombre de la base de datos
entry_db_name.grid(row=0, column=1, padx=10, pady=5)  # Ubicación del campo de entrada

tk.Label(root, text="Nombre de la tabla:").grid(row=1, column=0, padx=10, pady=5)  # Etiqueta para el nombre de la tabla
entry_table_name = tk.Entry(root)  # Campo de entrada para el nombre de la tabla
entry_table_name.grid(row=1, column=1, padx=10, pady=5)  # Ubicación del campo de entrada

tk.Label(root, text="Nombre de la columna 1:").grid(row=2, column=0, padx=10, pady=5)  # Etiqueta para el nombre de la columna 1
entry_column1 = tk.Entry(root)  # Campo de entrada para el nombre de la columna 1
entry_column1.grid(row=2, column=1, padx=10, pady=5)  # Ubicación del campo de entrada

tk.Label(root, text="Nombre de la columna 2:").grid(row=3, column=0, padx=10, pady=5)  # Etiqueta para el nombre de la columna 2
entry_column2 = tk.Entry(root)  # Campo de entrada para el nombre de la columna 2
entry_column2.grid(row=3, column=1, padx=10, pady=5)  # Ubicación del campo de entrada

# Botón para crear la base de datos
create_button = tk.Button(root, text="Crear Base de Datos", command=create_database)  # Crear un botón que llama a create_database
create_button.grid(row=4, column=0, columnspan=2, pady=20)  # Ubicación del botón

# Ejecutar la aplicación
root.mainloop()  # Iniciar el bucle principal de la aplicación
