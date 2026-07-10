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
libros = {
'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True],
'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral', False],
'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False],
'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021, 'Orión', True],
'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False],
}
prestamos = {
'L001': [500, 4],
'L002': [700, 0],
'L003': [300, 10],
'L004': [400, 2],
'L005': [600, 1],
'L006': [350, 6],
}
def opias_genero(genero, libros, prestamos):
    total = 0
    for clave in libros:
        if libros[clave][2].lower() == genero.lower():
            total += prestamos[clave][1]
    print(f"El total de copias disponibles es: {total}")
def busqueda_multa(multa_min, multa_max, libros, prestamos):
    resultados = []
    for clave in prestamos:
        multa = prestamos[clave][0]
        copias = prestamos[clave][1]
        if (multa >= multa_min and multa <= multa_max and copias > 0):
            producto = libros[clave][0] + "--" + clave
            resultados.append(producto)
    if len(resultados) == 0:
        print("No hay libros en ese rango de multa.")
    else:
        resultados.sort()
        for producto in resultados:
            print(f"Los libros encontrados son: {producto}")
