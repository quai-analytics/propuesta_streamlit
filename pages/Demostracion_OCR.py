import requests
import os
import json

import streamlit as st

from utils import *

apply_sidebar_style()
mostrar_sidebar_con_logo()
mostrar_sidebar_footer()


# --- Configuration ---
# Use Streamlit Secrets! Store your webhook URL and API key (if you set one).
# In .streamlit/secrets.toml:
# N8N_WEBHOOK_URL = "https://your.n8n.instance/webhook/production/your-id"
# N8N_API_KEY = "your-secret-api-key" 
#
# If you didn't set an API key, just comment out the "headers" line below.

if os.environ['USER'] == "appuser":
    # En Streamlit Community Cloud
    N8N_URL = st.secrets["n8n"]["ocr_webhook_url"]
else:
    json_path = os.path.join(os.path.dirname(__file__), "..", "secret_n8n_webhook.json")
    json_path = os.path.abspath(json_path)
    with open(json_path) as f:
        secrets = json.load(f)
    N8N_URL = secrets["dev_server"]
    


N8N_URL = "https://n8n.quaianalytics.com/webhook/15bcbbde-15df-4e36-bd33-7c2a66058169"

# Configuración de página para aprovechar el ancho completo
st.set_page_config(page_title="OCR Inteligente", layout="wide", page_icon="🧾")

st.title("🧾 Digitalización de Facturas")
st.markdown("""
Sube la foto de tu factura. La **Inteligencia Artificial** extraerá los datos automáticamente 
para que solo tengas que revisarlos y aprobarlos.
""")
st.divider()

# Layout Principal
col_left, col_right = st.columns([1, 1.2], gap="large")

# --- 2. GESTIÓN DE ESTADO (MEMORIA) ---
# Esto evita que los datos desaparezcan si el usuario interactúa con la página
if 'ocr_data' not in st.session_state:
    st.session_state.ocr_data = None
if 'ocr_status' not in st.session_state:
    st.session_state.ocr_status = "idle" # idle, processing, done, error

# --- COLUMNA IZQUIERDA: CARGA Y VISTA PREVIA ---
with col_left:

    uploaded_file = st.file_uploader(
            "Arrastra tu factura aquí o haz clic para buscar", 
            type=["jpg", "jpeg", "png", "pdf"],
            help="Soporta imágenes y PDF claros."
        )

    if uploaded_file is not None:
        # Marco visual para la imagen
        with st.container(border=True):
            st.image(uploaded_file, width="content", caption="Vista Previa del Documento")

        # Botón de Procesar (Solo si no hemos procesado ya este archivo específico)
        # Nota: En una app real, podrías resetear el estado si cambia el archivo.
        if st.button("✨ Extraer Datos con IA", type="primary", width="content"):
            st.session_state.ocr_status = "processing"
            
            # --- LÓGICA DE PROCESAMIENTO ---
            with st.spinner("🔍 Analizando píxeles, leyendo textos y detectando montos..."):
                try:
                    files_payload = {
                        'data': (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
                    }
                    response = requests.post(N8N_URL, files=files_payload)

                    if response.status_code == 200:
                        st.session_state.ocr_data = response.json()
                        st.session_state.ocr_status = "done"
                        st.toast("¡Lectura exitosa!", icon="✅")
                    else:
                        st.session_state.ocr_status = "error"
                        st.error(f"Error del servidor: {response.status_code}")
                except Exception as e:
                    st.session_state.ocr_status = "error"
                    st.error(f"Error de conexión: {e}")

# --- COLUMNA DERECHA: RESULTADOS Y EDICIÓN ---
with col_right:
    st.subheader("2. Revisión y Aprobación")

    # CASO 1: Aún no se ha cargado nada
    if uploaded_file is None:
        st.info("👈 Sube una imagen a la izquierda para comenzar.")

    # CASO 2: Procesando (Ya manejado por el spinner, pero podemos poner placeholder)
    elif st.session_state.ocr_status == "processing":
        st.warning("⏳ La IA está leyendo el documento...")

    # CASO 3: Resultados Listos
    elif st.session_state.ocr_status == "done" and st.session_state.ocr_data:
        data = st.session_state.ocr_data

        # --- FORMULARIO DE VERIFICACIÓN ---
        # Usamos un formulario para que el usuario pueda corregir si la IA falló
        with st.form("validation_form"):
            st.write("Verifica los datos extraídos antes de guardar.")
            
            # Tarjeta de Totales (Visualmente destacada)
            c1, c2 = st.columns(2)
            with c1:
                val_total = data.get("total", "0.00")
                # Limpieza básica si viene con simbolos raros
                new_total = st.text_input("💵 Monto Total ($)", value=str(val_total))
            with c2:
                val_factura = data.get("factura", "")
                new_factura = st.text_input("📄 N° Factura", value=str(val_factura))

            st.markdown("---")
            
            # Detalles del Proveedor
            val_empresa = data.get("empresa", "")
            new_empresa = st.text_input("🏢 Proveedor / Empresa", value=str(val_empresa))
            
            c3, c4 = st.columns(2)
            with c3:
                val_ruc = data.get("ruc", "")
                new_ruc = st.text_input("🆔 RUC / ID Fiscal", value=str(val_ruc))
            with c4:
                # Intentamos obtener fecha, si no, fecha de hoy
                val_fecha = data.get("fecha", "")
                new_fecha = st.text_input("📅 Fecha Emisión", value=str(val_fecha))

            st.caption("Si algún campo está vacío, la IA no pudo leerlo con certeza. Por favor complétalo.")

            # --- BOTONES DE ACCIÓN FINAL ---
            col_save, col_discard = st.columns([1, 0.5])
            with col_save:
                confirm_btn = st.form_submit_button("💾 Aprobar y Guardar en ERP", type="primary", width="content")
            with col_discard:
                # Este botón dentro de form actúa como submit también, cuidado. 
                # En forms simples mejor solo tener guardar.
                pass 

        if confirm_btn:
            # Aquí iría la lógica para enviar a tu Base de Datos o ERP real
            st.success(f"✅ Factura #{new_factura} de {new_empresa} guardada correctamente.")
            st.balloons()
            # Opcional: Resetear estado
            # st.session_state.ocr_data = None
            # st.rerun()

        # Debugging (Oculto)
        with st.expander("Ver datos crudos (JSON)"):
            st.json(data)

    # CASO 4: Error
    elif st.session_state.ocr_status == "error":
        st.error("Hubo un problema leyendo la factura. Intenta tomar la foto con mejor iluminación.")
        if st.button("Reintentar"):
            st.session_state.ocr_status = "idle"
            st.rerun()