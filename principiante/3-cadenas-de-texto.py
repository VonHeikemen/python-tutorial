# Tipo de variables: String
# Este tipo de variables es usado para
# almacenar cadenas de texto

# Declarando un string
# Para declarar un string se encierra 
# el texto en comillas dobles o simples

miNombre = "Fulano"
miApellido = 'De Tal'

print( miNombre )
print( miApellido )

# Las comillas indican el inicio y fin
# de la cadena de texto.
# Se debe empezar y culminar la cadena
# con el mismo tipo de comilla, combinarlos
# causaria un error

# Existen combinaciones especiales
# que sirven para representar espacios 
# en blanco como tabulacion o salto de 
# linea u otros simbolos

# A esto se le conoce como escapar un caracter
print(" Primera linea\nSegunda linea\ttabulacion ")

# Estas combinaciones en ocasiones pueden causar
# conflictos.

# Ejemplo: La ruta de un archivo o carpeta
print("C:\MiUsuario\MiCarpeta\nueva-carpeta\tambien-otra-carpeta")

# Para evitar que esto hay dos maneras

# 1: Escapar el caracter del slash, usando doble slash ( \\ )
print("C:\MiUsuario\MiCarpeta\\nueva-carpeta\\tambien-otra-carpeta")

# 2: Indicando una cadena de texto pura, esto es, decirle a Python
# que ignore cualquier combinacion considerada especial e interprete
# los caracteres tal cual como estan escritos. Esto se logra
# anteponiendo la letra 'r' antes de un String
print(r'C:\MiUsuario\MiCarpeta\nueva-carpeta\tambien-otra-carpeta')