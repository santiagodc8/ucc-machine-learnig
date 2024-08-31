'''
#ejercicio 1 Verificar si es mayor de edad

edad = int(input ("ingrese su edad: "))
if edad >= 18:
    print("Puedes entrar a la discoteca")
else:
    print("No puedes ingresar")
'''


'''
#ejercicio 2: Escribe un programa que le pida al usuario que ingrese un número. El programa debe verificar si
el número es positivo, negativo o cero e imprimir un mensaje apropiado para cada caso.


numero = int(input("Ingresa un numero entero: "))
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")
'''  

#Ejercicio 2: 
'''Escribe un programa que solicite al usuario ingresar una letra del alfabeto.
El programa debe determinar si la letra ingresada es una vocal o una consonante y
luego imprimir un mensaje correspondiente.
Si el usuario ingresa un carácter que no es una letra,
el programa debe imprimir un mensaje indicando que la entrada no es válida.
'''

# Solicitar al usuario que ingrese una letra
letra = input("Ingresa una letra del alfabeto: ").lower()

# Verificar si es una letra válida
if letra.isalpha() and len(letra) == 1:
    # Verificar si la letra es una vocal
    if letra in 'aeiou':
        print("La letra es una vocal.")
    else:
        print("La letra es una consonante.")
else:
    print("Entrada no válida. Por favor ingresa solo una letra del alfabeto.")
