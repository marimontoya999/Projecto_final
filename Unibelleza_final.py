from datetime import datetime
import customtkinter as ctk

# Configuración de CustomTkinter
ctk.set_appearance_mode("light")  # Modo claro
ctk.set_default_color_theme("blue")  # Tema base

# Colores personalizados
PINK_COLOR = "#FFB6C1"  # Pastel pink
PINK_HOVER = "#FFC0CB"  # Lighter pink
WHITE_COLOR = "#FFFFFF"  # White color
WHITE_HOVER = "#F0F0F0"  # Light grey for hover
BLACK_TEXT = "#000000"  # Black color for text

# Diccionario para almacenar el inventario con categorías
inventario = {
    "maquillaje": {
        "lapiz delineador": {"Cantidad": 7, "Precio": 40, "Vencimiento": "2025-08-15"},
        "paleta de sombras": {"Cantidad": 10, "Precio": 250, "Vencimiento": "2026-02-10"},
        "base liquida": {"Cantidad": 5, "Precio": 30, "Vencimiento": "2024-12-30"},
        "iluminador": {"Cantidad": 5, "Precio": 20, "Vencimiento": "2026-05-20"},
        "pestañina": {"Cantidad": 20, "Precio": 17, "Vencimiento": "2025-06-10"},
        "labial mate": {"Cantidad": 15, "Precio": 50, "Vencimiento": "2026-09-15"},
        "corrector liquido": {"Cantidad": 12, "Precio": 35, "Vencimiento": "2025-12-01"},
        "rubor en polvo": {"Cantidad": 8, "Precio": 45, "Vencimiento": "2026-07-18"},
        "primer facial": {"Cantidad": 6, "Precio": 60, "Vencimiento": "2026-03-22"}
    },
    "skincare": {
        "crema hidratante": {"Cantidad": 20, "Precio": 80, "Vencimiento": "2026-01-20"},
        "serum vitamina C": {"Cantidad": 10, "Precio": 100, "Vencimiento": "2025-11-05"},
        "protector solar SPF 50": {"Cantidad": 15, "Precio": 90, "Vencimiento": "2025-07-15"},
        "tonico facial": {"Cantidad": 12, "Precio": 55, "Vencimiento": "2026-04-10"},
        "agua micelar": {"Cantidad": 18, "Precio": 50, "Vencimiento": "2026-08-05"},
        "aceite limpiador": {"Cantidad": 10, "Precio": 65, "Vencimiento": "2025-09-01"}
    },
    "uñas": {
        "esmalte rojo": {"Cantidad": 20, "Precio": 20, "Vencimiento": "N/A"},
        "esmalte nude": {"Cantidad": 18, "Precio": 25, "Vencimiento": "N/A"},
        "quitaesmalte": {"Cantidad": 15, "Precio": 15, "Vencimiento": "N/A"},
        "lima de uñas": {"Cantidad": 25, "Precio": 10, "Vencimiento": "N/A"}
    },
    "accesorios": {
        "brocha para base": {"Cantidad": 10, "Precio": 35, "Vencimiento": "N/A"},
        "esponja de maquillaje": {"Cantidad": 15, "Precio": 20, "Vencimiento": "N/A"},
        "pinza para cejas": {"Cantidad": 8, "Precio": 15, "Vencimiento": "N/A"},
        "cepillo para pestañas": {"Cantidad": 10, "Precio": 12, "Vencimiento": "N/A"},
        "neceser de maquillaje": {"Cantidad": 5, "Precio": 100, "Vencimiento": "N/A"},
    }
}

# Diccionario para almacenar usuarios registrados
usuarios = {}

# Historial de ventas
historial_ventas = []

# REGISTRAR USUARIO
def registrar_usuario(usuarios):
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo electrónico: ")
    telefono = input("Ingrese su número de teléfono: ")
    direccion = input("Ingrese su dirección: ")

    if correo in usuarios:
        print(f"El correo '{correo}' ya está registrado.")
    else:
        usuarios[correo] = {"nombre": nombre, "telefono": telefono, "direccion": direccion}
        print(f"Usuario '{nombre}' registrado correctamente.")

