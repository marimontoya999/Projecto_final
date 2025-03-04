import customtkinter as ctk
from tkinter import messagebox, ttk

# Configuración de colores y fuente
color_fondo = "#FFD1DC"  # Rosa pastel
color_boton = "#B7ea93"  # Verde pastel
color_texto = "#FFFFFF"  # Blanco
fuente = ("Times New Roman", 12)

# Crear interfaz gráfica con customtkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Inventario de Tienda de Maquillaje")
root.geometry("700x500")
root.configure(bg=color_fondo)

frame = ctk.CTkFrame(root, fg_color=color_fondo)
frame.pack(pady=10)

# Entradas y etiquetas
ctk.CTkLabel(frame, text="Nombre:", text_color="black", font=fuente).grid(row=0, column=0, padx=10, pady=5)
entry_nombre = ctk.CTkEntry(frame, font=fuente)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

ctk.CTkLabel(frame, text="Cantidad:", text_color="black", font=fuente).grid(row=1, column=0, padx=10, pady=5)
entry_cantidad = ctk.CTkEntry(frame, font=fuente)
entry_cantidad.grid(row=1, column=1, padx=10, pady=5)

ctk.CTkLabel(frame, text="Precio:", text_color="black", font=fuente).grid(row=2, column=0, padx=10, pady=5)
entry_precio = ctk.CTkEntry(frame, font=fuente)
entry_precio.grid(row=2, column=1, padx=10, pady=5)

# Funciones para manejar la lista de productos
productos = []

def agregar_producto():
    nombre = entry_nombre.get()
    cantidad = entry_cantidad.get()
    precio = entry_precio.get()
    if nombre and cantidad and precio:
        productos.append((nombre, cantidad, precio))
        messagebox.showinfo("Éxito", "Producto agregado correctamente")
        actualizar_lista()
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios")

def actualizar_lista():
    tree.delete(*tree.get_children())
    for prod in productos:
        tree.insert("", "end", values=prod)

def actualizar_cantidad():
    seleccion = tree.selection()
    if seleccion:
        item = tree.item(seleccion)
        index = tree.index(seleccion)
        productos[index] = (item['values'][0], entry_cantidad.get(), item['values'][2])
        messagebox.showinfo("Éxito", "Cantidad actualizada")
        actualizar_lista()
    else:
        messagebox.showwarning("Error", "Selecciona un producto")

def actualizar_precio():
    seleccion = tree.selection()
    if seleccion:
        item = tree.item(seleccion)
        index = tree.index(seleccion)
        productos[index] = (item['values'][0], item['values'][1], entry_precio.get())
        messagebox.showinfo("Éxito", "Precio actualizado")
        actualizar_lista()
    else:
        messagebox.showwarning("Error", "Selecciona un producto")

def eliminar_producto():
    seleccion = tree.selection()
    if seleccion:
        item = tree.item(seleccion)
        productos.remove(tuple(item['values']))
        messagebox.showinfo("Éxito", "Producto eliminado")
        actualizar_lista()
    else:
        messagebox.showwarning("Error", "Selecciona un producto")

# Botones
ctk.CTkButton(frame, text="Agregar", command=agregar_producto, fg_color=color_boton, text_color="black", font=fuente).grid(row=3, column=0, columnspan=2, pady=5)
ctk.CTkButton(frame, text="Actualizar Cantidad", command=actualizar_cantidad, fg_color=color_boton, text_color="black", font=fuente).grid(row=4, column=0, columnspan=2, pady=5)
ctk.CTkButton(frame, text="Actualizar Precio", command=actualizar_precio, fg_color=color_boton, text_color="black", font=fuente).grid(row=5, column=0, columnspan=2, pady=5)
ctk.CTkButton(frame, text="Eliminar", command=eliminar_producto, fg_color=color_boton, text_color="black", font=fuente).grid(row=6, column=0, columnspan=2, pady=5)

# Tabla para mostrar productos
tree_frame = ctk.CTkFrame(root, fg_color=color_fondo)
tree_frame.pack(pady=10)

columns = ("Nombre", "Cantidad", "Precio")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack()

actualizar_lista()
root.mainloop()
