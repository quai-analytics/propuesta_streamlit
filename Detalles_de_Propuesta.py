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
    page_title=f"Propuesta de Estrategia de IA para {CLIENTE_NOMBRE}",
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
st.title(f"Propuesta de Estrategia de Datos e IA para El Alandalus")
st.subheader("De la entrada manual de datos a decisiones estratégicas en tiempo real")

st.divider()

# Usamos 'use_column_width' para que la imagen se ajuste mejor al layout.
st.image("image/alandalus_fachada.jpg", caption="Hacia la Transformación Digital de El Alandalus", width="stretch")

# --- SECCIÓN 2: DIAGNÓSTICO ---
st.header("1. Nuestro Entendimiento de su Desafío")
col1, col2 = st.columns(2)

# Reemplazamos st.warning y st.success por contenedores con borde para un look más profesional.
with col1:
    with st.container(border=True):
        st.markdown("### La Situación Actual")
        st.markdown("""
        * **Dependencia de Procesos Manuales:** La generación de reportes críticos depende de la entrada manual de datos, lo que puede introducir errores y retrasos.
        * **Ineficiencia Operativa:** El equipo administrativo invierte un tiempo considerable (estimado en **2-3 horas diarias**) en la transcripción de facturas al sistema ERP.
        * **Silos de Información:** Los datos valiosos de la operación diaria permanecen aislados en equipos específicos, limitando su acceso y aprovechamiento estratégico.
        """)

with col2:
    with st.container(border=True):
        st.markdown("### Nuestra Solución Propuesta")
        st.markdown("""
        * **Acceso Centralizado y Seguro:** Implementamos una conexión VPN para extraer datos del ERP de forma automática y segura, sin alterar su software actual.
        * **Inteligencia de Negocio (BI):** Desarrollamos dashboards interactivos que se actualizan en tiempo real, ofreciendo visibilidad instantánea de ventas, costos y KPIs.
        * **Automatización Inteligente (OCR):** Integramos una solución de IA que digitaliza e ingresa automáticamente la información de las facturas al sistema.
        """)


st.divider()


# --- SECCIÓN 3: LA SOLUCIÓN (ROADMAP) ---
st.header("2. La Solución: Nuestra Hoja de Ruta")
st.write("Proponemos un enfoque por fases, asegurando valor en cada etapa y mitigando riesgos.")

# Usamos st.tabs para un roadmap interactivo y limpio
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Fase 1: Infraestructura y Seguridad", 
    "Fase 2: Ingeniería de Datos", 
    "Fase 3: Visualización (BI)", 
    "Fase 4: Automatización (IA/OCR)",
    "Fase 5: Adopción y Soporte"
])

with tab1:
    st.subheader("Fase 1: Infraestructura y Seguridad (Semana 1)")
    st.write("Establecemos el puente seguro entre su restaurante y la nube sin interrumpir la operación diaria.")
    st.markdown("""
    **Acciones Clave:**
    * **Instalación de VPN:** Configuramos un túnel encriptado en el equipo designado.
    * **Permisos de Acceso:** Se configura el acceso de solo lectura a la base de datos del ERP para garantizar la integridad de sus datos.
    * ✅ **Validación de Seguridad:** Pruebas de conexión para asegurar que los datos viajan cifrados.
    
    *Objetivo: Tener acceso a los datos brutos sin depender de un USB o envíos por correo.*
    """)

with tab2:
    st.subheader("Fase 2: Limpieza y Estructura de Datos (Semana 1-2)")
    st.write("Los datos crudos del ERP suelen ser desordenados. Aquí los traducimos a información útil.")
    st.markdown("""
    **Acciones Clave:**
    * **Limpieza y Estandarización:** Homologación de nombres de productos, categorías e insumos para consistencia analítica.
    * **Modelado de Datos:** Creación de un modelo que relacione las tablas de ventas, costos e inventario.
    * **Pipelines de Datos:** Programación de procesos automáticos para la extracción y actualización de datos.
    
    *Objetivo: Que los datos estén listos para ser visualizados sin errores.*
    """)

with tab3:
    st.subheader("Fase 3: Despliegue de Dashboards (Semana 3)")
    st.write("Implementamos las interfaces visuales (que ya ha visto en el demo) conectadas a sus datos reales.")
    st.markdown("""
    **Entregables:**
    * **Dashboard de Ventas:** Análisis por franja horaria, personal y producto más vendido.
    * **Dashboard de Costos:** Control de *Food Cost* y análisis de mermas teóricas.
    * **Acceso Móvil:** Habilitación de acceso a los KPIs clave desde dispositivos móviles para la gerencia.
    
    *Objetivo: Eliminar el reporte manual de Excel y mejorar la toma de decisiones.*
    """)
    
