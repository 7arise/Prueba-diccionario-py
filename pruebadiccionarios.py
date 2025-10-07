def agregar():
    clave = input("\nEscriba el nombre: ")
    valor = input("Escriba la edad: ")
    dicc.setdefault(clave, valor)
    
def eliminar():
    clave = input("\nEscriba el nombre a eliminar: ")
    print("Eliminando %s . . . %s" % (clave, dicc.pop(clave, "No encontrado")))
    
def listar():
    print("\nContenido del diccionario:", dicc)
    print("\nnombres".ljust(15) + "edades".rjust(5))
    for clave in dicc.items():
        print(clave[0].ljust(15) + clave[1].rjust(5))
        
dicc = dict()
opcion = ""
while opcion !="0":
    print("\nMENU DE OPCIONES:")
    print("1 - Agregar elementos")
    print("2 - Eliminar elementos")
    print("3 - Listar contenido")
    print("0 - Salir")
    opcion = input("Escriba opción: ")
    match opcion:
        case "1":
            agregar()
        case "2":
            eliminar()
        case "3":
            listar()
        case "0":
            break
        case _:
            print("¡Opción incorrecta!")
print("Gracias por usar el programa")