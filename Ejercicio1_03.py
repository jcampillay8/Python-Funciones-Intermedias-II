# 1 Actualiza los valores en diccionarios y listas
# En el directorio sports_directory, cambia 'Messi' a 'Andres'

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

print(sports_directory)

sports_directory['soccer'][0]="Andres"

print(sports_directory)