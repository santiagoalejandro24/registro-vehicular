import streamlit as st
import pandas as pd
import urllib.parse

st.set_page_config(page_title="Registro Vehicular", layout="centered")
st.title("📋 Registro Ingreso/Egreso de Personal en Vehículo")
st.markdown("Garita **Batidero** - Proyecto Vicuña")

# Campos del formulario
hora = st.text_input("Hora (opcional)")
chofer = st.text_input("Nombre del Chófer")
dni_chofer = st.text_input("DNI del Chófer")
acompañantes = st.text_area("Acompañantes con DNI (formato: Nombre - DNI por línea)")

ingreso_egreso = st.selectbox("Ingreso o Egreso", ["EGRESO", "INGRESO"])
vehiculo = st.text_input("Tipo de vehículo")
empresa = st.text_input("Empresa")
perteneciente_a = st.selectbox("Perteneciente a", ["Vicuña", "Vicuña Filo"])

col1, col2 = st.columns(2)
origen = col1.selectbox("Origen", ["BATIDERO", "GUANDACOL"])
destino = col2.selectbox("Destino", ["GUANDACOL", "BATIDERO"])

observacion = st.text_area("Observaciones", value="s.n")

if st.button("📤 Registrar y generar WhatsApp"):
    # Armado del mensaje de WhatsApp
    mensaje = f"""📋 *Registro de {ingreso_egreso}*  
🕒 Hora: {hora or "s/n"}  
🚗 Vehículo: {vehiculo}  
👨‍✈️ Chófer: {chofer}  
🆔 DNI Chófer: {dni_chofer}  
🧍‍♂️ Acompañantes:
{acompañantes}  
🏢 Empresa: {empresa}  
📍 Origen: {origen}  
📍 Destino: {destino}  
📌 Perteneciente a: {perteneciente_a}  
📝 Observación: {observacion}
"""
    # Se codifica el mensaje para URL
    mensaje_encoded = urllib.parse.quote(mensaje)

    # Número de WhatsApp al que se envía. (completá si querés que sea fijo)
    numero_whatsapp = ""
    enlace = f"https://wa.me/{numero_whatsapp}?text={mensaje_encoded}"

    st.success("✅ Registro generado correctamente.")
    st.markdown(f"[📲 Enviar por WhatsApp]({enlace})", unsafe_allow_html=True)

    # Guardado local (opcional en el servidor)
    datos = {
        "Hora": hora,
        "Chófer": chofer,
        "DNI Chófer": dni_chofer,
        "Acompañantes": acompañantes,
        "Ingreso/Egreso": ingreso_egreso,
        "Vehículo": vehiculo,
        "Empresa": empresa,
        "Perteneciente a": perteneciente_a,
        "Origen": origen,
        "Destino": destino,
        "Observación": observacion,
    }
    df = pd.DataFrame([datos])
    df.to_csv("registro_vehicular.csv", mode='a', header=False, index=False)
