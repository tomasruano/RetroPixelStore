import DatosTPO
import MenusTPO
import random


def buscar_indice(lista, valor):
    for i in range(len(lista)): 
        #Recorre la lista para encontrar el indice de un elemento
        if lista[i] == valor:
            return i 
        #Si hay coincidencia, devuelve su posicion


def registrar_producto():
    '''Permite al usuario registrar un nuevo producto, ya sea ingresando los datos manualmente o generándolos aleatoriamente.'''
    print("-" * 50)
    print("Registrar producto")
    print("-" * 50)
    print("1. Carga Manual por teclado")
    print("2. Carga Automática (Aleatoria)")
    modo = input("Seleccione el modo de carga (1 o 2, o 'volver' para regresar): ")

    while modo != "1" and modo != "2" and modo.lower()!="volver": 
        #Se verifica que el numero ingresado sea valido
        if modo.lower() == "volver":
            print("Volviendo al menú principal...")
            return
        modo = (input("Opción no válida. Ingrese 1, 2 o 'volver': "))
    
    if modo == "1": 
        #Opcion de carga manual, se valida en cada while que coincida con las opciones.
        titulo = input("Ingrese el título del producto: ")
        while titulo == "":
            titulo = input("El título no puede estar vacío. Ingrese título: ")

        contenido = input("Ingrese la naturaleza (Videojuego o Pelicula): ")
        while contenido.lower() != "Videojuego".lower() and contenido.lower() != "Pelicula".lower():
            contenido = input("Error. Ingrese 'Videojuego' o 'Pelicula': ")
        
        print("Opciones válidas:", DatosTPO.Opciones_Plataforma)
        formato = input("Ingrese el formato: ")
        while formato.lower() not in DatosTPO.Opciones_Plataforma:
            formato = input("Formato no válido. Ingrese nuevamente: ")
            
        precio = float(input("Ingrese el precio del producto: "))
        while precio < 0:
            precio = float(input("El precio no puede ser negativo. Ingrese precio: "))
            
        stock = int(input("Ingrese el stock del producto: "))
        while stock < 0:
            stock = int(input("El stock debe ser mayor o igual a 0. Ingrese stock: "))
            
        print("Categorías válidas:", DatosTPO.Opciones_Categoria)    
        categoria = input("Ingrese la categoría del producto: ")
        while categoria.lower() not in DatosTPO.Opciones_Categoria:
            categoria = input("Categoría no válida. Intente nuevamente: ")

        print("Estados válidos:", DatosTPO.Opciones_Disponibilidad)    
        disponibilidad = input("Ingrese la disponibilidad del producto: ")
        while disponibilidad.lower() not in DatosTPO.Opciones_Disponibilidad:
            disponibilidad = input("Disponibilidad no válida. Intente nuevamente: ")

    else: #Carga aleatoria, genera un indice random en comun para que coincidan sus respectivos datos.
        elemento = random.randint(0, len(DatosTPO.Titulos_Posibles) - 1)
        titulo = DatosTPO.Titulos_Posibles[elemento]
        contenido = DatosTPO.Contenidos_Posibles[elemento]
        formato = DatosTPO.Plataformas_Posibles[elemento]
        precio = float(random.randint(10000, 60000))
        stock = random.randint(0, 10)
        categoria = DatosTPO.Categorias_Posibles[elemento]
        disponibilidad = DatosTPO.Disponibilidades_Posibles[elemento]
        print("Generando datos aleatorios...")

    #Agrega al final de las listas los atributos recien generados.
    DatosTPO.Titulo.append(titulo.title())
    DatosTPO.Contenido.append(contenido.capitalize())
    DatosTPO.Plataforma.append(formato.title())
    DatosTPO.Precio.append(precio)
    DatosTPO.Stock.append(stock)
    DatosTPO.Categoria.append(categoria.capitalize())
    DatosTPO.Disponibilidad.append(disponibilidad.capitalize())
    print(titulo, "registrado con éxito.")
        
