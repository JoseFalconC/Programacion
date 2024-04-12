def imprimir_productos(lista):
    print("ID\tNombre\tPrecio\tCantidad")
    for producto in lista:
        print("{}\t{}\t{}\t{}".format(producto["id"], producto["nombre"], producto["precio"], producto["cantidad"]))

def agregar_producto(lista, id_, nombre, precio, cantidad):
    inventario = {
        "id": id_,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
    }
    lista.append(inventario)
    return lista

lista_productos = []

id_ = input("Ingrese un id: ")
nombre = input("Ingrese un nombre: ")
precio = int(input("Ingrese un precio: "))
cantidad = int(input("Ingrese una cantidad: "))

agregar_producto(lista_productos, id_, nombre, precio, cantidad)

desear = input("¿Desea agregar algo más? (si/no): ").lower()

while desear == "si":
    id_ = int(input("Ingrese un id: "))
    nombre = input("Ingrese un nombre: ").lower()
    precio = int(input("Ingrese un precio: "))
    cantidad = int(input("Ingrese una cantidad: "))

    agregar_producto(lista_productos, id_, nombre, precio, cantidad)
    desear = input("¿Desea agregar algo más? (si/no): ").lower()

print("\nLista de productos actualizada:")
imprimir_productos(lista_productos)

def buscar_productos(nombre):
    termino = False  
    print("ID\tNombre\tPrecio\tCantidad")  
    for producto in lista_productos:
        if nombre in producto["nombre"]:
            termino = True
            print(f"{producto['id']}\t{producto['nombre']}\t{producto['precio']}\t{producto['cantidad']}")
    if not termino:
        print("\nEl producto no se encuentra.")


buscar_productos(input("\nIngrese un producto a buscar").lower())
