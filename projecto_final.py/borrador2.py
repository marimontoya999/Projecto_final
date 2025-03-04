import customtkinter as ctk

# Inicialización del inventario
inventario = []

# Funciones del inventario
def agregar_producto():
    nombre = nombre_entry.get()
    cantidad = int(cantidad_entry.get())
    precio = float(precio_entry.get())
    inventario.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    resultado_label.configure(text=f"{nombre} agregado al inventario.")
    limpiar_campos()

def ver_inventario():
    if not inventario:
        resultado_label.configure(text="El inventario está vacío.")
    else:
        inventario_str = "\nInventario:\n"
        for producto in inventario:
            inventario_str += f"- {producto['nombre']}: Cantidad={producto['cantidad']}, Precio={producto['precio']}\n"
        resultado_label.configure(text=inventario_str)

def actualizar_cantidad():
    nombre = nombre_actualizar_entry.get()
    for producto in inventario:
        if producto["nombre"] == nombre:
            producto["cantidad"] = int(nueva_cantidad_entry.get())
            resultado_label.configure(text=f"Cantidad de {nombre} actualizada.")
            limpiar_campos_actualizar()
            return
    resultado_label.configure(text="Producto no encontrado.")
    limpiar_campos_actualizar()

def actualizar_precio():
    nombre = nombre_actualizar_entry.get()
    for producto in inventario:
        if producto["nombre"] == nombre:
            producto["precio"] = float(nuevo_precio_entry.get())
            resultado_label.configure(text=f"Precio de {nombre} actualizado.")
            limpiar_campos_actualizar()
            return
    resultado_label.configure(text="Producto no encontrado.")
    limpiar_campos_actualizar()

def eliminar_producto():
    nombre = nombre_eliminar_entry.get()
    for producto in inventario:
        if producto["nombre"] == nombre:
            inventario.remove(producto)
            resultado_label.configure(text=f"{nombre} eliminado del inventario.")
            limpiar_campos_eliminar()
            return
    resultado_label.configure(text="Producto no encontrado.")
    limpiar_campos_eliminar()

def limpiar_campos():
    nombre_entry.delete(0, "end")
    cantidad_entry.delete(0, "end")
    precio_entry.delete(0, "end")

def limpiar_campos_actualizar():
    nombre_actualizar_entry.delete(0, "end")
    nueva_cantidad_entry.delete(0, "end")
    nuevo_precio_entry.delete(0, "end")

def limpiar_campos_eliminar():
    nombre_eliminar_entry.delete(0, "end")

# Configuración de la ventana principal
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("600x400")
root.title("Sistema de Inventario")
root.configure(bg="#FFD1DC")  # Baby pink background

# Colores personalizados
color_fondo = "#FFD1DC"  # Baby pink
color_boton = "#B7EA93"  # Pastel green
color_texto = "#FFFFFF"  # White

# Widgets para agregar producto
nombre_label = ctk.CTkLabel(root, text="Nombre:", text_color=color_texto, bg_color=color_fondo)
nombre_label.grid(row=0, column=0, padx=10, pady=5)
nombre_entry = ctk.CTkEntry(root, fg_color=color_fondo)
nombre_entry.grid(row=0, column=1, padx=10, pady=5)

cantidad_label = ctk.CTkLabel(root, text="Cantidad:", text_color=color_texto, bg_color=color_fondo)
cantidad_label.grid(row=1, column=0, padx=10, pady=5)
cantidad_entry = ctk.CTkEntry(root, fg_color=color_fondo)
cantidad_entry.grid(row=1, column=1, padx=10, pady=5)

precio_label = ctk.CTkLabel(root, text="Precio:", text_color=color_texto, bg_color=color_fondo)
precio_label.grid(row=2, column=0, padx=10, pady=5)
precio_entry = ctk.CTkEntry(root, fg_color=color_fondo)
precio_entry.grid(row=2, column=1, padx=10, pady=5)

agregar_button = ctk.CTkButton(root, text="Agregar", command=agregar_producto, fg_color=color_boton, text_color="black")
agregar_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Widgets para actualizar cantidad
nombre_actualizar_label = ctk.CTkLabel(root, text="Nombre a actualizar:", text_color=color_texto, bg_color=color_fondo)
nombre_actualizar_label.grid(row=4, column=0, padx=10, pady=5)
nombre_actualizar_entry = ctk.CTkEntry(root, fg_color=color_fondo)
nombre_actualizar_entry.grid(row=4, column=1, padx=10, pady=5)

nueva_cantidad_label = ctk.CTkLabel(root, text="Nueva cantidad:", text_color=color_texto, bg_color=color_fondo)
nueva_cantidad_label.grid(row=5, column=0, padx=10, pady=5)
nueva_cantidad_entry = ctk.CTkEntry(root, fg_color=color_fondo)
nueva_cantidad_entry.grid(row=5, column=1, padx=10, pady=5)

actualizar_cantidad_button = ctk.CTkButton(root, text="Actualizar Cantidad", command=actualizar_cantidad, fg_color=color_boton, text_color="black")
actualizar_cantidad_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Widgets para actualizar precio
nuevo_precio_label = ctk.CTkLabel(root, text="Nuevo precio:", text_color=color_texto, bg_color=color_fondo)
nuevo_precio_label.grid(row=7, column=0, padx=10, pady=5)
nuevo_precio_entry = ctk.CTkEntry(root, fg_color=color_fondo)
nuevo_precio_entry.grid(row=7, column=1, padx=10, pady=5)

actualizar_precio_button = ctk.CTkButton(root, text="Actualizar Precio", command=actualizar_precio, fg_color=color_boton, text_color="black")
actualizar_precio_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

# Widgets para eliminar producto
nombre_eliminar_label = ctk.CTkLabel(root, text="Nombre a eliminar:", text_color=color_texto, bg_color=color_fondo)
nombre_eliminar_label.grid(row=9, column=0, padx=10, pady=5)
nombre_eliminar_entry = ctk.CTkEntry(root, fg_color=color_fondo)
nombre_eliminar_entry.grid(row=9, column=1, padx=10, pady=5)

eliminar_button = ctk.CTkButton(root, text="Eliminar", command=eliminar_producto, fg_color=color_boton, text_color="black")
eliminar_button.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

# Widget para ver inventario
ver_inventario_button = ctk.CTkButton(root, text="Ver Inventario", command=ver_inventario, fg_color=color_boton, text_color="black")
ver_inventario_button.grid(row=11, column=0, columnspan=2, padx=10, pady=5)

# Label para mostrar resultados
resultado_label = ctk.CTkLabel(root, text="", text_color=color_texto, bg_color=color_fondo)
resultado_label.grid(row=12, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()