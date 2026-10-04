import joblib
import pandas as pd


class PredictorTiroides:

    def __init__(self, ruta_modelo):
        artefacto = joblib.load(ruta_modelo)

        self.modelo = artefacto["modelo"]
        self.columnas = artefacto["columnas"]

    def preparar_entrada(self, datos_paciente):
        entrada = pd.DataFrame([datos_paciente])

        entrada = entrada.reindex(
            columns=self.columnas
        )

        return entrada

    def predecir(self, datos_paciente):
        entrada = self.preparar_entrada(
            datos_paciente
        )

        clase = self.modelo.predict(
            entrada
        )[0]

        probabilidades = None

        if hasattr(self.modelo, "predict_proba"):
            probabilidades = self.modelo.predict_proba(
                entrada
            )[0]

        return clase, probabilidades

    def obtener_clases(self):
        return self.modelo.classes_
