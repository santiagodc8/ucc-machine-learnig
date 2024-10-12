import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Datos ficticios: Edad, Peso, Colesterol
X = np.array([
    [45, 85, 180],  # Paciente 1: 45 años, 85 kg, colesterol 180
    [50, 90, 200],  # Paciente 2: 50 años, 90 kg, colesterol 200
    [65, 100, 220], # Paciente 3: 65 años, 100 kg, colesterol 220
    [40, 70, 150],  # Paciente 4: 40 años, 70 kg, colesterol 150
    [60, 95, 230],  # Paciente 5: 60 años, 95 kg, colesterol 230
])

# Etiquetas: 0 = No tiene enfermedad, 1 = Tiene enfermedad
y = np.array([0, 1, 1, 0, 1])

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión logística
model = LogisticRegression()

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Nuevos datos para predecir: Edad 50 años, Peso 85 kg, Colesterol 190
nuevo_paciente = np.array([[50, 85, 190]])

# Predecir si el nuevo paciente tiene la enfermedad
prediccion = model.predict(nuevo_paciente)
probabilidad = model.predict_proba(nuevo_paciente)

print(f"El modelo predice que el paciente {'tiene' if prediccion[0] == 1 else 'no tiene'} la enfermedad.")
print(f"Probabilidad de tener la enfermedad: {probabilidad[0][1] * 100:.2f}%")

# Evaluación del modelo con los datos de prueba
y_pred_test = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred_test)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")

# Matriz de confusión
matriz_confusion = confusion_matrix(y_test, y_pred_test)
print("Matriz de confusión:")
print(matriz_confusion)