with tab4:
    st.subheader("Fase 4: Integración de IA / OCR (Semana 4)")
    st.write("Activamos el módulo de Inteligencia Artificial para la carga automática de facturas.")
    st.markdown("""
    **Entregables:**
    * **Módulo OCR:** Despliegue de la aplicación de escaneo y reconocimiento de facturas.
    * **Conector al ERP:** Configuración para que la IA proponga asientos contables en el sistema (requiere validación humana inicial).
    * **Pruebas de Precisión:** Procesamiento de un lote de facturas históricas para validar la precisión del modelo.
    
    *Objetivo: Ahorrar esas 2-3 horas diarias de digitación manual.*
    """)

with tab5:
    st.subheader("Fase 5: Adopción y Soporte (Semana 5 en adelante)")
    st.write("La tecnología no sirve si el equipo no la usa. Nos aseguramos de que sepan sacarle provecho.")
    st.markdown("""
    **Entregables:**
    * **Sesiones de Capacitación:** Entrenamiento dirigido al personal administrativo sobre el uso de la herramienta OCR y el proceso de validación.
    * **Documentación y Guías:** Elaboración de un manual de usuario y guías de referencia rápida.
    * **Soporte Post-Lanzamiento:** Acompañamiento durante las primeras semanas para resolver dudas y realizar ajustes menores.
    
    *Objetivo: Autonomía total del equipo de 'El Andalus'.*
    """)
st.divider()

# --- SECCIÓN 4: ¿POR QUÉ NOSOTROS? (PRUEBA SOCIAL) ---
st.header("3. Nuestro Equipo y Experiencia")
st.write("Contamos con más de 10 años de experiencia en la gestión, análisis e implementación de soluciones de datos. Nuestro enfoque es aplicar la tecnología de forma estratégica para generar un valor medible en el negocio.")

# Tu equipo
st.subheader("Expertos a su Servicio")
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
st.header("4. Inversión y Retorno (ROI)")

# Elemento estrella: Calculadora de ROI
st.subheader("Calculadora de ROI Interactiva")
st.write("Nuestra solución está diseñada para generar ahorros significativos. Use la calculadora a la derecha para estimar su retorno de inversión.")
col1_, col2_ = st.columns([2,3])
with col1_:
    # Inputs del usuario
    horas_por_tarea = st.slider("Horas diarias ahorradas por empleado", 0.5, 8.0, 3.0, 0.5)
    coste_por_hora = st.number_input("Costo promedio por hora de empleado ($)", min_value=1, max_value=200, value=10, step=1)

with col2_:
    num_empleados = st.slider("Número de empleados beneficiados por la automatización", 1, 5, 2)
    
    # Cálculo
    ahorro_diario = horas_por_tarea * coste_por_hora * num_empleados
    ahorro_mensual = ahorro_diario * 21.5 # Días laborables promedio en un mes
    ahorro_anual = ahorro_mensual * 12

    st.metric(label="Ahorro Anual Estimado", value=f"${ahorro_anual:,.2f}")

st.caption(f"Cálculo basado en un ahorro de {horas_por_tarea} horas diarias para {num_empleados} empleado(s) con un costo de ${coste_por_hora}/hora. "
         f"Este retorno de inversión se materializa principalmente a través de la automatización de tareas manuales.")


# Paquetes de Inversión
st.subheader("Inversión y Alcance")
st.write(f"Para El Alandalus, hemos diseñado dos rutas de implementación. Recomendamos el **Plan de Automatización Completa** para maximizar el ahorro de horas hombre.")
# Nombres más comerciales para los paquetes
pkg_bi, pkg_full, pkg_run = st.tabs([
    "Plan A: Control y Visibilidad (BI)", 
    "Plan B: Automatización Completa (BI + OCR)", 
    "Servicio de Mantenimiento y Soporte"
])

