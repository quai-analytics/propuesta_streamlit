import streamlit as st
from utils import *

apply_sidebar_style()
mostrar_sidebar_con_logo()

# --- DATOS DEL CLIENTE (¡PERSONALIZA ESTO!) ---
# Cambia estos valores para cada propuesta que envíes
CLIENTE_NOMBRE = "NOMBRE-DE-CLIENTE"
CLIENTE_PROBLEMA = "[Problema-Principal-del-Cliente,-ej:-optimizar-su-logística]"
CLIENTE_INDUSTRIA = "[Industria-del-Cliente,-ej:-E-commerce]"


# --- CONFIGURACIÓN DE LA PÁGINA ---
# Esto debe ser lo primero que ejecutes.
st.set_page_config(
    page_title="Propuesta Digital para El Alandalus",
    page_icon="🍷",
    layout="wide",  # 'wide' usa todo el ancho de la pantalla
    initial_sidebar_state="expanded" # 'expanded' mantiene la barra lateral abierta
)


# --- TU INFORMACIÓN (Barra Lateral) ---
with st.sidebar:
    # Puedes poner tu logo aquí
    # st.image("path/a/tu/logo.png", width=150) 
    st.header("Contacto")
    st.write("📧 info@quaianalytics.com")
    st.write("📞 (+507) 6679-1845")
    st.write("[QuAIAnalytics.com](https://www.tuconsultora.com)")


# --- SECCIÓN 1: PORTADA Y GANCHO ---
st.title(f"Propuesta de Estrategia de IA para El Alandalus")
st.subheader(f"De la entrada manual de datos a decisiones con datos en tiempo real.")

st.divider()

st.image("image/alandalus_fachada.jpg", caption="Transformación Digital - El Andalus", width="content")# Foto genérica de restaurante, cámbiala por una del local si tienes

# --- SECCIÓN 2: DIAGNÓSTICO ---
st.header("🔍 1. Nuestro Entendimiento de su Desafío")
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


st.divider()


# --- SECCIÓN 3: LA SOLUCIÓN (ROADMAP) ---
st.header("🗺️ 2. La Solución: Nuestra Hoja de Ruta (Roadmap)")
st.write("Proponemos un enfoque por fases, asegurando valor en cada etapa y mitigando riesgos.")

# Usamos st.tabs para un roadmap interactivo y limpio
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Fase 1: Conexión Segura", 
    "Fase 2: Ingesta de Datos", 
    "Fase 3: Visibilidad (BI)", 
    "Fase 4: Automatización (OCR)",
    "Fase 5: Capacitación"
])

with tab1:
    st.subheader("Fase 1: Infraestructura y Seguridad (Semana 1)")
    st.write("Establecemos el puente seguro entre su restaurante y la nube sin interrumpir la operación diaria.")
    st.markdown("""
    **Acciones Clave:**
    * 🔒 **Instalación de VPN:** Configuramos el túnel encriptado en la computadora de la 'Caja Menuda'.
    * 🛡️ **Permisos de Lectura:** Configuramos el acceso a la base de datos del ERP (Solo lectura para garantizar seguridad).
    * ✅ **Validación de Seguridad:** Pruebas de conexión para asegurar que los datos viajan cifrados.
    
    *Objetivo: Tener acceso a los datos brutos sin depender de un USB o envíos por correo.*
    """)

with tab2:
    st.subheader("Fase 2: Limpieza y Estructura de Datos (Semana 1-2)")
    st.write("Los datos crudos del ERP suelen ser desordenados. Aquí los traducimos a información útil.")
    st.markdown("""
    **Acciones Clave:**
    * 🧹 **Limpieza de Datos:** Estandarización de nombres de platos, categorías e insumos.
    * 🔗 **Modelado de Datos:** Relacionamos las tablas de ventas con las de costos/inventario.
    * ⚙️ **Pipelines Automáticos:** Programamos la actualización de datos (ej: cada noche o cada hora).
    
    *Objetivo: Que los datos estén listos para ser visualizados sin errores.*
    """)

with tab3:
    st.subheader("Fase 3: Despliegue de Dashboards (Semana 3)")
    st.write("Implementamos las interfaces visuales (que ya ha visto en el demo) conectadas a sus datos reales.")
    st.markdown("""
    **Entregables:**
    * 📊 **Dashboard de Ventas:** Análisis por hora, mesero, y plato más vendido en tiempo real.
    * 📉 **Dashboard de Costos:** Control de Food Cost y mermas teóricas.
    * 📱 **Acceso Móvil:** Configuración para que los socios puedan ver los KPIs desde el celular.
    
    *Objetivo: Eliminar el reporte manual de Excel y mejorar la toma de decisiones.*
    """)
    
