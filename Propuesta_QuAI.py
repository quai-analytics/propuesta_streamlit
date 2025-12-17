import streamlit as st
from utils import *

apply_sidebar_style()
mostrar_sidebar_con_logo()

with st.sidebar:
    st.divider()
    st.markdown("### ¿Listo para innovar?")
    st.link_button("📧 Contactar ahora", "mailto:info@quaianalytics.com", type="primary")
    st.caption("Sin compromiso de compra.")

    

mostrar_sidebar_footer()



# --- AGREGAR ESTO AL CSS AL INICIO DE TU APP ---
st.markdown("""
<style>
    .service-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        height: 100%;
        transition: transform 0.2s;
    }
    .service-card:hover {
        transform: translateY(-5px);
        border-color: #000000;
        box-shadow: 0 10px 15px rgba(0,0,0,0.1);
    }
    .service-icon {
        font-size: 2rem;
        margin-bottom: 10px;
    }
    .service-title {
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 8px;
        color: #111827;
    }
    .model-box {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    border: 1px solid #E5E7EB;
    text-align: center;
    height: 100%;
    }
    .service-desc {
        color: #6B7280;
        font-size: 0.9rem;
        line-height: 1.4;
    }
</style>
""", unsafe_allow_html=True)


def model_card(emoji, title, subtitle, desc, color):
    return f"""
    <div class="model-box" style="border-top: 5px solid {color};">
        <div style="font-size: 2rem; margin-bottom: 10px;">{emoji}</div>
        <div style="font-weight: bold; font-size: 1.1rem; color: #333;">{title}</div>
        <div style="font-size: 0.8rem; font-weight: 700; color: {color}; text-transform: uppercase; margin-bottom: 8px;">{subtitle}</div>
        <div style="font-size: 0.9rem; color: #666;">{desc}</div>
    </div>
    """

# Función helper para crear las tarjetas HTML
def card(icon, title, desc):
    return f"""
    <div class="service-card">
        <div class="service-icon">{icon}</div>
        <div class="service-title">{title}</div>
        <div class="service-desc">{desc}</div>
    </div>
    """

# --- CONFIGURACIÓN DE LA PÁGINA ---
# Esto debe ser lo primero que ejecutes.
st.set_page_config(
    page_title="QuAI Analytics | Propuesta Corporativa",
    page_icon="🤖",
    layout="wide",  # 'wide' usa todo el ancho de la pantalla
    initial_sidebar_state="expanded" # 'expanded' mantiene la barra lateral abierta
)

# --- HEADER / LOGO ---
st.title("QuAI Analytics")
st.write("Transformando datos en decisiones inteligentes")


# --- NAVEGACIÓN PRINCIPAL (TABS) ---
# Creamos 4 pestañas principales para no saturar la barra
tab_home, tab_servicios, tab_casos, tab_experiencia, tab_roi = st.tabs([
    "🏠 Quiénes Somos & Filosofía",
    "🛠️ Servicios & Metodología",
    "📈 Casos Reales",
    "🛠️ Stack Tecnológico & Expertise",
    "💰 Retorno de Inversión (ROI)",
])


