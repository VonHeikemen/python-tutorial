# Tipo de variables: List
# Este tipo de variables permite
# almacenar una lista de todo tipo de variables

# Declarando una lista
# Para declarar una lista se encierra 
# cada uno de los elementos entre corchetes
# y se separan por comas. 

lista = ['Uno', 2, "3"];

print( lista )

# Acceder a un elemento
print( lista[0] )

# Acceder a una seccion
print( lista[0:2] )

# Reemplazar un valor de una lista
lista[2] = 'TRES'

print( lista )

# Reemplazar una seccion
lista[1:] = ['Dos', 'Tres']

print( lista )

# Agregar elementos a una lista

# Usando el operador de suma
otra_lista = [4, 'cinco'];

# Esto produce una nueva lista
# compuesta de los elementos de las
# dos listas anteriores, sin afectarlas
# de manera permanente
print( lista + otra_lista )
print( lista )

# Utilizando el metodo append
lista.append( 4 )

# Esto une la variable "4"
# a "lista" y la afecta de manera permanente
print( lista )

# Eliminar elementos de una lista
lista[2:] = []

# Aqui se reemplazo la seccion
# de la lista con una lista vacia
# lo que resulta en la eliminacion
# de los elementos de la seccion
print( lista )