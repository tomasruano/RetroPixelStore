import DatosTPO
import MenusTPO
import random


#Ignacio Diaz
def carga():
    print("1. Carga manual")
    print("2. Carga aleatoria")

    opcion = input("Seleccione una opción: ")

    while opcion != "1" and opcion != "2":
        opcion = input("Error. Ingrese 1 o 2: ")

    return opcion
#Ignacio Diaz
def generar_indice_aleatorio_lista(lista):
    indice = random.randint(0, len(lista) - 1)
    return indice
#Tomas Ruano
def buscar_indice(lista, valor):
    indice = -1
    for i in range(len(lista)):
        if lista[i].lower() == valor.lower():
            indice = i
            break
    return indice
#Ignacio Diaz
def cantidad_titulos_a_registrar(datos):
    cantidad = ingresar_entero_no_negativo("Ingrese la cantidad de productos a registrar: ")

    while cantidad <= 0:
        cantidad = ingresar_entero_no_negativo("Error. Ingrese una cantidad mayor a 0: ")

    return cantidad
#Tomas Ruano
def registrar_producto_aleatorio(datos):

    opciones_plataforma = datos[8]
    opciones_disponibilidad = datos[10]

    random_data = DatosTPO.obtener_titulos_y_categorias()

    titulos = random_data[0]
    categorias = random_data[1]

    titulos_disponibles = 0

    for i in range(len(titulos)):
        if not producto_duplicado(datos, titulos[i]):
            titulos_disponibles += 1

    if titulos_disponibles == 0:
        print("No hay más títulos disponibles para generar aleatoriamente.")
        return

    indice = generar_indice_aleatorio_lista(titulos)
    nuevo_titulo = titulos[indice]

    while producto_duplicado(datos, nuevo_titulo):
        indice = generar_indice_aleatorio_lista(titulos)
        nuevo_titulo = titulos[indice]

    nueva_categoria = categorias[indice]

    if indice <= 3:
        nuevo_contenido = "Videojuego"
    else:
        nuevo_contenido = "Pelicula"

    indice_plataforma = generar_indice_aleatorio_lista(opciones_plataforma)
    nueva_plataforma = opciones_plataforma[indice_plataforma]

    nuevo_precio = random.randint(1000, 100000)

    nuevo_stock = random.randint(0, 50)

    indice_disponibilidad = generar_indice_aleatorio_lista(opciones_disponibilidad)
    nueva_disponibilidad = opciones_disponibilidad[indice_disponibilidad]

    guardar_producto(
        datos,
        nuevo_titulo,
        nuevo_contenido,
        nueva_plataforma,
        nuevo_precio,
        nuevo_stock,
        nueva_categoria,
        nueva_disponibilidad
    )
    print("Producto agregado correctamente")
#Tomas Ruano
def registrar_producto_manual(datos):
    
    opciones_contenido = datos[7]
    opciones_plataforma = datos[8]
    opciones_categoria = datos[9]
    opciones_disponibilidad = datos[10]

    cantidad = cantidad_titulos_a_registrar(datos)
    for i in range(cantidad):
        print("-" * 50)
        print("Producto", i + 1)
        print("-" * 50)
        nuevo_titulo = pedir_titulo(datos)

        nuevo_contenido = ingresar_opcion_valida(
            "Ingrese el contenido: ",
            opciones_contenido
        )

        nueva_plataforma = ingresar_opcion_valida(
            "Ingrese la plataforma: ",
            opciones_plataforma
        )

        nuevo_precio = ingresar_float_positivo(
            "Ingrese el precio: "
        )

        nuevo_stock = ingresar_entero_no_negativo(
            "Ingrese el stock: "
        )

        nueva_categoria = ingresar_opcion_valida(
            "Ingrese la categoria: ",
            opciones_categoria
        )

        nueva_disponibilidad = ingresar_opcion_valida(
            "Ingrese la disponibilidad: ",
            opciones_disponibilidad
        )

        guardar_producto(
            datos,
            nuevo_titulo,
            nuevo_contenido,
            nueva_plataforma,
            nuevo_precio,
            nuevo_stock,
            nueva_categoria,
            nueva_disponibilidad
        )
        print("Producto agregado correctamente")
