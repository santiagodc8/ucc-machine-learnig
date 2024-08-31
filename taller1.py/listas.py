#1
#colores

colores = ["amarillo","azul","rojo"]
print(colores)

colores.append("verde")
print(colores)

colores.extend(["morado","rosado"])
print(colores)

colores.pop(4)
print(colores)

cantidad_elementos = len(colores)
print(cantidad_elementos)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2

print(lista_concatenada)