def eliminar_producto():
    '''Permite al usuario eliminar un producto registrado solicitandole una confirmación previa a la ejecucion. Solo podran eliminarse productos cuyo estado de disponibilidad sea "Discontinuado" y 
la cantidad en stock sea cero.'''
    print("-"*50)
    print("Eliminar producto")
    print("-"*50)
    posibles_eliminar = []

    for producto in range(len(DatosTPO.Titulo)): 
        #Verifica que el producto seleccionado sea apto para eliminarlo
        if DatosTPO.Stock[producto] == 0 and DatosTPO.Disponibilidad[producto].lower() == "discontinuado":
            posibles_eliminar.append(DatosTPO.Titulo[producto])

    print("Los productos que están disponibles para eliminar son:", posibles_eliminar)
    nombre= input("Ingrese el titulo del producto a eliminar o 'volver' para regresar:").capitalize()
    while nombre not in DatosTPO.Titulo:
        if nombre != "Volver":
            nombre= input("El titulo no se encuentra en stock, ingrese otro titulo o 'volver' para regresar :").capitalize()
        else:
            return
    indice=buscar_indice(DatosTPO.Titulo,nombre) #Llamamos a la funcion para buscar el indice
    if DatosTPO.Stock[indice] == 0 and DatosTPO.Disponibilidad[indice] == "Discontinuado":
        #Verificacion de las pautas de eliminacion
        confirmacion=input("¿Está seguro que quiere eliminar este producto?, 'si' para eliminar, 'no' para regresar y cancelar la eliminacion :").lower()
        while confirmacion != "si" and confirmacion != "no":
            print("no se selecciono ninguna de las opciones dadas, intente nuevamente")
            confirmacion=input("¿esta seguro que quiere eliminar este producto?, 'si' para eliminar, 'no' para regresar y cancelar la eliminacion :").lower()
        if confirmacion == "si":
        #Elimina de las listas el elemento que se encuentre en el indice que corresponde
            DatosTPO.Titulo.pop(indice)
            DatosTPO.Contenido.pop(indice)
            DatosTPO.Plataforma.pop(indice)
            DatosTPO.Precio.pop(indice)
            DatosTPO.Stock.pop(indice)
            DatosTPO.Categoria.pop(indice)
            DatosTPO.Disponibilidad.pop(indice)
            print("producto eliminado con exito")
            return
            
        elif confirmacion == "no":
            return
        
    else:
        print("el producto no se puede eliminar ya que no esta discontinuado y su stock no es cero")
        return

