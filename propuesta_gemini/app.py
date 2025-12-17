import streamlit as st
# from utils import * # Asegúrate de tener tus estilos aquí
# Si tienes tus demos en otros archivos, impórtalos así:
# from modules import ocr_demo, dash_demo 

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(
    page_title="Propuesta Digital - El Andalus",
    page_icon="🍷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS PERSONALIZADOS (Pequeño toque elegante) ---
st.markdown("""
<style>
    .big-font { font-size:24px !important; color: #2E86C1; }
    .metric-card { background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #ff4b4b; }
</style>
""", unsafe_allow_html=True)

# --- VARIABLES DEL CLIENTE ---
CLIENTE = "Restaurante El Andalus"
PROYECTO = "Automatización Financiera & Inteligencia de Negocios"

# --- SIDEBAR ---
with st.sidebar:
    st.title("👨‍🍳 Menú de la Propuesta")
    st.info(f"Preparada para: **{CLIENTE}**")
    
    section = st.radio("Ir a sección:", 
        ["1. El Reto & Solución", "2. Demo: Tableros (BI)", "3. Demo: OCR Facturas", "4. ROI & Inversión", "5. Arquitectura Técnica"])
    
    st.divider()
    st.write("**Contacto:**")
    st.write("📞 (+507) 6679-1845")
    st.write("📧 tu_email@quaianalytics.com")

# ==========================================
# SECCIÓN 1: EL RETO Y LA SOLUCIÓN (VENTA)
# ==========================================
if section == "1. El Reto & Solución":
    st.title(f"🚀 Transformación Digital para {CLIENTE}")
    st.subheader("De la entrada manual de datos a decisiones en tiempo real.")
    
    st.image("https://images.unsplash.com/photo-1517248135467-4c7edcad34c4", caption="Optimización para El Andalus", use_column_width=True)# Foto genérica de restaurante, cámbiala por una del local si tienes
 
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🛑 La Situación Actual")
        st.warning("""
        * **Ceguera Operativa:** Los reportes dependen de alguien tecleando datos manualmente.
        * **Tiempo Perdido:** El equipo administrativo pierde **2-3 horas diarias** transcribiendo facturas al ERP.
        * **Datos Aislados:** La información valiosa vive atrapada en la computadora de la "Caja Menuda".
        """)
    
    with col2:
        st.markdown("### ✅ Nuestra Solución")
        st.success("""
        * **Conexión Segura (VPN):** Extraemos los datos de su ERP automáticamente sin cambiar su software actual.
        * **Inteligencia (BI):** Dashboards que se actualizan solos para ver ventas y costos al instante.
        * **Automatización (OCR):** Escanee una factura y deje que la IA la ingrese al sistema por usted.
        """)

# ==========================================
# SECCIÓN 2: DEMO DASHBOARDS (TU CÓDIGO EXISTENTE)
# ==========================================
elif section == "2. Demo: Tableros (BI)":
    st.title("📊 Sus Datos, Visualizados")
    st.markdown("""
    Esta es una muestra real de cómo se vería la información extraída directamente de su ERP a través de nuestra conexión segura.
    *Ya no es necesario esperar al cierre de mes para saber cómo va el negocio.*
    """)
    
    st.divider()
    
    # --- AQUÍ INTEGRAS TU CÓDIGO DE DASHBOARD ---
    # Opción A: Si lo tienes en una función en otro archivo:
    # dash_demo.mostrar_dashboard()
    
    # Opción B: Pegas aquí una versión simplificada de tu código visual:
    
    # --- EJEMPLO SIMULADO (Reemplaza esto con tu código real) ---
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Ventas de Hoy", "$1,240.50", "+15%")
    col2.metric("Ticket Promedio", "$45.00", "+2%")
    col3.metric("Plato Más Vendido", "Paella Marisco", "32 Unidades")
    col4.metric("Costo Alimentos (Food Cost)", "28%", "-2% (Mejora)")
    
    st.subheader("Análisis de Ventas por Hora")
    st.bar_chart({"12pm": 400, "1pm": 800, "2pm": 650, "7pm": 900, "8pm": 1100, "9pm": 700})
    
    st.info("💡 **Insight:** Con esta herramienta, detectamos que su pico de ventas los martes es inusual, permitiendo ajustar el personal.")
    # -------------------------------------------------------------

# ==========================================
# SECCIÓN 3: DEMO OCR (TU CÓDIGO EXISTENTE)
# ==========================================
elif section == "3. Demo: OCR Facturas":
    st.title("🧾 Adiós a la Digitación Manual")
    st.markdown("""
    Nuestro módulo de IA lee las facturas de proveedores (fotos o PDF) y extrae:
    **Proveedor, Fecha, Totales e ITBMS** automáticamente.
    """)
    
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("#### 1. Pruebe subir una factura")
        uploaded_file = st.file_uploader("Subir imagen de factura (Demo)", type=['png', 'jpg', 'jpeg', 'pdf'])
        if uploaded_file:
            st.image(uploaded_file, caption="Factura subida", width=300)
    
    with col2:
        st.markdown("#### 2. Resultado de la IA")
        if uploaded_file:
            with st.spinner('La IA está leyendo la factura...'):
                import time
                time.sleep(2) # Simulación de proceso
                
                # --- AQUÍ INTEGRAS TU LÓGICA DE OCR ---
                # ocr_data = mi_funcion_ocr(uploaded_file)
                
                # Resultado Simulado:
                st.json({
                    "Proveedor": "Distribuidora de Carnes S.A.",
                    "RUC": "1234-5678-DV90",
                    "Fecha": "16/12/2025",
                    "Subtotal": 350.00,
                    "ITBMS": 24.50,
                    "TOTAL": 374.50
                })
                st.success("✅ Datos listos para enviar a su ERP")
        else:
            st.info("Suba una imagen para ver la magia.")

# ==========================================
# SECCIÓN 4: ROI (CALCULADORA DE PANAMÁ)
# ==========================================
elif section == "4. ROI & Inversión":
    st.title("💰 Retorno de Inversión")
    st.markdown("¿Cuánto le cuesta a **El Andalus** seguir haciendo las cosas manuales?")
    
    st.markdown("#### Calculadora de Ahorro")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        horas_diarias = st.number_input("Horas diarias dedicadas a reportes/digitación", value=2.5, step=0.5)
    with c2:
        dias_mes = st.number_input("Días operativos al mes", value=26)
    with c3:
        # Salario base administrativo Panamá aprox $700-$900, hora aprox $4.50 - $6.00
        costo_hora = st.number_input("Costo por hora del personal ($)", value=6.00)

    ahorro_mensual = horas_diarias * dias_mes * costo_hora
    ahorro_anual = ahorro_mensual * 12
    
    st.markdown("---")
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>💸 Dinero Perdido Anualmente</h3>
            <h1 style="color: #ff4b4b">${ahorro_anual:,.2f}</h1>
            <p>En tiempo administrativo improductivo.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_res2:
        st.markdown(f"""
        <div class="metric-card" style="border-left: 5px solid #28B463;">
            <h3>🚀 Valor Estratégico</h3>
            <p>Además del ahorro directo, usted gana:</p>
            <ul>
                <li>Detección temprana de robo hormiga o mermas.</li>
                <li>Negociación con proveedores basada en datos reales.</li>
                <li>Gerente enfocado en clientes, no en Excel.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# SECCIÓN 5: ARQUITECTURA TÉCNICA (VPN)
# ==========================================
elif section == "5. Arquitectura Técnica":
    st.title("🔒 Seguridad y Conexión")
    st.write("Entendemos que la seguridad de sus datos financieros es crítica. Así es como conectaremos su ERP local a la nube.")
    
    # Diagrama simple usando graphviz
    st.graphviz_chart("""
    digraph {
        rankdir=LR;
        node [shape=box, style=filled, fillcolor=lightgrey];
        
        PC [label="💻 PC Caja Menuda\n(En el Restaurante)", fillcolor="#FFCDD2"];
        VPN [label="🔒 VPN Segura\n(Túnel Encriptado)", shape=ellipse, fillcolor="#FFF9C4"];
        Cloud [label="☁️ Servidor QuAI\n(Procesamiento)", fillcolor="#BBDEFB"];
        App [label="📱 App Streamlit\n(Dashboard & OCR)", fillcolor="#C8E6C9"];
        
        PC -> VPN [label="Datos ERP"];
        VPN -> Cloud;
        Cloud -> App [label="Insights"];
    }
    """)
    
    st.warning("**Nota de Privacidad:** La conexión es de solo lectura (para dashboards) y los datos viajan encriptados. Nadie externo tiene acceso a su PC.")
    
    st.markdown("### Próximos Pasos")
    if st.button("Agendar Instalación Técnica (Visita al Restaurante)"):
        st.balloons()
        st.success("¡Solicitud enviada! Nos coordinaremos para instalar el VPN en la PC de administración.")