# VER INVENTARIO
def ver_inventario(inventario, usuarios):
    """Muestra el inventario con fechas de vencimiento y aplica descuento si el usuario está registrado."""
    hoy = datetime.now().date()
    correo_usuario = input("Ingrese su correo electrónico (o presione Enter si no está registrado): ")
    descuento = 0.10 if correo_usuario in usuarios else 0

    print("\n--- Inventario ---")
    for categoria, productos in inventario.items():
        print(f"\n📌 Categoría: {categoria.capitalize()}")
        print("{:<25} {:<10} {:>10} {:>15}".format("Producto", "Cantidad", "$Precio", "Vencimiento"))
        for producto, detalles in productos.items():
            precio_con_descuento = detalles['Precio'] * (1 - descuento)
            vencimiento = detalles.get("Vencimiento", "N/A")
            if vencimiento != "N/A":
                fecha_venc = datetime.strptime(vencimiento, "%Y-%m-%d").date()
                if fecha_venc < hoy:
                    continue  # Omitir productos vencidos
            else:
                vencimiento = "Sin vencimiento"
            print("{:<25} {:<10} {:>10.2f} {:>15}".format(producto, detalles['Cantidad'], precio_con_descuento, vencimiento))

    if descuento > 0:
        print("\n¡Se aplicó un descuento del 10% por estar registrado!🩷")
    print("\nNota: Los productos vencidos no se muestran en el inventario.")

# BUSCAR PRODUCTO
def buscar_producto(inventario):
    producto = input("Ingrese el nombre del producto a buscar: ").lower()
    encontrado = False

    for categoria, productos in inventario.items():
        if producto in productos:
            detalles = productos[producto]
            print(f"\n--- Detalles de '{producto}' ---")
            print(f"Categoría: {categoria.capitalize()}")
            print(f"Cantidad: {detalles['Cantidad']}")
            print(f"Precio: ${detalles['Precio']:.2f}")
            encontrado = True
            break

    if not encontrado:
        print(f"El producto '{producto}' no existe en el inventario.")

# AGREGAR PRODUCTO
def agregar_producto(inventario):
    categoria = input("Ingrese la categoría: ").lower()
    if categoria not in inventario:
        print("Categoría inválida.")
        return

    producto = input("Ingrese el nombre del producto: ").lower()
    if producto in inventario[categoria]:
        print("El producto ya existe.")
        return

    try:
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio unitario: "))
        if cantidad < 0 or precio < 0:
            raise ValueError
    except ValueError:
        print("La cantidad y el precio deben ser valores positivos.")
        return

    inventario[categoria][producto] = {"Cantidad": cantidad, "Precio": precio}
    print(f"Producto '{producto}' agregado correctamente.")

# ACTUALIZAR CANTIDAD
def actualizar_cantidad(inventario):
    producto = input("Ingrese el nombre del producto: ").lower()
    for categoria, productos in inventario.items():
        if producto in productos:
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            productos[producto]['Cantidad'] = nueva_cantidad
            print(f"Cantidad de '{producto}' actualizada a {nueva_cantidad}.")
            return
    print(f"El producto '{producto}' no existe en el inventario.")

# ACTUALIZAR PRECIO
def actualizar_precio(inventario):
    producto = input("Ingrese el nombre del producto: ").lower()
    for categoria, productos in inventario.items():
        if producto in productos:
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            productos[producto]['Precio'] = nuevo_precio
            print(f"Precio de '{producto}' actualizado a ${nuevo_precio:.2f}.")
            return
    print(f"El producto '{producto}' no existe en el inventario.")

# ELIMINAR PRODUCTO
def eliminar_producto(inventario):
    producto = input("Ingrese el nombre del producto: ").lower()
    for categoria, productos in inventario.items():
        if producto in productos:
            del productos[producto]
            print(f"Producto '{producto}' eliminado.")
            return
    print(f"El producto '{producto}' no existe en el inventario.")

