# Predicción de enfermedades tiroideas

Trabajo de Fin de Grado sobre la predicción de enfermedades tiroideas mediante modelos de aprendizaje automático.

Se utiliza el conjunto de datos [Thyroid Disease](https://archive.ics.uci.edu/dataset/102/thyroid+disease) para clasificar los registros en tres clases:

- Hipotiroidismo.
- Hipertiroidismo.
- Otro diagnóstico.

El repositorio contiene el análisis exploratorio, el preprocesamiento, el entrenamiento y evaluación de los modelos, los modelos finales guardados y una interfaz desarrollada con Streamlit.

## Instalación

El proyecto utiliza Python 3.12. Las dependencias se pueden instalar mediante:

```bash
pip install -r requirements.txt
```

## Ejecución de la interfaz

```bash
streamlit run interfaz/app.py
```

## Tecnologías

Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Joblib y Streamlit.

## Autor

Francisco Avilés Carrera