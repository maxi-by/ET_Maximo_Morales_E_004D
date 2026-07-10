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
def copias_genero(genero, libros, prestamos):
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
def buscar_codigo(codigo, prestamos):
    for clave in prestamos:
        if codigo.upper() == codigo.upper():
            return True
    return False
def actualizar_multa(codigo, nueva_multa, prestamos):
    codigo = codigo.upper()
    if buscar_codigo(codigo, prestamos):
        prestamos[codigo][0] = nueva_multa
        return True
    return False
def validar_codigo(codigo):
    if codigo.strip() != "":
        return True
    else:
        return False
def validar_titulo(titulo):
    if titulo.strip() != "":
        return True
    else:
        return False
def validar_autor(autor):
    if autor.strip() != "":
        return True
    else:
        return False
def validar_año(año):
    if año > 0:
        return True
    else:
        return False
def validar_editorial(editorial):
    if editorial.strip() != "":
        return True
    else:
        return False
def validar_es_novedad(es_novedad):
    if es_novedad == "s" or es_novedad == "n":
        return True
    else:
        return False
def validar_precio_multa(precio_multa):
    if precio_multa > 0:
        return True
    else:
        return False
def validar_copias_disponibles(copias_disponibles):
    if copias_disponibles >= 0:
        return True
    else:
        return False
def agregar_libro(codigo, titulo, autor, genero, año, editorial, es_novedad, precio_multa, copias_disponibles, libros, prestamos):
    if buscar_codigo(codigo, prestamos):
        return False
    else:
        if es_novedad == "s":
            es_novedad_bool = True
        else:
            es_novedad_bool = False
        libros[codigo.upper()] = [titulo, autor, genero, año, editorial, es_novedad_bool]
        prestamos[codigo.upper()] = [precio_multa, copias_disponibles]
        return True