#Tomas Ruano
def registrar_producto(datos):

    opciones_contenido = datos[7]
    opciones_plataforma = datos[8]
    opciones_categoria = datos[9]
    opciones_disponibilidad = datos[10]

    opcion = carga()

    if opcion == "1":
        registrar_producto_manual(datos)

    else:

        registrar_producto_aleatorio(datos)
#Agustin Fani
def verificar_eliminables(stock, disponibilidad, titulo):
    print("Productos eliminables:")
    i = 0
    lista_eliminables = []
    while i < len(stock):
        if stock[i] == 0 and disponibilidad[i].lower() == "discontinuado":
            lista_eliminables.append(titulo[i])
        i += 1
    if len(lista_eliminables) == 0:
        print("No hay productos eliminables.")
        continuar=False
    else:
        for producto in lista_eliminables:
            print("- ", producto)
            continuar=True
    return continuar
#Agustin Fani
def eliminar_producto(datos):

    titulo = datos[0]
    contenido = datos[1]
    plataforma = datos[2]
    precio = datos[3]
    stock = datos[4]
    categoria = datos[5]
    disponibilidad = datos[6]

    continuar = True
    indice = -1

    continuar = verificar_eliminables(stock, disponibilidad, titulo)
    
    while continuar == True and indice == -1:
        titulo_buscado = input("Ingrese el titulo a eliminar o 'volver': ")

        if titulo_buscado.lower() == "volver":
            print("Volviendo al menu principal...")
            continuar = False
        else:
            indice = buscar_indice(titulo, titulo_buscado)

            if indice == -1:
                print("No se encontro el producto.")

    if continuar == True:

        if es_eliminable(stock, disponibilidad, indice):

            confirmacion = input("Confirma eliminar? (si/no): ")

            while confirmacion.lower() != "si" and confirmacion.lower() != "no":
                print("Opcion no valida. Ingrese 'si' para confirmar o 'no' para cancelar.")
                confirmacion = input("Confirma eliminar? (si/no): ")

            if confirmacion.lower() == "si":
                eliminar_por_indice(datos, indice)
                print("Producto eliminado correctamente.")
            else:
                print("Eliminacion cancelada.")

        else:
            print("No se puede eliminar el producto. ")
            print("El stock debe ser 0 y la disponibilidad debe ser 'Discontinuado'.")

#Tomas Sobrino
def aplicar_cambio_atributo(opcion, indice, datos):
    '''Modifica un atributo en el índice seleccionado de las listas paralelas'''
 #asignamos cada lista a una variable para facilitar la lectura del código
    titulo = datos[0]
    contenido = datos[1]
    plataforma = datos[2]
    precio = datos[3]
    stock = datos[4]
    categoria = datos[5]
    disponibilidad = datos[6]
 #listas de opciones para validar que lo que escriban sea correcto
    opciones_contenido = datos[7]
    opciones_plataforma = datos[8]
    opciones_categoria = datos[9]
    opciones_disponibilidad = datos[10]

    if opcion == "1":
        nuevo_titulo = input("Ingrese el nuevo título: ")
        while nuevo_titulo == "":
            nuevo_titulo = input("El título no puede estar vacío. Ingrese nuevo título: ")
        titulo[indice] = nuevo_titulo
    elif opcion == "2":
        contenido[indice] = ingresar_opcion_valida("Ingrese el nuevo contenido: ", opciones_contenido)
    elif opcion == "3":
        plataforma[indice] = ingresar_opcion_valida("Ingrese la nueva plataforma: ", opciones_plataforma)
    elif opcion == "4":
        precio[indice] = ingresar_float_positivo("Ingrese el nuevo precio: ")
    elif opcion == "5":
        stock[indice] = ingresar_entero_no_negativo("Ingrese el nuevo stock: ")
    elif opcion == "6":
        categoria[indice] = ingresar_opcion_valida("Ingrese la nueva categoría: ", opciones_categoria)
    elif opcion == "7":
        disponibilidad[indice] = ingresar_opcion_valida("Ingrese la nueva disponibilidad: ", opciones_disponibilidad)

    print("Producto modificado con éxito.")
