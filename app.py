import streamlit as st
import pandas as pd
import urllib.parse

st.set_page_config(page_title="Registro Vehicular", layout="centered")
st.title("Registro Ingreso/Egreso de Personal en Vehículo")
st.markdown("Garita Batidero - Proyecto Vicuña")

# Campos del formulario
hora = st.text_input("Hora (opcional)")
chofer = st.text_input("Nombre del Chófer")
dni_chofer = st.text_input("DNI del Chófer")
acompañantes = st.text_area("Acompañantes con DNI (formato libre)")

ingreso_egreso = st.selectbox("Ingreso o Egreso", ["EGRESO", "INGRESO"])
vehiculo = st.text_input("Tipo de vehículo")
patente = st.text_input("Patente")
empresa = st.text_input("Empresa")
perteneciente_a = st.selectbox("Perteneciente a", ["VICUÑA", "VICUÑA FILO"])
col1, col2 = st.columns(2)
origen = col1.selectbox("Origen", ["BATIDERO", "GUANDACOL"])
destino = col2.selectbox("Destino", ["GUANDACOL", "BATIDERO"])
observacion = st.text_area("Observaciones", value="s.n")

# Botón para registrar y generar mensaje
if st.button("Registrar y generar mensaje de WhatsApp"):
    mensaje = f"""HORA: {hora}
CHÓFER: {chofer}
DNI: {dni_chofer}
ACOMPAÑANTES:
{acompañantes}
INGRESO O EGRESO: {ingreso_egreso.lower()}
PATENTE: {patente}
EMPRESA: {empresa}
PERTENECIENTE A: {perteneciente_a}
DESTINO: {destino.capitalize()}
ORIGEN: {origen.capitalize()}
VEHÍCULO: {vehiculo.upper()}
ANTI ESTALLIDO: SI
OXÍGENO: SI
COMBUSTIBLE: SI
RADIO: S/N
OBSERVACIÓN: {observacion}"""

    mensaje_encoded = urllib.parse.quote(mensaje)
    numero_whatsapp = ""  # Ejemplo: "5491234567890"
    enlace = f"https://wa.me/{numero_whatsapp}?text={mensaje_encoded}"

    st.success("Mensaje generado correctamente.")
    st.markdown(f"[Abrir WhatsApp con el mensaje]({enlace})", unsafe_allow_html=True)

    # Guardar registro (opcional)
    datos = {
        "Hora": hora,
        "Chófer": chofer,
        "DNI Chófer": dni_chofer,
        "Acompañantes": acompañantes,
        "Ingreso/Egreso": ingreso_egreso,
        "Vehículo": vehiculo,
        "Patente": patente,
        "Empresa": empresa,
        "Perteneciente a": perteneciente_a,
        "Origen": origen,
        "Destino": destino,
        "Observación": observacion,
    }
    df = pd.DataFrame([datos])
    df.to_csv("registro_vehicular.csv", mode='a', header=False, index=False)
