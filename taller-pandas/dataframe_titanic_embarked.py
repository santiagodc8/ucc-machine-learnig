import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tita = pd.read_csv("/home/elmakiaxd/Downloads/titanic_embarked.csv",encoding="utf-8")

"""# Contar el número de pasajeros por puerto de embarque
conteo_puertos = tita['Embarked'].value_counts()

# Crear la gráfica de torta
plt.figure(figsize=(8, 6))  # Tamaño de la figura
plt.pie(conteo_puertos, 
        labels=conteo_puertos.index,  # Etiquetas de los puertos
        autopct='%1.1f%%',            # Mostrar porcentajes en cada porción
        colors=['lightblue', 'lightgreen', 'lightcoral'],  # Colores de las porciones
        startangle=140)               # Ángulo de inicio para la gráfica de torta

plt.title('Distribución de Pasajeros por Puerto de Embarque')
plt.show()"""


"""# Contar el número de pasajeros en cada clase
conteo_clases = tita['Pclass'].value_counts().sort_index()

# Crear la gráfica de barras
plt.figure(figsize=(8, 6))  # Tamaño de la figura
plt.bar(conteo_clases.index, conteo_clases.values, color='skyblue')

# Agregar etiquetas y título
plt.xlabel('Clase')
plt.ylabel('Número de Pasajeros')
plt.title('Número de Pasajeros por Clase en el Titanic')

# Mostrar la gráfica
plt.xticks(ticks=conteo_clases.index)  # Asegura que las etiquetas del eje x se correspondan con las clases
plt.show()"""


"""#distribucion de edades de los pasajeros
plt.hist(tita['Age'].dropna(), bins=30, edgecolor='black')
plt.xlabel('Edad')
plt.ylabel('Número de pasajeros')
plt.title('Distribución de Edad de los Pasajeros')
plt.show()"""

"""#Supervivencia de pasajeros por clases
survival_rate_by_class = tita.groupby('Pclass')['Survived'].mean()
survival_rate_by_class.plot(kind='bar', color='skyblue')
plt.xlabel('Clase')
plt.ylabel('Tasa de Supervivencia')
plt.title('Tasa de Supervivencia por Clase')
plt.show()"""


#Supervivencia de pasajeros por genero
survival_rate_by_gender = tita.groupby('Sex')['Survived'].mean()
survival_rate_by_gender.plot(kind='bar', color=['blue', 'pink'])
plt.xlabel('Género')
plt.ylabel('Tasa de Supervivencia')
plt.title('Tasa de Supervivencia por Género')
plt.show()