#Tomas Sobrino
def modificar_producto(datos):
    '''Modifica un atributo controlando el flujo por banderas lógicas para cada paso.'''
    print("-" * 50)
    print("Modificar Producto")
    print("-" * 50)

    titulos = datos[0]
    #se usa continuar como bandera lógica
    continuar = True

    #verificamos que haya productos registrados
    if len(titulos) == 0:
        print("No hay productos registrados para modificar.")
        continuar = False

    #hace busqueda del título a modificar, si no lo encuentra vuelve a pedirlo, se puede salir escribiendo "volver"
    if continuar:
        # primero muestra los títulos registrados para que el usuario sepa qué escribir, si no hay productos registrados muestra un mensaje y vuelve al menú principal
        print("Títulos registrados actualmente:")
        i = 0
        while i < len(titulos):
            print("- " + titulos[i])
            i += 1
        print("-" * 50)

        # luego busca el índice del título ingresado en la lista de títulos, si no lo encuentra muestra un mensaje de error y vuelve a pedir el título, se puede salir escribiendo "volver"
        indice_elegido = -1
        titulo_valido = False
        
        while titulo_valido == False and continuar == True:
            titulo_buscado = input("Ingrese el título del producto a modificar o 'volver': ")
            
            if titulo_buscado.lower() == "volver":
                print("Volviendo al menú principal...")
                continuar = False
            else:
                # busca el índice del título ingresado en la lista de títulos, si no lo encuentra muestra un mensaje de error y vuelve a pedir el título
                indice_elegido = buscar_indice(titulos, titulo_buscado)
                
                if indice_elegido != -1:
                    titulo_valido = True
                else:
                    print("El título no se encuentra registrado. Intente nuevamente.")
    
    # si el título se encuentra, muestra el menú de atributos modificables y pide seleccionar uno, si la opción no es válida vuelve a pedirla, se puede salir escribiendo "volver"
    if continuar:
        MenusTPO.menu_modificar()
        opcion_valida = False

        while opcion_valida == False and continuar == True:
            opcion = input("Seleccione el número del atributo a modificar o 'volver': ")
            if opcion.lower() == "volver":
                print("Volviendo al menú principal...")
                continuar = False
            else:
                if existe_en_lista(["1", "2", "3", "4", "5", "6", "7"], opcion):
                    opcion_valida = True
                else:
                    print("Opción no válida. Debe ser entre 1 y 7.")
        #por ultimo, si se seleccionó una opción válida, se aplica el cambio en el atributo seleccionado del producto elegido usando la función aplicar_cambio_atributo
        if continuar:
            aplicar_cambio_atributo(opcion, indice_elegido, datos)


#Gaspar Divano  
def ordenamiento_burbuja(matriz):
       # Ordenamiento burbuja por stock y alfabéticamente por título en caso de empate
    for i in range(len(matriz) - 1):
        for j in range(len(matriz) - 1 - i):
            stock_actual    = matriz[j][4]
            stock_siguiente = matriz[j + 1][4]
            titulo_actual   = matriz[j][0]
            titulo_siguiente = matriz[j + 1][0]
            if (stock_actual < stock_siguiente) or (stock_actual == stock_siguiente and titulo_actual > titulo_siguiente):
            #Ordena el stock por orden descendente o en orden ascendente alfabeticamente
                aux          = matriz[j]
                matriz[j]     = matriz[j + 1]
                matriz[j + 1] = aux
#Gaspar Divano
def crear_matriz( titulo, contenido, plataforma, precio, stock, categoria, disponibilidad):
    '''crea una matriz a partir de las listas paralelas con los datos de los productos registrados. Cada fila de la matriz representa un producto y cada columna representa un atributo del producto.'''
    matriz = []
    for i in range(len(titulo)):
        fila = [
            titulo[i],
            contenido[i],
            plataforma[i],
            precio[i],
            stock[i],
            categoria[i],
            disponibilidad[i]
        ]
        matriz.append(fila)
    return matriz  
#Gaspar Divano   
def informe_general(matriz):
    '''Muestra todos los productos registrados ordenados de mayor a menor
    según el stock disponible. En caso de igualdad, ordena alfabéticamente
    por título.'''
    print("-" * 50)
    print("Informe General")
    print("-" * 50)
    ordenamiento_burbuja(matriz)
    print("-" * 135)
    print("-" * 150)
    print(
        "Titulo".ljust(40) + "|" +
        "Contenido".ljust(15) + "|" +
        "Plataforma".ljust(20) + "|" +
        "Precio".ljust(12) + "|" +
        "Stock".ljust(8) + "|" +
        "Categorias".ljust(30) + "|" +
        "Disponibilidad"
    )
    print("-" * 150)
    for fila in matriz:
        print(
            str(fila[0]).ljust(40) + "|" +
            str(fila[1]).ljust(15) + "|" +
            str(fila[2]).ljust(20) + "|" +
            str(fila[3]).ljust(12) + "|" +
            str(fila[4]).ljust(8) + "|" +
            str(fila[5]).ljust(30) + "|" +
            str(fila[6])
        )

    print("-" * 150)