# --- PAQUETE 1: SOLO VISUALIZACIÓN ---
with pkg_bi:
    st.subheader("Plan A: Control y Visibilidad")
    st.markdown("Ideal si su prioridad inmediata es *ver* lo que pasa en el negocio, aunque sigan ingresando facturas manualmente.")
    
    col_a1, col_a2 = st.columns([2, 1])
    with col_a1:
        st.markdown("""
        **Incluye (Fases 1, 2 y 3):**
        * ✅ **Infraestructura Segura:** Instalación de VPN y configuración de acceso.
        * ✅ **Ingeniería de Datos:** Conexión y limpieza de datos del ERP.
        * ✅ **Dashboards BI:** Tableros de Ventas, Costos y Análisis de Menú.
        * ❌ **No incluye:** Módulo de escaneo de facturas (OCR).
        """)
    with col_a2:
        st.metric(label="Inversión Única", value="$1,500")
        st.caption("Tiempo de entrega: 3 Semanas")

# --- PAQUETE 2: RECOMENDADO (TODO) ---
with pkg_full:
    st.subheader("Plan B: Eficiencia y Ahorro Total")
    st.markdown("La solución completa. Elimina la ceguera operativa Y la digitación manual.")
    
    col_b1, col_b2 = st.columns([2, 1])
    with col_b1:
        st.markdown("""
        **Incluye Todo el Plan A + (Fases 4 y 5):**
        * ✅ **Todo lo incluido en el Plan A.**
        * ✅ **Módulo de IA (OCR):** Aplicación para la lectura y extracción de datos de facturas.
        * ✅ **Integración con ERP:** Inyección de datos de facturas (Proveedor, ITBMS, Totales) para validación.
        * ✅ **Capacitación:** Entrenamiento al personal administrativo.
        * ✅ **Soporte de Lanzamiento:** 1 mes de monitoreo intensivo.
        """)
    with col_b2:
        st.metric(label="Inversión Única", value="$2,500", help="Este plan ofrece el mayor retorno de inversión al automatizar tareas manuales.")
        st.caption("Tiempo de entrega: 5-6 Semanas")
        st.caption("🎯 *Ahorro estimado: 60-80 horas/mes*")

# --- MANTENIMIENTO (IMPORTANTÍSIMO PARA SAAS) ---
with pkg_run:
    st.subheader("Soporte y Evolución Continua")
    st.write("El software en la nube necesita cuidado. Este fee mensual asegura que todo siga funcionando 24/7.")
    st.markdown("""
    **El servicio mensual incluye:**
    * **Costos de Infraestructura Cloud:** Servidores y bases de datos.
    * **Monitoreo de Conectividad:** Supervisión proactiva de la VPN y los pipelines de datos.
    * **Soporte Técnico:** Resolución de incidencias y soporte al usuario.
    * **Actualizaciones Menores:** Pequeños ajustes en los dashboards según se requiera.
    """)
    st.info("**Inversión Mensual: $100 / mes** (Facturación inicia tras la entrega del proyecto)")

st.divider()

# --- VALIDACIÓN DE PRECIO (PSICOLOGÍA DE VENTAS) ---
# Esto ayuda a justificar el precio mostrando lo caro que es NO hacerlo
if st.checkbox("¿Por qué esta inversión? (Ver análisis comparativo)"):
    st.markdown(f"""
    | Concepto | Costo Actual (Manual) | Con Nuestra Solución |
    | :--- | :--- | :--- |
    | **Costo de Tareas Manuales (Anual)** | ~ $ {ahorro_anual:,.0f} | **$0** (Automatizado) |
    | **Errores Humanos** | Frecuentes (Dedo de error) | **Mínimos** (Validación IA) |
    | **Tiempo de Reportes** | Días (Cierre de mes) | **Segundos** (Tiempo Real) |
    | **Decisiones** | Basadas en intuición | **Basadas en Datos** |
    """)
st.divider()

# --- SECCIÓN 6: PRÓXIMOS PASOS (CTA) ---
st.header("5. Próximos Pasos")
st.write(f"Estamos listos para ayudar a El Alandalus a optimizar la toma de decisión apoyado por la digitalización de procesos. "
         "El siguiente paso es una reunión de 30 minutos para discutir esta propuesta y ajustar el alcance.")

col1, col2 = st.columns(2)

with col1:
    # Reemplaza esto con tu enlace real de Calendly, HubSpot, etc.
    st.link_button("Agendar Reunión de Inicio (30 min)", "https://calendly.com/tu-usuario", type="primary")

with col2:
    if st.button("Aprobar Propuesta Digitalmente"):
        # Reemplazamos los globos por un mensaje de éxito más profesional.
        st.success("Propuesta aprobada. Hemos sido notificados y nos pondremos en contacto en breve para formalizar el inicio del proyecto. ¡Gracias por su confianza!")
        # Aquí podrías agregar una lógica para enviar un email


mostrar_sidebar_footer()
