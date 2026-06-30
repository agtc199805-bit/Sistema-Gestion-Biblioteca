# Sistema de Gestión de Biblioteca Inteligente
# Proyecto Integrador
usuarios = []
libros = []
prestamos = []
def registrar_usuario():
    cedula = input("Ingrese la cédula del usuario: ")
    nombre = input("Ingrese el nombre del usuario: ")
    usuario = {
        "cedula": cedula,
        "nombre": nombre
    }
    usuarios.append(usuario)
    print("Usuario registrado correctamente.")
def registrar_libro():
    codigo = input("Ingrese el código del libro: ")
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    libro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "estado": "Disponible"
    }
    libros.append(libro)
    print("Libro registrado correctamente.")
def mostrar_libros():
    if len(libros) == 0:
        print("No existen libros registrados.")
    else:
        print("\nLISTA DE LIBROS")
        for libro in libros:
            print("Código:", libro["codigo"])
            print("Título:", libro["titulo"])
            print("Autor:", libro["autor"])
            print("Estado:", libro["estado"])
            print("--------------------")
def buscar_libro():
    codigo = input("Ingrese el código del libro a buscar: ")
    encontrado = False
    for libro in libros:
        if libro["codigo"] == codigo:
            print("Libro encontrado:")
            print("Título:", libro["titulo"])
            print("Autor:", libro["autor"])
            print("Estado:", libro["estado"])
            encontrado = True
            break
    if encontrado == False:
        print("No se encontro el libro.")
def prestar_libro():
    cedula = input("Ingrese la cedula del usuario: ")
    codigo = input("Ingrese el codigo del libro: ")
    usuario_existe = False
    libro_existe = False
    for usuario in usuarios:
        if usuario["cedula"] == cedula:
            usuario_existe = True
            break
    for libro in libros:
        if libro["codigo"] == codigo:
            libro_existe = True
            if libro["estado"] == "Disponible":
                libro["estado"] = "Prestado"
                prestamo = {
                    "cedula": cedula,
                    "codigo": codigo
                }
                prestamos.append(prestamo)
                print("Prestamo registrado correctamente.")
            else:
                print("El libro ya se encuentra prestado.")
            break
    if usuario_existe == False:
        print("El usuario no esta registrado.")
    if libro_existe == False:
        print("El libro no esta registrado.")
def devolver_libro():
    codigo = input("Ingrese el codigo del libro a devolver: ")
    encontrado = False
    for libro in libros:
        if libro["codigo"] == codigo:
            encontrado = True
            if libro["estado"] == "Prestado":
                libro["estado"] = "Disponible"
                print("Libro devuelto correctamente.")
            else:
                print("El libro ya se encuentra disponible.")
            break
    if encontrado == False:
        print("No se encontro el libro.")
def mostrar_prestamos():
    if len(prestamos) == 0:
        print("No existen prestamos registrados.")
    else:
        print("\nHISTORIAL DE PRESTAMOS")
        for prestamo in prestamos:
            print("Cedula del usuario:", prestamo["cedula"])
            print("Codigo del libro:", prestamo["codigo"])
            print("--------------------")
def estadisticas():
    disponibles = 0
    prestados = 0
    for libro in libros:
        if libro["estado"] == "Disponible":
            disponibles += 1
        else:
            prestados += 1
    print("\nESTADISTICAS")
    print("Usuarios registrados:", len(usuarios))
    print("Libros registrados:", len(libros))
    print("Libros disponibles:", disponibles)
    print("Libros prestados:", prestados)
    print("Prestamos realizados:", len(prestamos))
def menu():
    while True:
        print("\n===== BIBLIOTECA INTELIGENTE =====")
        print("1. Registrar usuario")
        print("2. Registrar libro")
        print("3. Mostrar libros")
        print("4. Buscar libro")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Mostrar prestamos")
        print("8. Estadisticas")
        print("9. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            registrar_libro()
        elif opcion == "3":
            mostrar_libros()
        elif opcion == "4":
            buscar_libro()
        elif opcion == "5":
            prestar_libro()
        elif opcion == "6":
            devolver_libro()
        elif opcion == "7":
            mostrar_prestamos()
        elif opcion == "8":
            estadisticas()
        elif opcion == "9":
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Opcion incorrecta. Intente nuevamente.")
            continue
menu()