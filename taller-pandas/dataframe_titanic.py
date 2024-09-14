import pandas as pd
import matplotlib.pyplot as plt

tita = pd.read_csv("/home/elmakiaxd/Downloads/titanic.csv",encoding="utf-8")
#print(tita)

#describe
#print(tita.describe())

#info
#print(tita.info())

"""#cambiar edad nula por el promedio de edad
tita['Age'].fillna(tita['Age'].mean(), inplace=True)
print(tita)

tita.to_csv('titanic_age.csv', index=False)"""

"""#contar mujeres y hombres
num_mujeres = tita['Sex'].value_counts()['female']
print(f"Hay {num_mujeres} mujeres en el DataFrame.")


num_hombres = tita['Sex'].value_counts()['male']
print(f"Hay {num_hombres} hombres en el DataFrame.")"""

"""#moda de la edad
moda_edad = tita['Age'].mode()[0]
print(f"La moda de la columna 'Age' es: {moda_edad}")"""

"""#desviacion estandar de edad
desviacion_edad = tita['Age'].std()
print(f"La desviación estándar de la columna 'Age' es: {desviacion_edad}")"""

"""#edad minima,maxima y promedio
edad_minima = tita['Age'].min()
print(f"La edad mínima en el Titanic es: {edad_minima}")

edad_maxima = tita['Age'].max()
print(f"La edad maxima en el Titanic es: {edad_maxima}")

promedio_edad = tita['Age'].mean()
print(f"El promedio de la columna 'Age' es: {promedio_edad}")"""

"""#contar los sobrevivientes
num_sobrevivientes = tita['Survived'].value_counts()[1]
print(f"Hay {num_sobrevivientes} sobrevivientes del Titanic")"""

