import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

def load_and_prepare_data():
    """
    Carga y prepara los datos desde un archivo CSV fijo.
    Returns:
        pandas.DataFrame: Dataset preparado
    """
    file_path = "/home/santiagodc/Documentos/ucc-repos/ucc-machine-learnig/csv/carro_electrico.csv"
    try:
        # Leer archivo CSV
        data = pd.read_csv(file_path)
        print(f"\nDatos cargados exitosamente. Dimensiones del dataset: {data.shape}")
        return data
    except Exception as e:
        print(f"Error al cargar los datos: {str(e)}")
        return None

def encode_categorical_features(data):
    """
    Codifica variables categóricas usando LabelEncoder
    Args:
        data (pandas.DataFrame): Dataset original
    Returns:
        tuple: (DataFrame procesado, diccionario de encoders)
    """
    label_encoders = {}
    categorical_cols = ['Vehicle Model', 'Charging Station ID',
                       'Charging Station Location', 'Time of Day',
                       'Day of Week', 'Charger Type', 'User Type']

    for col in categorical_cols:
        if col in data.columns:
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col])
            label_encoders[col] = le
            print(f"Codificada la columna: {col}")

    return data, label_encoders

def train_and_evaluate_model(X_train, X_test, y_train, y_test):
    """
    Entrena y evalúa el modelo Random Forest
    Returns:
        tuple: (modelo entrenado, predicciones)
    """
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )

    # Entrenamiento
    model.fit(X_train, y_train)

    # Cross-validation
    cv_scores = cross_val_score(model, X_train, y_train, cv=5)
    print(f"\nScore de validación cruzada: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")

    # Predicciones
    y_pred = model.predict(X_test)

    return model, y_pred

def plot_confusion_matrix(y_test, y_pred, labels):
    """
    Visualiza la matriz de confusión
    """
    plt.figure(figsize=(10, 8))
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=labels, yticklabels=labels)
    plt.title('Matriz de Confusión')
    plt.ylabel('Valor Real')
    plt.xlabel('Predicción')
    plt.show()

def plot_feature_importance(model, feature_names):
    """
    Visualiza la importancia de las características
    """
    importances = pd.DataFrame({
        'feature': feature_names,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='importance', y='feature', data=importances)
    plt.title('Importancia de las Características')
    plt.show()

def main():
    # Cargar datos
    data = load_and_prepare_data()
    if data is None:
        return

    # Codificar variables categóricas
    data, label_encoders = encode_categorical_features(data)

    # Preparar features y target
    X = data.drop(columns=['User ID', 'Charging Start Time',
                          'Charging End Time', 'User Type'])
    y = data['User Type']

    # División de datos
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Entrenamiento y evaluación
    model, y_pred = train_and_evaluate_model(X_train, X_test, y_train, y_test)

    # Mostrar resultados
    print("\nReporte de Clasificación:")
    print(classification_report(y_test, y_pred))

    # Visualizaciones
    unique_labels = label_encoders['User Type'].classes_
    plot_confusion_matrix(y_test, y_pred, unique_labels)
    plot_feature_importance(model, X.columns)

    return model, label_encoders

if __name__ == "__main__":
    model, encoders = main()
