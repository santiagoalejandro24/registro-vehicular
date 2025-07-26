from datetime import datetime
import streamlit as st

st.set_page_config(page_title="Control de Vehículos - Huarpe", layout="centered")

st.title("Control de Vehículos - Huarpe Seguridad Integral")
st.subheader("Registro de Ingresos y Egresos")

modo = st.radio("Tipo de Operación", ["Individual", "Convoy"])

def formulario_vehiculo(etiqueta=""):
    with st.expander(f"Formulario {etiqueta}", expanded=True):
        hora = st.time_input("Hora", value=datetime.now().time())
        chofer = st.text_input("Chofer", key=f"chofer_{etiqueta}")
        dni = st.text_input("DNI Chofer", key=f"dni_{etiqueta}")
        acompanantes = st.text_area("Acompañantes y DNI (uno por línea)", key=f"acomp_{etiqueta}")
        ingreso_egreso = st.selectbox("Ingreso o Egreso", ["INGRESO", "EGRESO"], key=f"ie_{etiqueta}")
        patente = st.text_input("Patente", key=f"patente_{etiqueta}")
        empresa = st.text_input("Empresa", key=f"empresa_{etiqueta}")
        pertenece = st.selectbox("Perteneciente a", ["VICUÑA", "FILO", "VICUÑA-FILO"], key=f"pertenece_{etiqueta}")
        destino = st.text_input("Destino", value="GUANDACOL", key=f"destino_{etiqueta}")
        origen = st.text_input("Origen", value="BATIDERO", key=f"origen_{etiqueta}")
        vehiculo = st.text_input("Vehículo", key=f"vehiculo_{etiqueta}")
        antiexplosivo = st.selectbox("Antiestallido", ["SI", "NO"], key=f"anti_{etiqueta}")
        oxigeno = st.selectbox("Oxígeno", ["SI", "NO"], key=f"ox_{etiqueta}")
        combustible = st.selectbox("Combustible", ["SI", "NO"], key=f"comb_{etiqueta}")
        radio = st.selectbox("Radio", ["S/N", "SI", "NO"], key=f"radio_{etiqueta}")
        observacion = st.text_area("Observación", key=f"obs_{etiqueta}")
    return {
        "hora": hora.strftime("%H:%M"),
        "chofer": chofer,
        "dni": dni,
        "acompanantes": acompanantes.strip(),
        "ingreso_egreso": ingreso_egreso,
        "patente": patente,
        "empresa": empresa,
        "pertenece": pertenece,
        "destino": destino,
        "origen": origen,
        "vehiculo": vehiculo,
        "antiexplosivo": antiexplosivo,
        "oxigeno": oxigeno,
        "combustible": combustible,
        "radio": radio,
        "observacion": observacion.strip()
    }

mensajes = []

if modo == "Individual":
    datos = formulario_vehiculo("vehículo")
    mensajes.append(datos)
else:
    st.markdown("### Datos del GIA")
    gia = formulario_vehiculo("GIA")
    cantidad = st.number_input("¿Cuántos vehículos acompañan al GIA?", min_value=1, max_value=10, step=1)
    tipos = []
    for i in range(cantidad):
        tipos.append(st.text_input(f"Tipo de vehículo {i+1} (Ej: Semi, Camioneta)", key=f"tipo_{i}"))
    resumen = f"Guía de {cantidad} " + ", ".join(tipos)
    gia["observacion"] = resumen
    mensajes.append(gia)

    st.markdown("### Vehículos acompañantes")
    for i in range(cantidad):
        datos = formulario_vehiculo(f"acompañante_{i+1}")
        mensajes.append(datos)

if st.button("Generar Mensaje"):
    resultado = ""
    for m in mensajes:
        resultado += f"""HORA: {m['hora']}
CHÓFER: {m['chofer']}
DNI: {m['dni']}
"""
        if m["acompanantes"]:
            resultado += "ACOMPAÑANTES:\n" + "\n".join([f"▪︎ {line.strip()}" for line in m["acompanantes"].split("\n")]) + "\n"
        resultado += f"""INGRESO O EGRESO: {m['ingreso_egreso']}
PATENTE: {m['patente']}
EMPRESA: {m['empresa']}
PERTENECIENTE A: {m['pertenece']}
DESTINO: {m['destino']}
ORIGEN: {m['origen']}
VEHÍCULO: {m['vehiculo']}
ANTI ESTALLIDO: {m['antiexplosivo']}
OXÍGENO: {m['oxigeno']}
COMBUSTIBLE: {m['combustible']}
RADIO: {m['radio']}
OBSERVACIÓN: {m['observacion']}

"""
    st.text_area("Mensaje generado", value=resultado.strip(), height=600)
