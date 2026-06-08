import FuncionesTPO
import MenusTPO
#Ignacio Diaz
def main():
    opcion = 0
    while opcion >=0 and opcion != 5:
    #Valida que el usuario ingrese una opcion valida
        MenusTPO.menu_opciones()
        #Imprime el menu interactivo en cada ciclo
        opcion = int(input ("Seleccione una opción: "))
        if opcion == 1:
            FuncionesTPO.registrar_producto()
        elif opcion == 2:
            FuncionesTPO.eliminar_producto()
        elif opcion == 3:
            FuncionesTPO.modificar_producto()
        elif opcion == 4:
            FuncionesTPO.informe_general()
        elif opcion == 5:
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")


main()