# ==========================================
# TAB 1: HOME (VISIÓN Y DIFERENCIACIÓN)
# ==========================================
with tab_home:
    st.markdown("### Transformamos lo manual en soluciones estratégicas e inteligentes")
    
    
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown(card("","¿Quienes somos?", 
                        "Somos una consultora panameña especializada en soluciones de IA, Automatización y Analítica Avanzada para negocios locales."), unsafe_allow_html=True)
    with col2:
        st.markdown(card("","Qué hacemos?", 
                        "En términos sencillos, vendemos soluciones a la medida que resuelven los problemas específicos de su negocio."), unsafe_allow_html=True)
    

    st.divider()
    st.info("💡 **En resumen**: Le ayudamos a ahorrar **tiempo y dinero** automatizando lo repetitivo y analizando su información para que pueda tomar mejores decisiones.")
    
    

    st.subheader("👥 Respaldo Técnico y Liderazgo")
    st.markdown("Detrás de la tecnología existe un equipo humano con más de **10 años de experiencia** transformando negocios.")

    # 1. SECCIÓN DE LÍDERES (TARJETAS DE PERFIL)
    # Usamos columnas con bordes para destacar a los expertos
    c_team1, c_team2 = st.columns(2)

    with c_team1:
        with st.container(border=True):
            col_avatar, col_info = st.columns([0.3, 0.7])
            with col_avatar:
                # Placeholder de imagen profesional (o iniciales)
                st.markdown("<div style='font-size: 3rem; text-align: center;'>👨🏻‍💻</div>", unsafe_allow_html=True)
            with col_info:
                st.markdown("#### Ing. Ricardo Alvarez")
                st.caption("MSc, Científico de Datos & Estrategia")
                st.markdown("Especialista en modelos de negocio y analítica avanzada[cite: 124].")

    with c_team2:
        with st.container(border=True):
            col_avatar, col_info = st.columns([0.3, 0.7])
            with col_avatar:
                # Placeholder de imagen profesional
                st.markdown("<div style='font-size: 3rem; text-align: center;'>🚀</div>", unsafe_allow_html=True)
            with col_info:
                st.markdown("#### Ing. Alexander Cuadra")
                st.caption("Ingeniero de Datos & Cloud")
                st.markdown("Experto en arquitectura de datos e infraestructura en la nube[cite: 125].")

st.write("") # Espacio vertical
    
# ==========

