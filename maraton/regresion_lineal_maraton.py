import pandas as pd
import matplotlib.pyplot as plt
datos_maraton = pd.read_csv('/home/santiagodc/Documentos/ucc-repos/ucc-machine-learnig/csv/MarathonData.csv')
import matplotlib
matplotlib.use('TkAgg')


#print(datos_maraton)

#print(datos_maraton["Name"])

#print(datos_maraton.info())

#datos_maraton['Wall21'] = pd.to_numeric(datos_maraton['Wall21'], errors='coerce')

#print(datos_maraton.describe())

#print(datos_maraton.hist())


datos_maraton = datos_maraton.drop(columns= ['Name'])
datos_maraton = datos_maraton.drop(columns= ['id'])
datos_maraton = datos_maraton.drop(columns= ['Marathon'])
datos_maraton = datos_maraton.drop(columns= ['CATEGORY'])
#print(datos_maraton)

print(datos_maraton.isna().sum())

datos_maraton["CrossTraining"] = datos_maraton["CrossTraining"].fillna(0)
#print(datos_maraton)


datos_maraton = datos_maraton.dropna(how="any")
#print(datos_maraton)

datos_maraton["CrossTraining"].unique()

valores_cross = {"CrossTraining": {'ciclista 1h':1, 'ciclista 3h':2, 'ciclista 4h':3, 'ciclista 5h':4, 'ciclista 13h':5,}}
datos_maraton.replace(valores_cross, inplace=True)
print(datos_maraton)

'''plt.scatter(x = datos_maraton['km4week'], y=datos_maraton['MarathonTime'])
plt.title('km4week vs Marathon Time')
plt.xlabel('km4week')
plt.ylabel('Marathon Time')
plt.show()'''

datos_maraton = datos_maraton.query('sp4week<1000')

'''plt.scatter(x = datos_maraton['sp4week'], y=datos_maraton['MarathonTime'])
plt.title('sp4week vs Marathon Time')
plt.xlabel('sp4week')
plt.ylabel('Marathon Time')
plt.show()'''

datos_entrenamiento = datos_maraton.sample(frac=0.8,random_state=0)
datos_test = datos_maraton.drop(datos_entrenamiento.index)

print(datos_entrenamiento)