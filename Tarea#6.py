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

# Recolectar información del primer producto
id_ = (input("Ingrese un id: "))
nombre = input("Ingrese un nombre: ").lower()
precio = int(input("Ingrese un precio: "))
cantidad = int(input("Ingrese una cantidad: "))

# Agregar el primer producto a la lista
agregar_producto(lista_productos, id_, nombre, precio, cantidad)

# Preguntar si desea agregar más productos
desear = input("¿Desea agregar algo más? (si/no): ").lower()

while desear == "si":
    id_ = input("Ingrese un id: ")  
    nombre = input("Ingrese un nombre: ").lower()
    precio = int(input("Ingrese un precio: "))
    cantidad = int(input("Ingrese una cantidad: "))

    agregar_producto(lista_productos, id_, nombre, precio, cantidad)
    desear = input("¿Desea agregar algo más? (si/no): ").lower()
Lis=input("\nDesea imprimir lista(si/no)").lower()
if Lis=="si":
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
Bus=input("\nDesea buscar algun producto(si/no)")
if Bus=="si":
    buscar_productos(input("\nIngrese un producto a buscar: ").lower())


lista_productos.sort(key=lambda x: x["nombre"].lower())
ordi=("\nDesea ordenar la lista alfabéticamente(si/no)").lower()
if ordi=="si":
    print("\nLista de productos ordenada alfabéticamente:")
    imprimir_productos(lista_productos)

# Función para cambiar el nombre del producto

def cambiar_nombre_producto(lista, id_producto, nuevo_nombre):
    producto_encontrado = False
    for producto in lista:
        if producto["id"] == id_producto:  
            producto["nombre"] = nuevo_nombre
            producto_encontrado = True
            break

    if not producto_encontrado:
        print("No se encontró ningún producto con el ID proporcionado.")

cambio=input("\nDesea cambiar el nombre de algun producto(si/no)").lower()
if cambio=="si":
    id_producto_a_cambiar = (input("Ingrese el ID del producto que desea cambiar el nombre: "))
    nuevo_nombre_producto = input("Ingrese el nuevo nombre del producto: ")
    cambiar_nombre_producto(lista_productos, id_producto_a_cambiar, nuevo_nombre_producto)
    print("\nLista de productos actualizada:")
    imprimir_productos(lista_productos)
