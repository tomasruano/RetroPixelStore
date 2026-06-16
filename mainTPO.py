import FuncionesTPO
import MenusTPO
import DatosTPO

# Ignacio Diaz
def ejecutar_menu(datos):
    salir = False

    while salir == False:

        MenusTPO.menu_opciones()

        opcion = input("Seleccione una opcion: ")

        while opcion not in ["1", "2", "3", "4", "5"]:
            print("Opcion invalida. Seleccione entre 1 y 5.")
            opcion = input("Ingrese una opcion valida: ")

        if opcion == "1":
            FuncionesTPO.registrar_producto(datos)

        elif opcion == "2":
            FuncionesTPO.eliminar_producto(datos)

        elif opcion == "3":
            FuncionesTPO.modificar_producto(datos)

        elif opcion == "4":
            FuncionesTPO.mostrar_informe(datos)

        elif opcion == "5":
            print("Saliendo del programa...")
            salir = True

#Tomas Ruano
def main():
    datos = DatosTPO.crearDatosIniciales()
    ejecutar_menu(datos)


main()