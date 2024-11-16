import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

# Definir la ruta del archivo CSV como una constante
FILE_PATH = '/home/santiagodc/Documentos/ucc-repos/ucc-machine-learnig/csv/carro_electrico.csv'

def load_and_prepare_data():
    """
    Carga un archivo CSV desde una ruta predefinida.
    Returns:
        pandas.DataFrame: Dataset preparado o None si falla.
    """
    try:
        data = pd.read_csv(FILE_PATH)
        print(f"\nDatos cargados exitosamente. Dimensiones del dataset: {data.shape}")
        return data
    except Exception as e:
        print(f"Error al cargar los datos: {str(e)}")
        return None

def encode_categorical_features(data, categorical_cols):
    """
    Codifica variables categóricas usando LabelEncoder.
    Args:
        data (pandas.DataFrame): Dataset original.
        categorical_cols (list): Lista de columnas categóricas.
    Returns:
        tuple: (DataFrame procesado, diccionario de encoders).
    """
    label_encoders = {}
    for col in categorical_cols:
        if col in data.columns:
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col].astype(str))
            label_encoders[col] = le
            print(f"Codificada la columna: {col}")
    return data, label_encoders

def train_and_evaluate_model(X_train, X_test, y_train, y_test):
    """
    Entrena y evalúa el modelo Random Forest.
    Returns:
        tuple: (modelo entrenado, predicciones).
    """
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    print(f"\nScore de validación cruzada: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")

    y_pred = model.predict(X_test)

    return model, y_pred

def plot_confusion_matrix(y_test, y_pred, labels):
    """
    Visualiza la matriz de confusión.
    """
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=labels, yticklabels=labels)
    plt.title('Matriz de Confusión')
    plt.ylabel('Valor Real')
    plt.xlabel('Predicción')
    plt.show()

def plot_feature_importance(model, feature_names):
    """
    Visualiza la importancia de las características.
    """
    importances = pd.DataFrame({
        'feature': feature_names,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='importance', y='feature', data=importances)
    plt.title('Importancia de las Características')
    plt.show()

def classify_new_user(model, encoders, feature_columns):
    """
    Clasifica a un nuevo usuario basándose en las características proporcionadas.
    Args:
        model: Modelo entrenado de clasificación.
        encoders: Diccionario con los LabelEncoders usados para codificar datos.
        feature_columns: Lista de nombres de características esperadas.
    """
    try:
        print("\nPor favor, ingresa los valores para las siguientes características:")
        user_data = {}

        for feature in feature_columns:
            print(f"\nSelecciona un valor para la característica '{feature}':")
            if feature in encoders:
                options = encoders[feature].classes_
                for i, option in enumerate(options, 1):
                    print(f"{i}. {option}")
                choice = int(input("Opción (número): "))
                if 1 <= choice <= len(options):
                    value = options[choice - 1]
                    value = encoders[feature].transform([value])[0]
                    user_data[feature] = value
                else:
                    raise ValueError(f"Opción no válida. Por favor, ingrese un número entre 1 y {len(options)}")
            else:
                value = input(f"{feature}: ")
                user_data[feature] = float(value)

        user_df = pd.DataFrame([user_data])
        prediction = model.predict(user_df)[0]

        if 'User Type' in encoders:
            prediction = encoders['User Type'].inverse_transform([prediction])[0]

        print(f"\nLa categoría predicha para este usuario es: {prediction}")

    except Exception as e:
        print(f"Error durante la clasificación del usuario: {e}")

def main():
    # Cargar datos desde la ruta predefinida
    data = load_and_prepare_data()
    if data is None:
        return

    # Columnas categóricas a codificar
    categorical_cols = [
        'Vehicle Model', 'Charging Station ID',
        'Charging Station Location', 'Time of Day',
        'Day of Week', 'Charger Type', 'User Type'
    ]

    # Codificar variables categóricas
    data, label_encoders = encode_categorical_features(data, categorical_cols)

    # Preparar features (X) y target (y)
    drop_cols = ['User ID', 'Charging Start Time', 'Charging End Time', 'User Type']
    X = data.drop(columns=[col for col in drop_cols if col in data.columns])
    y = data['User Type']

    # División de datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Entrenamiento y evaluación
    model, y_pred = train_and_evaluate_model(X_train, X_test, y_train, y_test)

    # Mostrar métricas
    print("\nReporte de Clasificación:")
    print(classification_report(y_test, y_pred))

    # Visualizar resultados
    if 'User Type' in label_encoders:
        unique_labels = label_encoders['User Type'].classes_
        plot_confusion_matrix(y_test, y_pred, unique_labels)
    plot_feature_importance(model, X.columns)

    # Clasificar un nuevo usuario
    while True:
        classify_new_user(model, label_encoders, X.columns)
        continuar = input("\n¿Desea clasificar otro usuario? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()