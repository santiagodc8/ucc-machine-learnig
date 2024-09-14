import pandas as pd

datos = pd.read_csv("/home/santiagod/Documentos/ucc-repos/ucc-machine-learnig/taller-pandas2/inmoviliaria_sin_nulos.csv")
#print(datos)

#valores nulos
print("\nvalores nulos por columna: ")
print(datos.isnull().sum())