#Gaspar Divano
def mostrar_informe(datos):

    titulo = datos[0]
    contenido = datos[1]
    plataforma = datos[2]
    precio = datos[3]
    stock = datos[4]
    categoria = datos[5]
    disponibilidad = datos[6]

    matriz = crear_matriz(
        titulo,
        contenido,
        plataforma,
        precio,
        stock,
        categoria,
        disponibilidad
    )

    informe_general(matriz)
#Tomas Ruano
def existe_en_lista(lista, valor):
    encontrado = False
    i = 0

    while i < len(lista) and encontrado == False:
        if lista[i].lower() == valor.lower():
            encontrado = True
        i += 1

    return encontrado
#Tomas Ruano
def ingresar_entero_no_negativo(msg):
    valor = input(msg)

    while valor.isdigit() == False:
        valor = input("Error. Ingrese un numero entero positivo: ")

    return int(valor)
#Tomas Sobrino
def ingresar_opcion_valida(msg, opciones):
    print("Opciones disponibles:")

    i = 0
    while i < len(opciones):
        print("-", opciones[i])
        i += 1

    valor = input(msg)

    while existe_en_lista(opciones, valor) == False:
        print("Opcion invalida. Debe elegir una de las opciones mostradas.")
        valor = input(msg)

    return valor
#Ignacio Diaz
def ingresar_float_positivo(msg):
    valor = input(msg)
    valido = False

    while valido == False:

        puntos = 0
        i = 0
        es_numero = True

        while i < len(valor) and es_numero == True:

            if valor[i] == ".":
                puntos += 1
                if puntos > 1:
                    es_numero = False

            elif valor[i].isdigit() == False:
                es_numero = False

            i += 1

        if es_numero == True and len(valor) > 0:
            valido = True
        else:
            valor = input("Ingrese un precio valido: ")

    return float(valor)
#Agustin Fani
def producto_duplicado(datos, titulo_buscado):
    titulos = datos[0]

    duplicado = False
    i = 0

    while i < len(titulos) and duplicado == False:
        if titulos[i].lower() == titulo_buscado.lower():
            duplicado = True
        i += 1

    return duplicado
#Agustin Fani
def es_eliminable(stock, disponibilidad, indice):
    eliminable = False

    if stock[indice] == 0 and disponibilidad[indice].lower() == "discontinuado":
        eliminable = True

    return eliminable
#Agustin Fani
def eliminar_por_indice(datos, indice):

    titulo = datos[0]
    contenido = datos[1]
    plataforma = datos[2]
    precio = datos[3]
    stock = datos[4]
    categoria = datos[5]
    disponibilidad = datos[6]

    titulo.pop(indice)
    contenido.pop(indice)
    plataforma.pop(indice)
    precio.pop(indice)
    stock.pop(indice)
    categoria.pop(indice)
    disponibilidad.pop(indice)
#Tomas Sobrino
def guardar_producto(datos, titulo_nuevo, contenido_nuevo, plataforma_nueva,
                     precio_nuevo, stock_nuevo, categoria_nueva, disponibilidad_nueva):

    datos[0].append(titulo_nuevo)
    datos[1].append(contenido_nuevo)
    datos[2].append(plataforma_nueva)
    datos[3].append(precio_nuevo)
    datos[4].append(stock_nuevo)
    datos[5].append(categoria_nueva)
    datos[6].append(disponibilidad_nueva)
#Tomas Ruano
def pedir_titulo(datos):
    titulo = input("Ingrese el titulo: ")

    while titulo == "" or producto_duplicado(datos, titulo):

        if titulo == "":
            print("El titulo no puede estar vacio.")
        else:
            print("Ese producto ya existe.")

        titulo = input("Ingrese otro titulo: ")

    return titulo