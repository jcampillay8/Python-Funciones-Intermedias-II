# 1 Actualiza los valores en diccionarios y listas
# Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

print(students)

students[0]['last_name']='Bryant'

print(students)