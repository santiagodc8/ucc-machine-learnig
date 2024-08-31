#1
#imprimir los numeros del 1 a 10
'''for num in range(11):
    print(num)'''
    
#2
#potencia
'''for i in [1,3,6,7,1]:
    x = i**2 
    print("la potencia de de cada numero de la lista es:  ")'''
    
#3
# Lista de notas
notas = [3, 4, 5, 2, 3.5, 2]

contar_notas = len(notas)

suma_notas = 0

for nota in notas:
    suma_notas += nota
    
promedio = suma_notas / contar_notas

print(f"El promedio es: {promedio}")