with tab4:
    st.subheader("Fase 4: Integración de IA / OCR (Semana 4)")
    st.write("Activamos el módulo de Inteligencia Artificial para la carga automática de facturas.")
    st.markdown("""
    **Entregables:**
    * 🤖 **Despliegue del Módulo OCR:** Instalación de la app de escaneo de facturas.
    * 🔄 **Conector de Escritura:** Configuración para que la IA pueda proponer los asientos en el sistema (requiere validación humana al inicio).
    * 🧾 **Pruebas de Estrés:** Escaneo de facturas históricas para validar precisión de lectura de ITBMS y totales.
    
    *Objetivo: Ahorrar esas 2-3 horas diarias de digitación manual.*
    """)

with tab5:
    st.subheader("Fase 5: Adopción y Soporte (Semana 5 en adelante)")
    st.write("La tecnología no sirve si el equipo no la usa. Nos aseguramos de que sepan sacarle provecho.")
    st.markdown("""
    **Entregables:**
    * 🎓 **Entrenamiento al Personal:** Capacitación a la administración sobre cómo usar el escáner OCR y validar datos.
    * 📘 **Manual de Uso:** Guía simple de "Qué hacer si..." (Internet lento, error de lectura, etc.).
    * 🤝 **Soporte Post-Lanzamiento:** Acompañamiento básico para ajustes menores en los reportes.
    
    *Objetivo: Autonomía total del equipo de 'El Andalus'.*
    """)
st.divider()

# --- SECCIÓN 4: ¿POR QUÉ NOSOTROS? (PRUEBA SOCIAL) ---
st.header("🏆 3. ¿Por Qué Nosotros?")
st.write(f"TEnemos más de 10 años de experiencia en el manejo de todo tipo de datos y manejamos la implementación estratégica de la para atender las necesidades del negocio garantizando el aporte del valor.")

# Tu equipo
st.subheader("Equipo de Expertos")
col1, col2 = st.columns(2)
with col1:
    # st.image("path/a/foto1.png")
    st.markdown("**Ing. Ricardo Alvarez**\n*MSc, Científico de Datos*")
    st.write("Experto en Analítica Avanzada de Datos y Gestión Estratégica de Negocios.")
with col2:
    # st.image("path/a/foto2.png")
    st.markdown("**Ing. Alexander Cuadra**\n*Ingeniero de Datos*")
    st.write("Experto en Analítica e Ingeniería de Datos.")

st.divider()

# --- SECCIÓN 5: INVERSIÓN Y ROI ---
st.header("💰 4. Inversión y Retorno (ROI)")

# Elemento estrella: Calculadora de ROI
st.subheader("Calculadora de ROI Interactiva")
st.write("Nuestra solución está diseñada para generar ahorros significativos. Use la calculadora a la derecha para estimar su retorno de inversión.")
col1_, col2_ = st.columns([2,3])
with col1_:
    # Inputs del usuario
    horas_por_tarea = st.slider("Horas diarias ahorradas gracias a nuestra solución", 0.5, 8.0, 3.0, 0.5)
    coste_por_hora = st.number_input("Coste promedio por hora de empleado ($)", min_value=1, max_value=200, value=10, step=1)

with col2_:
    num_empleados = st.slider("Número de empleados que usarán la nueva herramienta", 1, 5, 2)
    
    # Cálculo
    ahorro_semanal = horas_por_tarea * num_empleados * coste_por_hora
    ahorro_mensual = ahorro_semanal * 4.33
    ahorro_anual = ahorro_mensual * 12

    st.success(f"**Ahorro Anual Estimado: ${ahorro_anual:,.2f}**")
st.write(f"Este cálculo se basa en un ahorro de {horas_por_tarea} horas semanales por {num_empleados} empleados. "
         f"Nuestra propuesta busca materializar esta cifra.")


# Paquetes de Inversión
st.header("💰 Inversión y Alcance")
st.write(f"Para El Alandalus, hemos diseñado dos rutas de implementación. Recomendamos el **Plan de Automatización Completa** para maximizar el ahorro de horas hombre.")
# Nombres más comerciales para los paquetes
pkg_bi, pkg_full, pkg_run = st.tabs([
    "📍 Plan A: Control (Solo Dashboards)", 
    "🚀 Plan B: Automatización (BI + OCR) ⭐", 
    "🛠️ Mantenimiento Mensual"
])

