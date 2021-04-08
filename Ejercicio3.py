#3 Obtén valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario.

def iterateDictionary(lista):
    for i in range(len(lista)):
        nombre=lista[i]['first_name']      
        print(nombre)

    print("*"*10)
    for i in range(len(lista)):
        apellido=lista[i]['last_name']    
        print(apellido)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterateDictionary(students)
