import tkinter as tk  # Importar el módulo tkinter para la interfaz gráfica
from tkinter import filedialog, messagebox, ttk  # Importar filedialog para abrir archivos, messagebox para mostrar mensajes emergentes, y ttk para widgets mejorados
import pandas as pd  # Importar pandas para manejar archivos de Excel

# Función para abrir y mostrar el contenido de un archivo de Excel
def open_excel_file():
    # Abrir diálogo para seleccionar el archivo de Excel
    file_path = filedialog.askopenfilename(title="Seleccionar archivo de Excel", filetypes=[("Excel files", "*.xlsx *.xls"), ("All files", "*.*")])
    if not file_path:
        return  # Salir de la función si no se selecciona archivo

    try:
        # Leer el archivo de Excel usando pandas
        df = pd.read_excel(file_path)
        
        # Crear una nueva ventana para mostrar los resultados
        result_window = tk.Toplevel(root)
        result_window.title("Contenido del Archivo de Excel")
        
        # Crear un Treeview para mostrar los registros
        tree = ttk.Treeview(result_window, show='headings')
        
        # Configurar las columnas del Treeview
        tree["columns"] = list(df.columns)  # Establecer las columnas en el Treeview con los nombres de las columnas del DataFrame
        for col in df.columns:
            tree.heading(col, text=col)  # Configurar los encabezados de las columnas con los nombres del DataFrame
            tree.column(col, width=100)  # Configurar el ancho de las columnas
        
        # Añadir los registros al Treeview
        for index, row in df.iterrows():
            tree.insert("", tk.END, values=list(row))  # Insertar cada fila del DataFrame en el Treeview
        
        tree.pack(fill=tk.BOTH, expand=True)  # Empacar el Treeview en la ventana y permitir que se expanda
    except Exception as e:  # Capturar errores
        messagebox.showerror("Error", f"Ocurrió un error: {e}")  # Mostrar mensaje de error si ocurre una excepción

# Crear la ventana principal
root = tk.Tk()  # Crear una instancia de Tk para la ventana principal
root.title("Abrir y Mostrar Archivo de Excel")  # Establecer el título de la ventana principal

# Botón para abrir el archivo de Excel
open_button = tk.Button(root, text="Seleccionar y Mostrar Archivo de Excel", command=open_excel_file)  # Crear un botón que llama a la función open_excel_file
open_button.pack(pady=20)  # Empacar el botón en la ventana principal con un margen vertical

# Ejecutar la aplicación
root.mainloop()  # Iniciar el bucle principal de la aplicación