# REGISTRAR VENTA
def registrar_venta(inventario, usuarios):
    producto = input("Ingrese el nombre del producto vendido: ").lower()
    for categoria, productos in inventario.items():
        if producto in productos:
            try:
                cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
                if cantidad_vendida < 0:
                    print("La cantidad vendida no puede ser negativa.")
                    return
                if cantidad_vendida > productos[producto]["Cantidad"]:
                    print("No hay suficiente inventario para esta venta.")
                    return
                productos[producto]["Cantidad"] -= cantidad_vendida
                total = cantidad_vendida * productos[producto]["Precio"]
                fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Solicitar el correo del usuario que realiza la venta
                correo_usuario = input("Ingrese el correo electrónico del usuario que realiza la venta: ")
                if correo_usuario in usuarios:
                    nombre_usuario = usuarios[correo_usuario]["nombre"]
                else:
                    nombre_usuario = "Usuario no registrado"

                # Agregar el usuario al registro de ventas
                historial_ventas.append({
                    "Producto": producto,
                    "Cantidad": cantidad_vendida,
                    "Total": total,
                    "Fecha": fecha,
                    "Usuario": nombre_usuario
                })
                print(f"Venta registrada: {cantidad_vendida} x '{producto}' = ${total:.2f} (Vendido por: {nombre_usuario})")
                return
            except ValueError:
                print("Cantidad inválida.")
                return
    print("Producto no encontrado.")

# VER HISTORIAL DE VENTAS
def ver_historial_ventas():
    if not historial_ventas:
        print("No hay ventas registradas.")
        return

    print("\n--- Historial de Ventas ---")
    print("{:<20} {:<10} {:<10} {:<20} {:<20}".format("Producto", "Cantidad", "Total", "Fecha", "Usuario"))
    for venta in historial_ventas:
        print("{:<20} {:<10} {:<10.2f} {:<20} {:<20}".format(
            venta['Producto'], venta['Cantidad'], venta['Total'], venta['Fecha'], venta['Usuario']
        ))

