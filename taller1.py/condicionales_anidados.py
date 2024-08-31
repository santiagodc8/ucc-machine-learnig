#1
'''Escribe un programa que clasifique el clima en función de la temperatura ingresada por el usuario.
El programa debe clasificar la temperatura en tres categorías:

    Frío: Si la temperatura es menor a 10 grados Celsius.
    Templado: Si la temperatura está entre 10 y 25 grados Celsius, inclusive.
    Caliente: Si la temperatura es mayor a 25 grados Celsius.'''
    
'''temp = float(input("Ingresa la temperatura en grados celsuis: "))
if temp < 10:
    print("El clima es frio")
else:
    if temp <= 25:
        print("El clima es templado")
    else:
        if temp > 25:
            print("El clima es caliente")'''
  
#2            
'''
Crea un programa que evalúe una variable onumeropy dependiendo del resultado,
imprima un mensaje diferente. Si el número es mayor a 10, imprime "El número es 
mayor a 10". Si el número es menor a 10, imprime "El número es menor a 10".
Si el número es igual a 10, imprime "El número es igual a 10"
'''

'''numero = int(input("Ingresa un numero entero: "))
if numero > 10:
    print(f"el numero {numero} es mayor a diez")
elif numero < 10:
    print(f"el numero {numero} es menor a diez")
else:
    print(f"el numero {numero} es diez")'''
    

#3
'''Escribe un programa que le pida al usuario que ingrese un número. El programa debe verificar si
el número es positivo, negativo o cero e imprimir un mensaje apropiado para cada caso.'''


numero = int(input("Ingresa un numero entero: "))
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero") 

