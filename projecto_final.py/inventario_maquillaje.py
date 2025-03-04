# Diccionario para almacenar el inventario
inventario = {
    "Lapiz Delineador": {"Cantidad": 7, "Precio": 40},
    "Paleta de Sombras": {"Cantidad": 10, "Precio": 25},
    "Base Liquida": {"Cantidad": 5, "Precio": 30},
    "Iluminador": {"Cantidad": 5, "Precio": 20},
    "Pestañina": {"Cantidad": 20, "Precio": 17}
}

def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Actualizar cantidad de producto")
    print("4. Actualizar precio de producto")
    print("5. Eliminar producto")
    print("6. Salir")

def ver_inventario():
    if not inventario:
        print("El inventario está vacío.")
        return
    
    print("\n--- Inventario ---")
    print(f"{'Producto':<15} {'Cantidad':<10} {'Precio':<10}")
    for producto, detalles in inventario.items():
        print(f"{producto:<15} {detalles['Cantidad']:<10} ${detalles['Precio']:<10.3f}")

def agregar_producto():
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio unitario: "))
    if cantidad < 0 or precio < 0:
        print("La cantidad y el precio no pueden ser negativos.")
        return
    elif producto in inventario:
        print("El producto ya existe en el inventario.")
    else:
        inventario[producto] = {'Cantidad': cantidad, 'Precio': precio}
        print(f"Producto '{producto}' agregado con {cantidad} unidades y un precio de ${precio:.3f}.")

def actualizar_cantidad():
    producto = input("Ingrese el nombre del producto: ")
    if producto in inventario:
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        if nueva_cantidad < 0:
            print("La cantidad no puede ser negativa.")
            return
        inventario[producto]['Cantidad'] = nueva_cantidad
        print(f"Cantidad de '{producto}' actualizada a {nueva_cantidad} unidades.")
    else:
        print("El producto no existe en el inventario.")

def actualizar_precio():
    producto = input("Ingrese el nombre del producto: ")
    if producto in inventario:
        nuevo_precio = float(input("Ingrese el nuevo precio unitario: "))
        if nuevo_precio < 0:
            print("El precio no puede ser negativo.")
            return
        inventario[producto]['Precio'] = nuevo_precio
        print(f"Precio de '{producto}' actualizado a ${nuevo_precio:.3f}.")
    else:
        print("El producto no existe en el inventario.")

def eliminar_producto():
    producto = input("Ingrese el nombre del producto: ")
    if producto in inventario:
        del inventario[producto]
        print(f"Producto '{producto}' eliminado del inventario.")
    else:
        print("El producto no existe en el inventario.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_inventario()
        elif opcion == "3":
            actualizar_cantidad()
        elif opcion == "4":
            actualizar_precio()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            print("Saliendo del sistema de inventario...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()