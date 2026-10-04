import numpy as np
import streamlit as st


def mostrar_datos_generales():

    columna1, columna2 = st.columns(2)

    with columna1:
        edad = st.number_input(
            "Edad",
            min_value=1,
            max_value=110,
            value=55
        )

    with columna2:
        sexo_texto = st.selectbox(
            "Sexo",
            [
                "Mujer",
                "Hombre",
                "No indicado"
            ]
        )

    mapa_sexo = {
        "Mujer": 0,
        "Hombre": 1,
        "No indicado": np.nan
    }

    return {
        "edad": edad,
        "sexo": mapa_sexo[sexo_texto]
    }


def mostrar_datos_clinicos():

    st.subheader("Antecedentes y tratamientos")

    variables = {
        "tratamiento_con_tiroxina":
            "Tratamiento con tiroxina",

        "consulta_sobre_tiroxina":
            "Consulta sobre tiroxina",

        "medicacion_antitiroidea":
            "Medicación antitiroidea",

        "enfermo":
            "Paciente enfermo",

        "embarazada":
            "Embarazada",

        "cirugia_tiroidea":
            "Cirugía tiroidea",

        "tratamiento_I131":
            "Tratamiento con I131",

        "consulta_hipotiroidismo":
            "Consulta por hipotiroidismo",

        "consulta_hipertiroidismo":
            "Consulta por hipertiroidismo",

        "litio":
            "Tratamiento con litio",

        "bocio":
            "Bocio",

        "tumor":
            "Tumor",

        "hipopituitarismo":
            "Hipopituitarismo",

        "trastorno_psiquiatrico":
            "Trastorno psiquiátrico"
    }

    resultados = {}

    columna1, columna2 = st.columns(2)

    for posicion, (variable, etiqueta) in enumerate(
        variables.items()
    ):
        columna = (
            columna1
            if posicion % 2 == 0
            else columna2
        )

        with columna:
            resultados[variable] = int(
                st.checkbox(
                    etiqueta,
                    key=variable
                )
            )

    return resultados


def mostrar_hormona(
    nombre,
    valor_inicial,
    paso,
    formato
):

    medida = st.checkbox(
        f"{nombre} medida",
        value=True,
        key=f"{nombre}_medida"
    )

    valor = st.number_input(
        f"Valor de {nombre}",
        min_value=0.0,
        value=float(valor_inicial),
        step=float(paso),
        format=formato,
        disabled=not medida,
        key=f"{nombre}_valor"
    )

    if not medida:
        valor = np.nan

    return valor, int(medida)


def mostrar_datos_hormonales():

    st.subheader("Resultados hormonales")

    columna1, columna2 = st.columns(2)

    with columna1:
        TSH, TSH_medida = mostrar_hormona(
            "TSH", 1.40, 0.10, "%.2f"
        )

        T3, T3_medida = mostrar_hormona(
            "T3", 1.90, 0.10, "%.2f"
        )

        TT4, TT4_medida = mostrar_hormona(
            "TT4", 105.0, 1.0, "%.1f"
        )

    with columna2:
        T4U, T4U_medida = mostrar_hormona(
            "T4U", 0.96, 0.01, "%.2f"
        )

        FTI, FTI_medido = mostrar_hormona(
            "FTI", 110.0, 1.0, "%.1f"
        )

    return {
        "TSH_medida": TSH_medida,
        "TSH": TSH,
        "T3_medida": T3_medida,
        "T3": T3,
        "TT4_medida": TT4_medida,
        "TT4": TT4,
        "T4U_medida": T4U_medida,
        "T4U": T4U,
        "FTI_medido": FTI_medido,
        "FTI": FTI
    }
