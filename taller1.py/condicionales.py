#1
#Verificar si es mayor de edad

'''edad = int(input ("ingrese su edad: "))
if edad >= 18:
    print("Puedes entrar a la discoteca")
else:
    print("No puedes ingresar")
'''


#2
'''
#contrasena
contrasena_almacenada = "HolaCompae"
contrasena_escrita = "HolaCmpae"

if contrasena_escrita == contrasena_almacenada:
    print("ingresando al sistema...")
else:
    print("ingreso invalido")'''


#3
#verificar si la letra es vocal

letra = input("ingresa una letra: ").lower()

if letra in 'aeiou':
    print(f"la letra {letra} es una vocal")
else:
    print(f"la letra {letra} no es una vocal")