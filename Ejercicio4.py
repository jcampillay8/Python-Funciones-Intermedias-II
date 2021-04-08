#4 Itera a través de un diccionario con valores de listas
# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:

def printInfo(lista):
    largo= len(lista['locations'])
    print(str(largo)+" LOCATIONS")
    for i in lista['locations']:
        print(i)
    
    print('')

    largo= len(lista['instructors'])
    print(str(largo)+" INSTRUCTORES")
    for i in lista['instructors']:
        print(i)



dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)