with tab_roi:
    st.markdown("### Simule su Ahorro Potencial")
    st.write("¿Cuánto le cuesta la operatividad manual hoy?")

    # Contenedor con fondo suave para diferenciar la calculadora
    with st.container(border=True):
        c_calc1, c_calc2, c_calc3 = st.columns(3)
        
        with c_calc1:
            horas = st.slider("Horas manuales/semana por persona", 1, 40, 10)
        with c_calc2:
            personas = st.number_input("Nº Personas en tareas repetitivas", 1, 50, 2)
        with c_calc3:
            costo = st.number_input("Costo promedio por hora ($)", 5, 100, 15)
            
        ahorro_anual = horas * personas * costo * 52
        
        # Mostrar resultado grande y verde
        st.markdown(f"""
        <div style="text-align: center; padding: 10px;">
            <span style="font-size: 1.2rem; color: #555;">Ahorro Anual Estimado:</span><br>
            <span style="font-size: 2.5rem; font-weight: 800; color: #16A34A;">${ahorro_anual:,.2f}</span>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# TAB 2: SERVICIOS Y CÓMO TRABAJAMOS
# ==========================================
with tab_servicios:
    st.markdown("### Servicios")
    # FILA 1 (3 Servicios)
    c1, c2, c3 = st.columns(3)
    
    with c1:
        # [cite: 31-33]
        st.markdown(card("🧠", "1. Consultoría Estratégica", 
                         "Modelos de negocios digitales y gestión del cambio organizacional."), unsafe_allow_html=True)
    with c2:
        # [cite: 35-37]
        st.markdown(card("🔄", "2. Transformación Digital", 
                         "Diagnóstico tecnológico integral y creación de Roadmap digital."), unsafe_allow_html=True)
    with c3:
        # [cite: 39-40]
        st.markdown(card("⚙️", "3. Automatización (RPA)", 
                         "Optimización operativa y reducción de errores en procesos repetitivos."), unsafe_allow_html=True)

    st.write("") # Espaciador visual

    # FILA 2 (2 Servicios, centrados visualmente)
    # Usamos columnas vacías a los lados para centrar los 2 del medio si quisieras, 
    # o simplemente 2 columnas anchas. Aquí uso 2 columnas directas.
    c4, c5 = st.columns(2)
    
    with c4:
        # [cite: 42-43]
        st.markdown(card("🤖", "4. Inteligencia Artificial (IA)", 
                         "Modelos predictivos, Chatbots AI y Procesamiento de lenguaje natural."), unsafe_allow_html=True)
    with c5:
        # [cite: 45-46]
        st.markdown(card("☁️", "5. Integración de Sistemas", 
                         "Uso de APIs, conexión de ERPs, CRMs y soluciones con recursos en la nube."), unsafe_allow_html=True)

    st.text("")

    st.markdown("### 📦 Modelos de Entrega de Valor")
    col1x, col2x, col3x, col4x = st.columns(4)

    with col1x:
        st.markdown(model_card("🎯", "Proyecto Fijo", "Cerrado", "Alcance y costo definidos.", "#2563EB"), unsafe_allow_html=True)
    with col2x:
        st.markdown(model_card("🧠", "Consultoría", "Diagnóstico", "Propuesta de valor conjunta.", "#9333EA"), unsafe_allow_html=True)
    with col3x:
        st.markdown(model_card("🔄", "Híbrido", "Iterativo", "Alcance base + mejoras continuas.", "#F59E0B"), unsafe_allow_html=True)
    with col4x:
        st.markdown(model_card("🛡️", "Acompañamiento", "Soporte", "Mantenimiento y capacitaciones.", "#10B981"), unsafe_allow_html=True)

    st.markdown("### 📦 Modelos de Entrega de Valor")
    # Usamos columnas con contenedores individuales para dar jerarquía
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        with st.container(border=True):
            st.markdown("### 🎯 Fijo")
            st.write("**Proyecto Cerrado**")
            st.caption("Alcance, costo y tiempo previamente definidos y establecidos.")

    with col2:
        with st.container(border=True):
            st.markdown("### 🧠 Consultoría")
            st.write("**Co-Creación**")
            st.caption("Evaluación integral de procesos y propuesta de valor conjunta.")

    with col3:
        with st.container(border=True):
            st.markdown("### 🔄 Híbrido")
            st.write("**Ágil / Iterativo**")
            st.caption("Alcance preliminar con iteraciones de mejora continua.")

    with col4:
        with st.container(border=True):
            st.markdown("### 🛡️ Soporte")
            st.write("**Acompañamiento**")
            st.caption("Mantenimiento, capacitaciones y soporte continuo post-implementación.")
    
    st.markdown("### Nuestra Metodología de 5 Pasos")
    st.info("Nuestro proceso de 5 pasos garantiza resultados desde el diagnóstico hasta el escalamiento.")
    
    # Usamos un expander para mantenerlo limpio
    with st.expander("Detalle del proceso de trabajo", expanded=True):
        # Barra de progreso visual para dar sensación de flujo
        st.progress(100)
        
        # Definimos los pasos con sus iconos y descripciones exactas [cite: 54-70]
        pasos_info = [
            {
                "titulo": "Diagnóstico",
                "icono": "🔍",
                "desc": "Mapeo y análisis de los procesos actuales para identificar mejoras." 
            },
            {
                "titulo": "Co-diseño",
                "icono": "🎨",
                "desc": "Diseño colaborativo de soluciones adaptadas a su necesidad." 
            },
            {
                "titulo": "Desarrollo",
                "icono": "⚙️",
                "desc": "Configuración y despliegue de pruebas de concepto (PoC)." 
            },
            {
                "titulo": "Entrega",
                "icono": "✅",
                "desc": "Validación de resultados y ajustes de performance." 
            },
            {
                "titulo": "Escalamiento",
                "icono": "🚀",
                "desc": "Ampliación progresiva y soporte continuo." 
            }
        ]
        
        # Creamos las 5 columnas
        cols = st.columns(5)
        
        # Iteramos para rellenar cada columna
        for i, col in enumerate(cols):
            with col:
                # Título con Icono para impacto visual
                st.markdown(f"##### {pasos_info[i]['icono']} {pasos_info[i]['titulo']}")
                # Descripción en texto pequeño (caption) para no saturar
                st.caption(pasos_info[i]['desc'])

    


# ==========================================
# TAB 3: CASOS REALES
# ==========================================
with tab_casos:
    st.header("Resultados Tangibles")
    st.markdown("Transformamos ineficiencias en valor medible.")
    st.write("") # Espacio vertical

    # --- CASO 1: SECTOR ENERGÍA ---
    with st.container(border=True):
        # Encabezado de la Tarjeta
        c_head1, c_head2 = st.columns([0.1, 0.9])
        with c_head1:
            st.title("⚡")
        with c_head2:
            st.subheader("Empresa del Sector Energía")
            st.caption("Optimización de procesos contables y gestión de clientes.")
        
        st.divider()
        
        # Problema vs Solución (Usando componentes nativos)
        col_prob, col_sol = st.columns(2)
        
        with col_prob:
            st.error("**🔴 El Dolor (Antes)**")
            st.markdown("""
            * **Gestión ineficiente:** Poca clasificación y seguimiento de clientes.
            * **Ceguera:** Falta de visibilidad en métricas clave.
            * **Manualidad:** Contabilidad ingresada a mano con errores frecuentes.
            """)
            
        with col_sol:
            st.success("**🟢 La Solución (QuAI)**")
            st.markdown("""
            * **Bots Inteligentes:** Clasificación automática de clientes.
            * **Dashboards:** Monitoreo de KPIs en tiempo real.
            * **Automatización:** Integración directa con sistemas contables.
            """)
            
        st.divider()
        
        # Métricas de Impacto
        m1, m2, m3 = st.columns(3)
        m1.metric(label="⏱️ Tiempo Admin Ahorrado", value="65%", delta="Eficiencia") 
        m2.metric(label="📉 Errores Contables", value="-90%", delta="Calidad", delta_color="inverse") 
        m3.metric(label="🙌 Experiencia Cliente", value="Mejorada", delta="Atención")

    st.write("") # Espaciador entre tarjetas

    # --- CASO 2: SECTOR SALUD ---
    with st.container(border=True):
        # Encabezado de la Tarjeta
        c_head1, c_head2 = st.columns([0.1, 0.9])
        with c_head1:
            st.title("🏥")
        with c_head2:
            st.subheader("Empresa del Sector Salud")
            st.caption("Automatización de agenda y seguimiento de pacientes.")
        
        st.divider()
        
        # Problema vs Solución
        col_prob, col_sol = st.columns(2)
        
        with col_prob:
            st.error("**🔴 El Dolor (Antes)**")
            st.markdown("""
            * **Citas Manuales:** Agendamiento humano generando retrasos.
            * **Pérdida de Tiempo:** Procesos manuales para revisión diaria de pacientes.
            """)
            
        with col_sol:
            st.success("**🟢 La Solución (QuAI)**")
            st.markdown("""
            * **Chatbots:** Automatización de agenda integrada al calendario.
            * **Flujos Automáticos:** Notificaciones y registros automáticos.
            """)
            
        st.divider()
        
        # Métricas de Impacto
        m1, m2, m3 = st.columns(3)
        m1.metric(label="⏱️ Tiempo Admin Ahorrado", value="60%", delta="Eficiencia") # [cite: 102]
        m2.metric(label="✅ Precisión Citas", value="100%", delta="Sin errores") # [cite: 103]
        m3.metric(label="🔔 Recordatorios", value="Automáticos", delta="Experiencia") # [cite: 104]           

# ==========================================
# TAB 4: EXPERIENCIA Y EQUIPO
# ==========================================
with tab_experiencia:
    st.header("🛠️ Stack Tecnológico & Expertise")
    st.write("Nuestra caja de herramientas para construir soluciones robustas.")

    with st.container(border=True):
        st.subheader("☁️ Cloud & Infra")
        # Usando markdown para badges estilo GitHub
        st.markdown("![Azure](https://img.shields.io/badge/Microsoft_Azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white) "
                    "![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) "
                    "![GCP](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)")

    with st.container(border=True):
        st.subheader("🤖 IA & Automatización")
        st.markdown("![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white) "
                    "![UiPath](https://img.shields.io/badge/UiPath-FA4616?style=for-the-badge&logo=uipath&logoColor=white) "
                    "![n8n](https://img.shields.io/badge/n8n-FF6584?style=for-the-badge&logo=n8n&logoColor=white)")

    with st.container(border=True):
        st.subheader("📊 Data & BI")
        st.markdown("![PowerBI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=black) "
                    "![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white) "
                    "![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)")
        
    st.info("🎓 **Certificaciones:** El equipo cuenta con acreditaciones oficiales en AWS, Azure y Databricks. [cite: 120, 121]")
