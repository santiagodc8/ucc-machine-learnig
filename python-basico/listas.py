'''
numeros = list(range(1,11))
print(numeros)

print("La salida de la iteracion: ")
for i in numeros:
    if i % 2 == 0:
        print(i)
'''
        
ciudades = ["Bosconia", "Curumani", "Becerril", "Pailitas", "Aguachica", "La Paz", "El Copey"]
print(ciudades)

for ciudad in ciudades:
    print(ciudad)
    
ciudades.append("Valledupar")
print(ciudades)

ciudades.insert(3, "Pelaya")
print(ciudades)

