# Manipulando texto

# Al igual que con los numeros, los operadores
# matematicos tambien afectan los Strings

miNombre = 'Fulano '
miApellido = 'De Tal'

# Si se quiere unir una cadena de texto a otra
# se usa el operador de la suma. A esto se le
# conoce como concatenacion

nombre_completo = miNombre + miApellido

print( nombre_completo )

# Para repetir tantas veces se requiera un
# String se usa el operador de multiplicacion
print( miNombre * 5 )

# Acceder a cada caracter de un String:
# Para ello usan los corchetes y entre ellos
# la posicion del caracter en el string

# Nota: las posiciones se cuentan a partir
# del numero 0

print( nombre_completo[0] )

# Es posible tambien recorrer el String
# de atras hacia adelante usando numeros
# negativos

print( nombre_completo[-1] )

# Secciones
# Para acceder a una seccion de un String
# se usan corchetes indicando la posicion
# de inicio y fin de dicha seccion separado
# por dos puntos

print( nombre_completo[2:8] )

# Si no se indica la posicion de inicio la seccion
# comenzara desde la posicion 0, de igual manera
# si no se indica la posicion final la seccion se
# extendera hasta el final de la cadena de texto
print( nombre_completo[2:] )
print( nombre_completo[:8] )

# Longitud de una cadena de texto:
# Para conocer la longitud de una cadena
# se usa la funcion "len"
print( len(nombre_completo) )