# --- PAQUETE 1: SOLO VISUALIZACIÓN ---
with pkg_bi:
    st.subheader("Plan A: Control y Visibilidad")
    st.markdown("Ideal si su prioridad inmediata es *ver* lo que pasa en el negocio, aunque sigan ingresando facturas manualmente.")
    
    col_a1, col_a2 = st.columns([2, 1])
    with col_a1:
        st.markdown("""
        **Incluye (Fases 1, 2 y 3):**
        * ✅ **Infraestructura:** Instalación de VPN Segura en PC Caja Menuda.
        * ✅ **Ingeniería de Datos:** Conexión y limpieza de datos del ERP.
        * ✅ **Dashboards BI:** Tableros de Ventas, Costos y Análisis de Menú.
        * ❌ **No incluye:** Módulo de escaneo de facturas (OCR).
        """)
    with col_a2:
        st.metric(label="Inversión Única", value="$1,500")
        st.caption("Tiempo de entrega: 3 Semanas")

# --- PAQUETE 2: RECOMENDADO (TODO) ---
with pkg_full:
    st.success("Opción Recomendada: El mayor retorno de inversión (ROI)")
    st.subheader("Plan B: Eficiencia y Ahorro Total")
    st.markdown("La solución completa. Elimina la ceguera operativa Y la digitación manual.")
    
    col_b1, col_b2 = st.columns([2, 1])
    with col_b1:
        st.markdown("""
        **Incluye Todo el Plan A + (Fases 4 y 5):**
        * ✨ **Todo lo del Plan A.**
        * ✅ **App de OCR:** Módulo de Inteligencia Artificial para lectura de facturas.
        * ✅ **Automatización:** Inyección de datos de facturas (Proveedor, ITBMS, Totales).
        * ✅ **Capacitación:** Entrenamiento al personal administrativo.
        * ✅ **Soporte de Lanzamiento:** 1 mes de monitoreo intensivo.
        """)
    with col_b2:
        st.metric(label="Inversión Única", value="$2,500") # Pon un precio bundle atractivo
        st.caption("Tiempo de entrega: 5-6 Semanas")
        st.caption("🎯 *Ahorro estimado: 60-80 horas/mes*")

# --- MANTENIMIENTO (IMPORTANTÍSIMO PARA SAAS) ---
with pkg_run:
    st.subheader("Soporte y Evolución Continua")
    st.write("El software en la nube necesita cuidado. Este fee mensual asegura que todo siga funcionando 24/7.")
    st.markdown("""
    **El servicio mensual incluye:**
    * ☁️ **Hosting:** Costos de servidores y base de datos en la nube.
    * 🔒 **Monitoreo VPN:** Asegurar que la conexión con el restaurante no se caiga.
    * 🐛 **Soporte Técnico:** Corrección de errores y dudas del equipo.
    * 🔄 **Actualizaciones Menores:** Ajustes pequeños en los gráficos.
    """)
    st.info("**Costo Mensual Sugerido: $100 / mes** (Inicia después de la entrega final)")

st.divider()

# --- VALIDACIÓN DE PRECIO (PSICOLOGÍA DE VENTAS) ---
# Esto ayuda a justificar el precio mostrando lo caro que es NO hacerlo
if st.checkbox("¿Por qué esta inversión? (Ver análisis comparativo)"):
    st.markdown(f"""
    | Concepto | Costo Actual (Manual) | Con Nuestra Solución |
    | :--- | :--- | :--- |
    | **Costo de Digitalización (Anual)** | $ {ahorro_anual:,.0f} (aprox) | **$0** (Automatizado) |
    | **Errores Humanos** | Frecuentes (Dedo de error) | **Mínimos** (Validación IA) |
    | **Tiempo de Reportes** | Días (Cierre de mes) | **Segundos** (Tiempo Real) |
    | **Decisiones** | Basadas en intuición | **Basadas en Datos** |
    """)
st.divider()

# --- SECCIÓN 6: PRÓXIMOS PASOS (CTA) ---
st.header("🏁 5. Próximos Pasos")
st.write(f"Estamos listos para ayudar a El Alandalus a optimizar la toma de decisión apoyado por la digitalización de procesos. "
         "El siguiente paso es una reunión de 30 minutos para discutir esta propuesta y ajustar el alcance.")

col1, col2 = st.columns(2)

with col1:
    # Reemplaza esto con tu enlace real de Calendly, HubSpot, etc.
    st.link_button("Agendar Reunión de Inicio (30 min)", "https://calendly.com/tu-usuario", type="primary")

with col2:
    if st.button("Aprobar Propuesta Digitalmente"):
        st.success("¡Excelente decisión! Hemos sido notificados. Nos pondremos en contacto en breve para formalizar el inicio.")
        # Aquí podrías agregar una lógica para enviar un email
        st.balloons()


mostrar_sidebar_footer()
