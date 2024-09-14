import pandas as pd


"""#1. leer un dataframe desde una pagina web
url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"
df = pd.read_csv(url)
print(df)"""

"""#2. descargar el archivo csv
df.to_csv("/home/santiagod/Documentos/ucc-repos/ucc-machine-learnig/csv/inmobiliaria.csv", index=False, encoding='utf-8')"""

#3. cargar el archivo csv local
datos = pd.read_csv("/home/santiagod/Documentos/ucc-repos/ucc-machine-learnig/csv/inmobiliaria.csv")
#print(datos)

#print(datos.describe())
#print(datos.info())

"""print("primeras filas del dataframe")
print(df.head())

print(f"\nTamaño del dataframe: {df.shape}")"""


#cambiar edad nula por el promedio de edad
datos['total_bedrooms'].fillna(datos['total_bedrooms'].mode()[0], inplace=True)
print(datos)

datos.to_csv('inmoviliaria_sin_nulos.csv', index=False)

#valores nulos
print("\nvalores nulos por columna: ")
print(datos.isnull().sum())


