import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Datos ficticios: Tamaño (m²), Habitaciones, Edad de la casa
X = np.array([
    [100, 3, 5],
    [150, 4, 3],
    [200, 5, 1],
    [120, 3, 4],
    [180, 4, 2]
])

# Precio en miles de dólares
y = np.array([200, 300, 400, 250, 350])

# Crear un modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo con los datos
model.fit(X, y)

# Nuevos datos: Tamaño (120 m²), 3 habitaciones, Edad 4 años
nueva_casa = np.array([[120, 3, 4]])

# Predecir el precio de la nueva casa
prediccion = model.predict(nueva_casa)

print(f"El precio predicho para la nueva casa es: ${prediccion[0]*1000:.2f}")

# Visualización para ver cómo se ajustan los precios al tamaño
# Solo graficaremos la relación entre el tamaño y el precio

tamanos = X[:, 0]  # Tamaños de las casas
plt.scatter(tamanos, y, color='blue', label='Datos reales')
plt.plot(tamanos, model.predict(X), color='red', label='Ajuste del modelo')
plt.xlabel('Tamaño (m²)')
plt.ylabel('Precio (en miles de dólares)')
plt.title('Relación entre el Tamaño y el Precio de la casa')
plt.legend()
plt.show()
