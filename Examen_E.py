def mostrar_menu():
    print("""========== MENÚ PRINCIPAL ==========
1. Copias por género
2. Búsqueda de libros por rango de multa
3. Actualizar multa de libro
4. Agregar libro
5. Eliminar libro
6. Salir
=====================================""")
def leer_opcion():
    while True:
        try:
            opc = int(input("Ingrese opcion: "))
        except ValueError:
            print("Error: Debe ingresar numeros enteros")
        else:
            if opc >= 1 and opc <= 6:
                return opc
            else:
                print("Error: Debe ingresar una opcion entre 1-6")
