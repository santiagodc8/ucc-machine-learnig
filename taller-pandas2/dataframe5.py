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

# Recorrer el dataframe y mostrar la region y valor de la casa si es mayor a 500.000
print('\nMostrar la región y valor de la casa si es mayor 500.000')
for index, row in datos.iterrows():
  if row['median_house_value'] > 500000:
    print(f"Región: {row['ocean_proximity']}, Valor: {row['median_house_value']}")