def modificar_producto():
    '''Permite al usuario modificar uno o mas atributos de un elemento ya registrado anteriormente. El producto se selecciona introduciendo su titulo.'''
    print("-"*50)
    print("Modificar producto")
    print("-"*50)
    if len(DatosTPO.Titulo) == 0:
        print("No hay productos registrados para modificar.")
        return
    
    print("Los productos registrados son:", DatosTPO.Titulo)
    titulo = input("Ingrese el título del producto a modificar o 'volver' para regresar: ").title()

    if titulo.lower() == "volver":
        print("Volviendo al menú principal...")
        return
    
    while titulo not in DatosTPO.Titulo:
        titulo = input("El título no se encuentra registrado. Ingrese otro título o 'volver' para regresar: ").title()
        if titulo.lower() == "volver":
            return

    coincidencias = []
    
    for i in range(len(DatosTPO.Titulo)):
    #Recorre la lista y agrupa todos los elementos con mismo titulo
        if DatosTPO.Titulo[i] == titulo:
            coincidencias.append(i)

    if len(coincidencias) > 1:
        print("Se encontraron", len(coincidencias), "productos con el título", titulo, ":")
        for opcion_lista in range(len(coincidencias)):
            i = coincidencias[opcion_lista]
            print(opcion_lista + 1,
                "Plataforma:", DatosTPO.Plataforma[i],
                ", Contenido:", DatosTPO.Contenido[i],
                ", Precio:", DatosTPO.Precio[i],
                ", Stock:", DatosTPO.Stock[i],
                ", Categoría:", DatosTPO.Categoria[i],
                ", Disponibilidad:", DatosTPO.Disponibilidad[i])
            
        seleccion = input("Seleccione el número del producto que desea modificar o 'volver' para regresar: ")
        
        while seleccion.lower() != "volver" and not (seleccion == "1" or (seleccion == "2" and len(coincidencias) >= 2) or
        (seleccion == "3" and len(coincidencias) >= 3) or
        (seleccion == "4" and len(coincidencias) >= 4) or
        (seleccion == "5" and len(coincidencias) >= 5) or
        (seleccion == "6" and len(coincidencias) >= 6) or
        (seleccion == "7" and len(coincidencias) >= 7)):
            seleccion = input("Opción no válida. Ingrese un número válido o 'volver': ")
        if seleccion.lower() == "volver":
            return
        indice = coincidencias[int(seleccion) - 1]
    else:
        indice = buscar_indice(DatosTPO.Titulo, titulo)

    MenusTPO.menu_modificar()
    opcion = input("Seleccione el número del atributo a modificar o 'volver' para regresar: ")
    
    while opcion not in ["1", "2", "3", "4", "5", "6", "7"] and opcion.lower() != "volver":
        opcion = input("Opción no válida. Ingrese un número del 1 al 7 o 'volver' para regresar: ")
    if opcion.lower() == "volver":
        return
    
    if opcion == "1":
    #Sirve para modificar los atributos de las listas paralelas.
        nuevo_titulo = input("Ingrese el nuevo título: ")
        while nuevo_titulo == "":
            nuevo_titulo = input("El título no puede estar vacío. Ingrese nuevo título: ")
        DatosTPO.Titulo[indice] = nuevo_titulo.title()

    elif opcion == "2":
        nuevo_contenido = input("Ingrese la nueva naturaleza (Videojuego o Pelicula): ")
        while nuevo_contenido.lower() != "Videojuego".lower() and nuevo_contenido.lower() != "Pelicula".lower():
            nuevo_contenido = input("Error. Ingrese 'Videojuego' o 'Pelicula': ")
        DatosTPO.Contenido[indice] = nuevo_contenido.capitalize()

    elif opcion == "3":
        print("Opciones válidas:", DatosTPO.Opciones_Plataforma)
        nuevo_formato = input("Ingrese el nuevo formato: ")
        while nuevo_formato.lower() not in DatosTPO.Opciones_Plataforma:
            nuevo_formato = input("Formato no válido. Ingrese nuevamente: ")
        DatosTPO.Plataforma[indice] = nuevo_formato.title()

    elif opcion == "4":
        nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
        while nuevo_precio < 0:
            nuevo_precio = float(input("El precio no puede ser negativo. Ingrese nuevo precio: "))
        DatosTPO.Precio[indice] = nuevo_precio

    elif opcion == "5":
        nuevo_stock = int(input("Ingrese el nuevo stock del producto: "))
        while nuevo_stock < 0:
            nuevo_stock = int(input("El stock debe ser mayor o igual a 0. Ingrese nuevo stock: "))
        DatosTPO.Stock[indice] = nuevo_stock

    elif opcion == "6":
        print("Categorías válidas:", DatosTPO.Opciones_Categoria)    
        nueva_categoria = input("Ingrese la nueva categoría del producto: ")
        while nueva_categoria.lower() not in DatosTPO.Opciones_Categoria:
            nueva_categoria = input("Categoría no válida. Intente nuevamente: ")
        DatosTPO.Categoria[indice] = nueva_categoria.capitalize()

    elif opcion == "7":
        print("Estados válidos:", DatosTPO.Opciones_Disponibilidad)    
        nueva_disponibilidad = input("Ingrese la nueva disponibilidad del producto: ")
        while nueva_disponibilidad.lower() not in DatosTPO.Opciones_Disponibilidad:
            nueva_disponibilidad = input("Disponibilidad no válida. Intente nuevamente: ")
        DatosTPO.Disponibilidad[indice] = nueva_disponibilidad.capitalize()
    print("Producto modificado con éxito.")
           
def informe_general():
    '''Muestra todos los productos registrados ordenados de mayor a menor
    según el stock disponible. En caso de igualdad, ordena alfabéticamente
    por título.'''
    print("-" * 50)
    print("Informe General")
    print("-" * 50)
    matriz = []
    for i in range(len(DatosTPO.Titulo)):
    #Convierte las listas paralelas, agrupadas en filas, en una matriz
        fila = [
            DatosTPO.Titulo[i],
            DatosTPO.Contenido[i],
            DatosTPO.Plataforma[i],
            DatosTPO.Precio[i],
            DatosTPO.Stock[i],
            DatosTPO.Categoria[i],
            DatosTPO.Disponibilidad[i]
        ]
        matriz.append(fila)
        
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
    print("-" * 135)
    print(
        "Titulo".ljust(40) + "|" +
        "Contenido".ljust(15) + "|" +
        "Plataforma".ljust(20) + "|" +
        "Precio".ljust(12) + "|" +
        "Stock".ljust(8) + "|" +
        "Categoria".ljust(18) + "|" +
        "Disponibilidad"
    )
    print("-" * 135)
    for fila in matriz:
        print(
            str(fila[0]).ljust(40) + "|" +
            str(fila[1]).ljust(15) + "|" +
            str(fila[2]).ljust(20) + "|" +
            str(fila[3]).ljust(12) + "|" +
            str(fila[4]).ljust(8) + "|" +
            str(fila[5]).ljust(18) + "|" +
            str(fila[6])
        )

    print("-" * 135)