# Clase principal de la aplicación
class InventarioApp(ctk.CTk):
    def __init__(self):
        super(InventarioApp, self).__init__()
        self.title("Sistema de Inventario")
        self.geometry("800x600")
        
        # Configurar colores de la ventana
        self.configure(fg_color="white")

        # Crear pestañas con estilo personalizado
        self.tabview = ctk.CTkTabview(self, fg_color=PINK_COLOR)
        self.tabview.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestañas disponibles
        self.tabview.add("Ver Inventario")
        self.tabview.add("Registrar Usuario")
        self.tabview.add("Buscar Producto")
        self.tabview.add("Agregar Producto")
        self.tabview.add("Actualizar Cantidad")
        self.tabview.add("Actualizar Precio")
        self.tabview.add("Eliminar Producto")
        self.tabview.add("Registrar Venta")
        self.tabview.add("Historial de Ventas")

        # Widgets para cada pestaña
        self._crear_pestaña_ver_inventario()
        self._crear_pestaña_registrar_usuario()
        self._crear_pestaña_buscar_producto()
        self._crear_pestaña_agregar_producto()
        self._crear_pestaña_actualizar_cantidad()
        self._crear_pestaña_actualizar_precio()
        self._crear_pestaña_eliminar_producto()
        self._crear_pestaña_registrar_venta()
        self._crear_pestaña_historial_ventas()

    # Pestaña: Ver Inventario
    def _crear_pestaña_ver_inventario(self):
        frame = self.tabview.tab("Ver Inventario")

        self.correo_label = ctk.CTkLabel(frame, text="Correo electrónico (opcional):")
        self.correo_label.pack(pady=5)

        self.correo_entry = ctk.CTkEntry(frame, width=300)
        self.correo_entry.pack(pady=5)

        self.ver_inventario_button = ctk.CTkButton(
            frame, 
            text="Ver Inventario",
            command=self._ver_inventario,
            fg_color=WHITE_COLOR,
            hover_color=WHITE_HOVER,
            text_color=BLACK_TEXT
        )
        self.ver_inventario_button.pack(pady=10)

        self.inventario_text = ctk.CTkTextbox(frame, width=700, height=400)
        self.inventario_text.pack(pady=10)

    def _ver_inventario(self):
        correo = self.correo_entry.get()
        self.inventario_text.delete("1.0", "end")  # Limpiar el texto anterior
        hoy = datetime.now().date()
        descuento = 0.10 if correo in usuarios else 0

        for categoria, productos in inventario.items():
            self.inventario_text.insert("end", f"\n📌 Categoría: {categoria.capitalize()}\n")
            self.inventario_text.insert("end", "{:<25} {:<10} {:>10} {:>15}\n".format(
                "Producto", "Cantidad", "$Precio", "Vencimiento"
            ))
            for producto, detalles in productos.items():
                precio_con_descuento = detalles['Precio'] * (1 - descuento)
                vencimiento = detalles.get("Vencimiento", "N/A")
                if vencimiento != "N/A":
                    fecha_venc = datetime.strptime(vencimiento, "%Y-%m-%d").date()
                    if fecha_venc < hoy:
                        continue  # Omitir productos vencidos
                else:
                    vencimiento = "Sin vencimiento"
                self.inventario_text.insert("end", "{:<25} {:<10} {:>10.2f} {:>15}\n".format(
                    producto, detalles['Cantidad'], precio_con_descuento, vencimiento
                ))

        if descuento > 0:
            self.inventario_text.insert("end", "\n¡Se aplicó un descuento del 10% por estar registrado!🩷\n")
        self.inventario_text.insert("end", "\nNota: Los productos vencidos no se muestran en el inventario.\n")

    # Pestaña: Registrar Usuario
    def _crear_pestaña_registrar_usuario(self):
        frame = self.tabview.tab("Registrar Usuario")

        self.nombre_label = ctk.CTkLabel(frame, text="Nombre:")
        self.nombre_label.pack(pady=5)

        self.nombre_entry = ctk.CTkEntry(frame, width=300)
        self.nombre_entry.pack(pady=5)

        self.correo_label = ctk.CTkLabel(frame, text="Correo electrónico:")
        self.correo_label.pack(pady=5)

        self.correo_entry = ctk.CTkEntry(frame, width=300)
        self.correo_entry.pack(pady=5)

        self.telefono_label = ctk.CTkLabel(frame, text="Teléfono:")
        self.telefono_label.pack(pady=5)

        self.telefono_entry = ctk.CTkEntry(frame, width=300)
        self.telefono_entry.pack(pady=5)

        self.direccion_label = ctk.CTkLabel(frame, text="Dirección:")
        self.direccion_label.pack(pady=5)

        self.direccion_entry = ctk.CTkEntry(frame, width=300)
        self.direccion_entry.pack(pady=5)

        self.registrar_button = ctk.CTkButton(
            frame, 
            text="Registrar Usuario",
            command=self._registrar_usuario,
            fg_color=WHITE_COLOR,
            hover_color=WHITE_HOVER,
            text_color=BLACK_TEXT
        )
        self.registrar_button.pack(pady=10)

    def _registrar_usuario(self):
        nombre = self.nombre_entry.get()
        correo = self.correo_entry.get()
        telefono = self.telefono_entry.get()
        direccion = self.direccion_entry.get()

        if correo in usuarios:
            self.mostrar_mensaje("Error", f"El correo '{correo}' ya está registrado.")
        else:
            usuarios[correo] = {"nombre": nombre, "telefono": telefono, "direccion": direccion}
            self.mostrar_mensaje("Éxito", f"Usuario '{nombre}' registrado correctamente.")

    # Pestaña: Buscar Producto
    def _crear_pestaña_buscar_producto(self):
        frame = self.tabview.tab("Buscar Producto")

        self.buscar_producto_label = ctk.CTkLabel(frame, text="Nombre del producto:")
        self.buscar_producto_label.pack(pady=5)

        self.buscar_producto_entry = ctk.CTkEntry(frame, width=300)
        self.buscar_producto_entry.pack(pady=5)

        self.buscar_button = ctk.CTkButton(
            frame, 
            text="Buscar Producto",
            command=self._buscar_producto,
            fg_color=WHITE_COLOR,
            hover_color=WHITE_HOVER,
            text_color=BLACK_TEXT
        )
        self.buscar_button.pack(pady=10)

        self.buscar_resultado_text = ctk.CTkTextbox(frame, width=700, height=200)
        self.buscar_resultado_text.pack(pady=10)

    def _buscar_producto(self):
        producto = self.buscar_producto_entry.get().lower()
        encontrado = False

        for categoria, productos in inventario.items():
            if producto in productos:
                detalles = productos[producto]
                self.buscar_resultado_text.delete("1.0", "end")
                self.buscar_resultado_text.insert("end", f"\n--- Detalles de '{producto}' ---\n")
                self.buscar_resultado_text.insert("end", f"Categoría: {categoria.capitalize()}\n")
                self.buscar_resultado_text.insert("end", f"Cantidad: {detalles['Cantidad']}\n")
                self.buscar_resultado_text.insert("end", f"Precio: ${detalles['Precio']:.2f}\n")
                encontrado = True
                break

        if not encontrado:
            self.mostrar_mensaje("Error", f"El producto '{producto}' no existe en el inventario.")

    # Pestaña: Agregar Producto
    def _crear_pestaña_agregar_producto(self):
        frame = self.tabview.tab("Agregar Producto")

        self.categoria_label = ctk.CTkLabel(frame, text="Categoría:")
        self.categoria_label.pack(pady=5)

        self.categoria_entry = ctk.CTkEntry(frame, width=300)
        self.categoria_entry.pack(pady=5)

        self.producto_label = ctk.CTkLabel(frame, text="Nombre del producto:")
        self.producto_label.pack(pady=5)

        self.producto_entry = ctk.CTkEntry(frame, width=300)
        self.producto_entry.pack(pady=5)

        self.cantidad_label = ctk.CTkLabel(frame, text="Cantidad:")
        self.cantidad_label.pack(pady=5)

        self.cantidad_entry = ctk.CTkEntry(frame, width=300)
        self.cantidad_entry.pack(pady=5)

        self.precio_label = ctk.CTkLabel(frame, text="Precio:")
        self.precio_label.pack(pady=5)

        self.precio_entry = ctk.CTkEntry(frame, width=300)
        self.precio_entry.pack(pady=5)

        self.agregar_button = ctk.CTkButton(
            frame, 
            text="Agregar Producto",
            command=self._agregar_producto,
            fg_color=WHITE_COLOR,
            hover_color=WHITE_HOVER,
            text_color=BLACK_TEXT
        )
        self.agregar_button.pack(pady=10)

    def _agregar_producto(self):
        categoria = self.categoria_entry.get().lower()
        producto = self.producto_entry.get().lower()
        cantidad = self.cantidad_entry.get()
        precio = self.precio_entry.get()

        if categoria not in inventario:
            self.mostrar_mensaje("Error", "Categoría inválida.")
            return

        if producto in inventario[categoria]:
            self.mostrar_mensaje("Error", "El producto ya existe.")
            return

        try:
            cantidad = int(cantidad)
            precio = float(precio)
            if cantidad < 0 or precio < 0:
                raise ValueError
        except ValueError:
            self.mostrar_mensaje("Error", "La cantidad y el precio deben ser valores positivos.")
            return

        inventario[categoria][producto] = {"Cantidad": cantidad, "Precio": precio}
        self.mostrar_mensaje("Éxito", f"Producto '{producto}' agregado correctamente.")

    # Pestaña: Actualizar Cantidad
    def _crear_pestaña_actualizar_cantidad(self):
        frame = self.tabview.tab("Actualizar Cantidad")

        self.actualizar_cantidad_label = ctk.CTkLabel(frame, text="Nombre del producto:")
        self.actualizar_cantidad_label.pack(pady=5)

        self.actualizar_cantidad_entry = ctk.CTkEntry(frame, width=300)
        self.actualizar_cantidad_entry.pack(pady=5)

        self.nueva_cantidad_label = ctk.CTkLabel(frame, text="Nueva cantidad:")
        self.nueva_cantidad_label.pack(pady=5)

        self.nueva_cantidad_entry = ctk.CTkEntry(frame, width=300)
        self.nueva_cantidad_entry.pack(pady=5)

        self.actualizar_cantidad_button = ctk.CTkButton(
            frame, 
            text="Actualizar Cantidad",
            command=self._actualizar_cantidad,
            fg_color=WHITE_COLOR,
            hover_color=WHITE_HOVER,
            text_color=BLACK_TEXT
        )
        self.actualizar_cantidad_button.pack(pady=10)

    def _actualizar_cantidad(self):
        producto = self.actualizar_cantidad_entry.get().lower()
        nueva_cantidad = self.nueva_cantidad_entry.get()

        try:
            nueva_cantidad = int(nueva_cantidad)
        except ValueError:
            self.mostrar_mensaje("Error", "La cantidad debe ser un número entero.")
            return

        for categoria, productos in inventario.items():
            if producto in productos:
                productos[producto]['Cantidad'] = nueva_cantidad
                self.mostrar_mensaje("Éxito", f"Cantidad de '{producto}' actualizada a {nueva_cantidad}.")
                return

        self.mostrar_mensaje("Error", f"El producto '{producto}' no existe en el inventario.")

    # Pestaña: Actualizar Precio
    def _crear_pestaña_actualizar_precio(self):
        frame = self.tabview.tab("Actualizar Precio")

        self.actualizar_precio_label = ctk.CTkLabel(frame, text="Nombre del producto:")
        self.actualizar_precio_label.pack(pady=5)

        self.actualizar_precio_entry = ctk.CTkEntry(frame, width=300)
        self.actualizar_precio_entry.pack(pady=5)

        self.nuevo_precio_label = ctk.CTkLabel(frame, text="Nuevo precio:")
        self.nuevo_precio_label.pack(pady=5)

        self.nuevo_precio_entry = ctk.CTkEntry(frame, width=300)
        self.nuevo_precio_entry.pack(pady=5)

        self.actualizar_precio_button = ctk.CTkButton(
            frame, 
            text="Actualizar Precio",
            command=self._actualizar_precio,
            fg_color=WHITE_COLOR,
            hover_color=WHITE_HOVER,
            text_color=BLACK_TEXT
        )
        self.actualizar_precio_button.pack(pady=10)

    def _actualizar_precio(self):
        producto = self.actualizar_precio_entry.get().lower()
        nuevo_precio = self.nuevo_precio_entry.get()

        try:
            nuevo_precio = float(nuevo_precio)
        except ValueError:
            self.mostrar_mensaje("Error", "El precio debe ser un número.")
            return

        for categoria, productos in inventario.items():
            if producto in productos:
                productos[producto]['Precio'] = nuevo_precio
                self.mostrar_mensaje("Éxito", f"Precio de '{producto}' actualizado a ${nuevo_precio:.2f}.")
                return

        self.mostrar_mensaje("Error", f"El producto '{producto}' no existe en el inventario.")

    # Pestaña: Eliminar Producto
    def _crear_pestaña_eliminar_producto(self):
        frame = self.tabview.tab("Eliminar Producto")

        self.eliminar_producto_label = ctk.CTkLabel(frame, text="Nombre del producto:")
        self.eliminar_producto_label.pack(pady=5)

        self.eliminar_producto_entry = ctk.CTkEntry(frame, width=300)
        self.eliminar_producto_entry.pack(pady=5)

        self.eliminar_button = ctk.CTkButton(
            frame, 
            text="Eliminar Producto",
            command=self._eliminar_producto,
            fg_color=WHITE_COLOR,
            hover_color=WHITE_HOVER,
            text_color=BLACK_TEXT
        )
        self.eliminar_button.pack(pady=10)

    def _eliminar_producto(self):
        producto = self.eliminar_producto_entry.get().lower()

        for categoria, productos in inventario.items():
            if producto in productos:
                del productos[producto]
                self.mostrar_mensaje("Éxito", f"Producto '{producto}' eliminado.")
                return

        self.mostrar_mensaje("Error", f"El producto '{producto}' no existe en el inventario.")

    # Pestaña: Registrar Venta
    def _crear_pestaña_registrar_venta(self):
        frame = self.tabview.tab("Registrar Venta")

        self.registrar_venta_label = ctk.CTkLabel(frame, text="Nombre del producto:")
        self.registrar_venta_label.pack(pady=5)

        self.registrar_venta_entry = ctk.CTkEntry(frame, width=300)
        self.registrar_venta_entry.pack(pady=5)

        self.cantidad_venta_label = ctk.CTkLabel(frame, text="Cantidad vendida:")
        self.cantidad_venta_label.pack(pady=5)

        self.cantidad_venta_entry = ctk.CTkEntry(frame, width=300)
        self.cantidad_venta_entry.pack(pady=5)

        self.correo_venta_label = ctk.CTkLabel(frame, text="Correo del usuario:")
        self.correo_venta_label.pack(pady=5)

        self.correo_venta_entry = ctk.CTkEntry(frame, width=300)
        self.correo_venta_entry.pack(pady=5)

        self.registrar_venta_button = ctk.CTkButton(
            frame, 
            text="Registrar Venta",
            command=self._registrar_venta,
            fg_color=WHITE_COLOR,
            hover_color=WHITE_HOVER,
            text_color=BLACK_TEXT
        )
        self.registrar_venta_button.pack(pady=10)

    def _registrar_venta(self):
        producto = self.registrar_venta_entry.get().lower()
        cantidad_vendida = self.cantidad_venta_entry.get()
        correo_usuario = self.correo_venta_entry.get()

        try:
            cantidad_vendida = int(cantidad_vendida)
        except ValueError:
            self.mostrar_mensaje("Error", "La cantidad vendida debe ser un número entero.")
            return

        for categoria, productos in inventario.items():
            if producto in productos:
                if cantidad_vendida > productos[producto]["Cantidad"]:
                    self.mostrar_mensaje("Error", "No hay suficiente inventario para esta venta.")
                    return
                productos[producto]["Cantidad"] -= cantidad_vendida
                total = cantidad_vendida * productos[producto]["Precio"]
                fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                if correo_usuario in usuarios:
                    nombre_usuario = usuarios[correo_usuario]["nombre"]
                else:
                    nombre_usuario = "Usuario no registrado"

                historial_ventas.append({
                    "Producto": producto,
                    "Cantidad": cantidad_vendida,
                    "Total": total,
                    "Fecha": fecha,
                    "Usuario": nombre_usuario
                })
                self.mostrar_mensaje("Éxito", f"Venta registrada: {cantidad_vendida} x '{producto}' = ${total:.2f} (Vendido por: {nombre_usuario})")
                return

        self.mostrar_mensaje("Error", f"El producto '{producto}' no existe en el inventario.")

    # Pestaña: Historial de Ventas
    def _crear_pestaña_historial_ventas(self):
        frame = self.tabview.tab("Historial de Ventas")

        self.historial_ventas_text = ctk.CTkTextbox(frame, width=700, height=400)
        self.historial_ventas_text.pack(pady=10)

        self.actualizar_historial_button = ctk.CTkButton(
            frame, 
            text="Actualizar Historial",
            command=self._actualizar_historial_ventas,
            fg_color=WHITE_COLOR,
            hover_color=WHITE_HOVER,
            text_color=BLACK_TEXT
        )
        self.actualizar_historial_button.pack(pady=10)

    def _actualizar_historial_ventas(self):
        self.historial_ventas_text.delete("1.0", "end")
        if not historial_ventas:
            self.historial_ventas_text.insert("end", "No hay ventas registradas.")
            return

        self.historial_ventas_text.insert("end", "\n--- Historial de Ventas ---\n")
        self.historial_ventas_text.insert("end", "{:<20} {:<10} {:<10} {:<20} {:<20}\n".format(
            "Producto", "Cantidad", "Total", "Fecha", "Usuario"
        ))
        for venta in historial_ventas:
            self.historial_ventas_text.insert("end", "{:<20} {:<10} {:<10.2f} {:<20} {:<20}\n".format(
                venta['Producto'], venta['Cantidad'], venta['Total'], venta['Fecha'], venta['Usuario']
            ))

    def mostrar_mensaje(self, titulo, mensaje):
        ctk.CTkToplevel(self, title=titulo).label(text=mensaje).pack(pady=10)

# MOSTRAR MENÚ
def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Actualizar cantidad de producto")
    print("4. Actualizar precio de producto")
    print("5. Eliminar producto")
    print("6. Buscar producto")
    print("7. Registrar usuario")
    print("8. Registrar venta")
    print("9. Ver historial de ventas")
    print("10. Salir")

# DICCIONARIO DE FUNCIONES
opciones = {
    '1': lambda: agregar_producto(inventario),
    '2': lambda: ver_inventario(inventario, usuarios),
    '3': lambda: actualizar_cantidad(inventario),
    '4': lambda: actualizar_precio(inventario),
    '5': lambda: eliminar_producto(inventario),
    '6': lambda: buscar_producto(inventario),
    '7': lambda: registrar_usuario(usuarios),
    '8': lambda: registrar_venta(inventario, usuarios),
    '9': lambda: ver_historial_ventas()
}

# EJECUTAR MENÚ
def main():
    app = InventarioApp()
    app.mainloop()

if __name__ == "__main__":
    main()
