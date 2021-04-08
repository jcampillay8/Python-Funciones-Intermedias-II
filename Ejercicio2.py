#2 Itera a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado. Por ejemplo, dada la siguiente lista:

def iterateDictionary(lista):
    for i in range(len(lista)):
        nombre=lista[i]['first_name']
        apellido=lista[i]['last_name']
        print("first_name - {}, last_name - {}".format(nombre,apellido))

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterateDictionary(students)