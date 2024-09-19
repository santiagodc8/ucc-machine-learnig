import pandas as pd

datos = pd.read_csv("/home/santiagod/Documentos/ucc-repos/ucc-machine-learnig/taller-pandas2/inmoviliaria_sin_nulos.csv")
#print(datos)

#valores nulos
print("\nvalores nulos por columna: ")
print(datos.isnull().sum())

# Buscar todas las casas en la region de "INLAND" con mas de 4 habitaciones
casas_inland = datos[(datos["ocean_proximity"] == "INLAND") & (datos["total_rooms"] > 4000)]
print("\ncasas en la region INLAND con mas de 4000 habitaciones: ")
print(casas_inland)
casas_inland.to_csv("inmoviliaria_inland.csv", index = False)