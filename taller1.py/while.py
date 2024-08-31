#1
#imprimir los numeros de 1 al 20

'''contador = 1
while contador <= 20:
    print(contador)
    contador += 1'''

#2
#suma de numeros

'''suma = 0
numero = int(input("Ingresa un número (0 para terminar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingresa un número (0 para terminar): "))

print("La suma total es:", suma)'''


#3
#adivivnar numero

import random

numero_secreto = random.randint(1, 5)
adivinanza = None

while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (entre 1 y 5): "))
    
    if adivinanza < numero_secreto:
        print("Muy bajo, intenta de nuevo.")
    elif adivinanza > numero_secreto:
        print("Muy alto, intenta de nuevo.")
    else:
        print("¡Correcto! El número era:", numero_secreto)
