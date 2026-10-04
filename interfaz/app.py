import pandas as pd
import streamlit as st

from formulario import (
    mostrar_datos_generales,
    mostrar_datos_clinicos,
    mostrar_datos_hormonales
)

from modelo_tiroides import PredictorTiroides


st.set_page_config(
    page_title="Predicción tiroidea",
    page_icon="🩺"
)


@st.cache_resource
def cargar_predictor():
    return PredictorTiroides(
        "modelo_lr_tiroides.joblib"
    )


predictor = cargar_predictor()


st.title("Predicción de enfermedad tiroidea")

st.warning(
    "Aplicación con finalidad académica. "
    "No sustituye un diagnóstico médico."
)


datos_generales = mostrar_datos_generales()
datos_clinicos = mostrar_datos_clinicos()
datos_hormonales = mostrar_datos_hormonales()


datos_paciente = {
    **datos_generales,
    **datos_clinicos,
    **datos_hormonales
}


if st.button(
    "Realizar predicción",
    type="primary",
    use_container_width=True
):

    clase, probabilidades = predictor.predecir(
        datos_paciente
    )

    st.success(
        f"Resultado estimado: {clase}"
    )

    if probabilidades is not None:

        tabla = pd.DataFrame({
            "Clase": predictor.obtener_clases(),
            "Probabilidad": probabilidades * 100
        })

        tabla = tabla.sort_values(
            "Probabilidad",
            ascending=False
        )

        st.dataframe(
            tabla.style.format({
                "Probabilidad": "{:.2f}%"
            }),
            hide_index=True,
            use_container_width=True
        )

        st.bar_chart(
            tabla.set_index("Clase")["Probabilidad"]
        )

    else:
        st.info(
            "El modelo seleccionado no proporciona "
            "probabilidades."
        )
