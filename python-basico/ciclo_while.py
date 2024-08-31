'''numero = float(input("Ingresa un numero (0 para detener): "))

while numero != 0:
    print(f"Has Ingresado el numero: {numero}")
    
    numero = float(input("Ingresa otro numero (0 para detener): "))
print(f"Programa terminado. Ingresaste el numero cero")
'''

'''Escribe un programa que pida al usuario que ingrese números hasta que ingrese un número negativo.
El programa debe contar cuántos números positivos se ingresaron y mostrar ese conteo al final.'''

numeros = int(input("Ingresa un numero por favor (positivo o negativo)"))

while numeros > 0:
    print(f"Has ingresado el numero {numeros}")
    
    numeros = int(input("Ingresa otro numero por favor (positivo o negativo)"))
print(f"Programa terminado. Ingresaste un numero negativo")
