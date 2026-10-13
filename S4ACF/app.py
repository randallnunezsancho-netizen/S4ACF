import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os
import io

# ==============================================================================
# CONFIGURACIÓN DE PÁGINA Y TEMA INSTITUCIONAL UIA
# ==============================================================================
st.set_page_config(
    page_title="UIA Economía - Orientación del Crédito & Ley de Usura",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estilos CSS Profesionales: Dark Mode con Acentos Oro (#F5B700) y Azul Marino (#1E3A8A)
st.markdown(
    """
    <style>
    /* Tipografía y fondo principal */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background-color: #0b0f19;
        color: #f1f5f9;
    }
    
    /* Encabezados y títulos */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        font-weight: 700;
        letter-spacing: -0.02em;
    }
    
    /* Contenedores con estilo Glassmorphism y bordes acentuados */
    .metric-card {
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.25) 0%, rgba(15, 23, 42, 0.6) 100%);
        border: 1px solid rgba(245, 183, 0, 0.35);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }
    
    .feynman-box {
        background: linear-gradient(135deg, rgba(245, 183, 0, 0.1) 0%, rgba(15, 23, 42, 0.7) 100%);
        border-left: 5px solid #F5B700;
        border-radius: 8px;
        padding: 18px 22px;
        margin: 18px 0;
    }
    
    .socratic-box {
        background: linear-gradient(135deg, rgba(14, 165, 233, 0.1) 0%, rgba(15, 23, 42, 0.7) 100%);
        border-left: 5px solid #38bdf8;
        border-radius: 8px;
        padding: 16px 20px;
        margin: 14px 0;
    }
    
    .warning-box {
        background: rgba(239, 68, 68, 0.12);
        border-left: 5px solid #ef4444;
        border-radius: 8px;
        padding: 16px 20px;
        margin: 14px 0;
    }
    
    .success-box {
        background: rgba(34, 197, 94, 0.12);
        border-left: 5px solid #22c55e;
        border-radius: 8px;
        padding: 16px 20px;
        margin: 14px 0;
    }
    
    /* Botones primarios */
    .stButton > button {
        background: linear-gradient(90deg, #F5B700 0%, #E5A100 100%) !important;
        color: #0b0f19 !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.55rem 1.4rem !important;
        transition: all 0.25s ease-in-out !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(245, 183, 0, 0.45) !important;
    }
    
    /* Inputs y textareas */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background-color: #131d31 !important;
        color: #ffffff !important;
        border: 1px solid #2a3a5c !important;
        border-radius: 8px !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #F5B700 !important;
        box-shadow: 0 0 0 1px #F5B700 !important;
    }
    
    /* Badges de etapa */
    .stage-badge {
        display: inline-block;
        background-color: #1e3a8a;
        color: #f5b700;
        font-weight: 700;
        font-size: 0.85rem;
        padding: 4px 12px;
        border-radius: 20px;
        margin-bottom: 8px;
        border: 1px solid #f5b700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# INICIALIZACIÓN DE VARIABLES DE ESTADO (st.session_state)
# ==============================================================================
def init_session_state():
    defaults = {
        "student_name": "",
        "student_id": "",
        # Fase 1: Activación
        "p1_choice": None,
        "p1_justification": "",
        "p1_feynman": "",
        "p1_completed": False,
        # Fase 2: Demostración
        "p2_cliente_ingreso": 100000,
        "p2_cliente_gastos": 38000,
        "p2_precio_contado": 200000,
        "p2_enganche_pct": 30.0,
        "p2_plazo_meses": 12,
        "p2_gastos_depto": 1200000,
        "p2_ventas_credito": 18181818,
        "p2_tasa_interes": 12.0,
        "p2_feynman": "",
        "p2_completed": False,
        # Fase 3: Aplicación (Comité de Crédito)
        "p3_decision": None,
        "p3_enganche_propuesto": 30.0,
        "p3_garantia": "Ninguna adicional",
        "p3_justification": "",
        "p3_feynman": "",
        "p3_socratic_step": 0,
        "p3_completed": False,
        # Fase 4: Integración
        "p4_peer_feedback": "",
        "p4_feynman_oral": "",
        "p4_feynman_cierre": "",
        "p4_completed": False,
        # Ponderación y feedback
        "scores": {"activacion": 0, "demostracion": 0, "aplicacion": 0, "integracion": 0},
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

init_session_state()

# ==============================================================================
# DATOS REGULATORIOS Y PARÁMETROS REALES BCCR / CONASSIF (Costa Rica)
# ==============================================================================
# Techos semestrales oficiales de la Ley 9859 (Tasas anuales máximas BCCR):
TECHO_COLONES_REGULAR = 34.50    # Tasa Máxima de Interés para créditos convencionales en Colones
TECHO_DOLARES_REGULAR = 28.20    # Tasa Máxima para créditos en Dólares
TECHO_COLONES_MICRO = 49.30      # Tasa Máxima Microcréditos (< ₡672.000 aprox / 1.5 salarios base)
LIMITE_GASTO_FIJO_MAX = 30.0     # Regla prudencial Morales Castro: Gasto fijo <= 30% del ingreso

# ==============================================================================
# BARRA LATERAL (SIDEBAR): CONTEXTO, FUENTES & IDENTIDAD UIA
# ==============================================================================
with st.sidebar:
    # Logo UIA
    logo_path = os.path.join(os.path.dirname(__file__), "Logo-oscuro- UIA.png")
    if os.path.exists(logo_path):
        st.image(logo_path, width="stretch")
    else:
        st.markdown("<h2 style='color:#F5B700; text-align:center;'>UNIVERSIDAD INTERNACIONAL DE LAS AMÉRICAS</h2>", unsafe_allow_html=True)
    
    st.markdown("### 🏛️ Escuela de Economía")
    st.markdown("**Cátedra de Análisis de Crédito y Finanzas (ACF)**")
    st.caption("Semana 4: Orientación del Crédito, Tasas Máximas y Regulación de Usura")
    st.divider()

    # Identificación del Alumno
    st.markdown("#### 👤 Identificación del Estudiante")
    student_name = st.text_input("Nombre Completo:", value=st.session_state.student_name, placeholder="Ej. Randall Núñez")
    student_id = st.text_input("Carné Estudiantil:", value=st.session_state.student_id, placeholder="Ej. ECO-2026-001")
    if student_name != st.session_state.student_name:
        st.session_state.student_name = student_name
    if student_id != st.session_state.student_id:
        st.session_state.student_id = student_id
    
    st.divider()
    
    # Menú Lateral de Contexto Didáctico y Fuentes
    with st.expander("📚 Fuentes y Marco Regulatorio", expanded=False):
        st.markdown("""
        - **Ley N° 7472**: Promoción de la Competencia y Defensa Efectiva del Consumidor (Art. 36 bis, ter y 42).
        - **Ley N° 9859**: Ley contra la Usura Crediticia en Costa Rica.
        - **BCCR**: Techos Semestrales de Tasa de Interés Máxima y Tasa de Política Monetaria (TPM).
        - **CONASSIF / SUGEF**: Acuerdo CONASSIF 14-21 (Estimaciones crediticias prudenciales).
        - **Morales Castro**: *Crédito y Cobranza*, Cap. 5: Otorgamiento de crédito y fijación de sobreprecio.
        """)

    with st.expander("🧠 Metodología Didáctica", expanded=False):
        st.markdown("""
        **1. Principios de Merrill:**
        - **Activación**: Rescate de esquemas previos y sesgos cognitivos.
        - **Demostración**: Visualización del sistema causal (*what-happens*).
        - **Aplicación**: Toma de decisiones bajo restricciones reales con feedback socrático.
        - **Integración**: Defensa oral transferible y contraste crítico.

        **2. Método de Feynman:**
        - Explicar mecanismos complejos sin jerga matemática o bancaria vacía, utilizando analogías de la vida cotidiana.
        """)

    st.divider()
    # Monitor de Progreso en la Sesión
    prog_count = sum([
        st.session_state.p1_completed,
        st.session_state.p2_completed,
        st.session_state.p3_completed,
        st.session_state.p4_completed
    ])
    st.markdown("#### 📊 Progreso del Mastery Check")
    st.progress(prog_count / 4.0)
    st.caption(f"Fases completadas: {prog_count} de 4")

# ==============================================================================
# ENCABEZADO PRINCIPAL DE LA APLICACIÓN
# ==============================================================================
col_head1, col_head2 = st.columns([4, 1])
with col_head1:
    st.title("Laboratorio de Pensamiento Crítico: Orientación del Crédito")
    st.markdown(
        """
        *¿Cómo interactúan las políticas comerciales de los bancos comerciales con los límites legales de usura y la estabilidad macroeconómica de Costa Rica?*
        """
    )
with col_head2:
    st.markdown(
        """
        <div style="background-color:#131d31; border:1px solid #F5B700; border-radius:8px; padding:10px; text-align:center;">
            <span style="color:#F5B700; font-size:12px; font-weight:700;">CICLO 2026</span><br>
            <span style="color:#ffffff; font-size:11px;">Sesión Sincrónica</span>
        </div>
        """,
        unsafe_allow_html=True
    )

if not st.session_state.student_name:
    st.warning("⚠️ Por favor, ingresa tu **Nombre Completo** en el panel lateral para registrar tu sesión y habilitar la exportación del reporte final.")

# ==============================================================================
# NAVEGACIÓN POR PESTAÑAS (LOS 4 PRINCIPIOS DE MERRILL)
# ==============================================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. ⚡ Activación (Sondeo & Creencias)",
    "2. 🔍 Demostración (Simulador Dinámico)",
    "3. ⚖️ Aplicación (Comité de Crédito)",
    "4. 🎤 Integración (Defensa Oral Viva)",
    "5. 📄 Resumen & Exportación"
])

# ==============================================================================
# PESTAÑA 1: FASE DE ACTIVACIÓN
# ==============================================================================
with tab1:
    st.markdown('<span class="stage-badge">FASE 1: ACTIVACIÓN COGNITIVA</span>', unsafe_allow_html=True)
    st.subheader("Sondeo de Creencias y Preguntas Detonantes")
    
    st.markdown(
        """
        Antes de abrir balances bancarios o consultar fórmulas de crédito, examinemos nuestra intuición sobre la regulación financiera.
        En debates parlamentarios y en la opinión pública a menudo se asume una relación directa y simple entre la ley y el bienestar social.
        """
    )

    st.markdown(
        """
        <div class="metric-card">
            <h4 style="color:#F5B700; margin-top:0;">❓ Dilema de Partida:</h4>
            <p style="font-size:1.05rem;">
                <strong>"¿Establecer un tope máximo legal a las tasas de interés (Ley de Usura) garantiza automáticamente que las personas de menores ingresos paguen menos intereses y gocen de mayor bienestar?"</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    p1_options = [
        "Sí, porque la ley frena la avaricia del prestamista y abarata el crédito para toda la población sin distinciones.",
        "No necesariamente; al fijar un tope por debajo del costo real de administrar préstamos pequeños y riesgosos, las entidades formales optan por expulsar a estos clientes del sistema.",
        "Es indiferente; las personas de bajos ingresos no acuden a instituciones financieras en ningún país del mundo."
    ]
    
    selected_idx = None
    if st.session_state.p1_choice in p1_options:
        selected_idx = p1_options.index(st.session_state.p1_choice)
    
    p1_radio = st.radio(
        "Selecciona la postura que mejor refleje tu hipótesis inicial como futuro(a) economista:",
        p1_options,
        index=selected_idx if selected_idx is not None else 0
    )
    st.session_state.p1_choice = p1_radio

    st.markdown("#### 💬 Justificación Económica Inicial")
    st.caption("Argumenta tu respuesta: ¿Qué incentivos cambian en la institución bancaria y en el deudor ante este tipo de regulación de precios?")
    p1_just = st.text_area(
        "Tu justificación (mínimo 50 palabras):",
        value=st.session_state.p1_justification,
        height=100,
        placeholder="Considera los costos de administración fijos, el riesgo de morosidad y qué alternativas le quedan al cliente si el banco le niega el crédito..."
    )
    st.session_state.p1_justification = p1_just

    # Ejercicio Feynman de Fase 1
    st.markdown(
        """
        <div class="feynman-box">
            <h4 style="color:#F5B700; margin-top:0;">🧠 Reto del Método de Feynman:</h4>
            <p>
                <em>"Explícale a un amigo que no estudia economía por qué la gente recurre a prestamistas informales 'gota a gota' cuando un banco reduce artificialmente las tasas de interés o endurece sus requisitos de aprobación, usando un ejemplo cotidiano (como un puesto de frutas en la feria del agricultor)."</em>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    p1_fey = st.text_area(
        "Tu analogía cotidiana (Método Feynman):",
        value=st.session_state.p1_feynman,
        height=110,
        placeholder="Piensa en una verdulería obligada a vender tomates a pérdida o con requisitos de factura electrónica a clientes que solo tienen monedas..."
    )
    st.session_state.p1_feynman = p1_fey

    # Retroalimentación Formativa sin dar la respuesta masticada
    if st.button("Validar Razonamiento de Activación", key="btn_p1"):
        word_count_just = len(p1_just.strip().split())
        word_count_fey = len(p1_fey.strip().split())

        if word_count_just < 20 or word_count_fey < 20:
            st.error("⚠️ Tu argumentación es demasiado breve. Desarrolla tus ideas con mayor profundidad antes de continuar.")
        else:
            st.session_state.p1_completed = True
            st.session_state.scores["activacion"] = 25
            
            if "No necesariamente" in p1_radio:
                st.markdown(
                    """
                    <div class="success-box">
                        <strong>✅ Excelente conexión de incentivos:</strong> Has identificado el mecanismo de <em>racionamiento del crédito</em> y exclusión financiera.
                        Cuando el precio legal no cubre el costo de fondeo + costo operativo + prima de riesgo, la oferta formal se contrae.
                        En la siguiente fase demostraremos matemáticamente cómo se forma esa brecha.
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    """
                    <div class="warning-box">
                        <strong>🤔 Pista socrática para contrastar tu perspectiva:</strong>
                        Pregúntate: si el banco tiene costos fijos ineludibles por investigar y cobrar un microcrédito de ₡100.000, ¿qué pasa cuando la ley le prohíbe cobrar lo suficiente para cubrir esos costos de papelería, analistas y riesgo?
                        ¿Prestará con gusto asumiendo pérdidas contables continuas, o cerrará la ventanilla a ese perfil?
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# ==============================================================================
# PESTAÑA 2: FASE DE DEMOSTRACIÓN
# ==============================================================================
with tab2:
    st.markdown('<span class="stage-badge">FASE 2: DEMOSTRACIÓN VISUAL Y CAUSAL</span>', unsafe_allow_html=True)
    st.subheader("Desglose Causal: Estados Financieros, Sobreprecio y Límites de Usura")
    
    st.markdown(
        """
        En esta etapa desmontamos el sistema operativo del crédito según el marco de **Morales Castro (Capítulo 5)** 
        y lo contrastamos con las restricciones de la **Ley N° 9859 (BCCR)** y el **Acuerdo CONASSIF 14-21**.
        """
    )

    col_demo_input, col_demo_viz = st.columns([1, 1.2])

    with col_demo_input:
        st.markdown("#### ⚙️ Parámetros del Solicitante y de la Entidad")
        
        c_ing = st.number_input(
            "Ingresos Mensuales del Cliente (₡):",
            min_value=50000, max_value=2000000, value=st.session_state.p2_cliente_ingreso, step=10000
        )
        st.session_state.p2_cliente_ingreso = c_ing

        c_gas = st.number_input(
            "Gastos Fijos Previos del Cliente (₡):",
            min_value=0, max_value=2000000, value=st.session_state.p2_cliente_gastos, step=5000
        )
        st.session_state.p2_cliente_gastos = c_gas

        c_precio = st.number_input(
            "Monto de la Compra / Solicitud de Contado (₡):",
            min_value=50000, max_value=10000000, value=st.session_state.p2_precio_contado, step=25000
        )
        st.session_state.p2_precio_contado = c_precio

        c_eng = st.slider(
            "Porcentaje de Enganche / Pago Inicial (%):",
            min_value=0.0, max_value=70.0, value=float(st.session_state.p2_enganche_pct), step=5.0
        )
        st.session_state.p2_enganche_pct = c_eng

        c_plazo = st.selectbox(
            "Plazo del Financiamiento (Meses):",
            [6, 12, 18, 24, 36],
            index=1
        )
        st.session_state.p2_plazo_meses = c_plazo

        with st.expander("🛠️ Estructura Interna del Banco (Fórmula Morales Castro)", expanded=False):
            g_depto = st.number_input("Gastos Anuales Depto. Crédito y Cobranza (₡):", value=1200000, step=100000)
            v_anual = st.number_input("Ventas Anuales a Crédito de la Empresa (₡):", value=18181818, step=500000)
            t_interes = st.slider("Tasa de Interés Financiera Anual base (%):", 0.0, 30.0, 12.0, 0.5)

    # CÁLCULOS MATEMÁTICOS DE MORALES CASTRO
    pago_inicial = c_precio * (c_eng / 100.0)
    saldo_insoluto = c_precio - pago_inicial
    
    # Sobreprecio = (Gastos del Departamento / Ventas Anuales a Crédito) + Tasa de Interés
    tasa_gastos_operativos = (g_depto / v_anual) * 100.0  # 6.6% en el ejemplo de Morales Castro
    sobreprecio_total_pct = tasa_gastos_operativos + t_interes  # ~18.6%
    
    # Monto cargado por sobreprecio
    recargo_sobreprecio = saldo_insoluto * (sobreprecio_total_pct / 100.0) * (c_plazo / 12.0)
    deuda_total_a_plazo = saldo_insoluto + recargo_sobreprecio
    cuota_mensual = deuda_total_a_plazo / c_plazo if c_plazo > 0 else 0
    
    # Análisis de Capacidad Cuantitativa:
    # Proporción de Gastos Fijos = (Gastos Previos + Nueva Cuota) / Ingresos
    gasto_total_con_credito = c_gas + cuota_mensual
    prop_gasto_fijo_pct = (gasto_total_con_credito / c_ing) * 100.0 if c_ing > 0 else 0
    prop_gasto_previo_pct = (c_gas / c_ing) * 100.0 if c_ing > 0 else 0

    with col_demo_viz:
        st.markdown("#### 📊 Diagnóstico en Tiempo Real")
        
        # Métrica 1: Capacidad de Pago vs Límite del 30%
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric(
                label="Ratio de Gastos Fijos Total",
                value=f"{prop_gasto_fijo_pct:.1f}%",
                delta=f"{prop_gasto_fijo_pct - LIMITE_GASTO_FIJO_MAX:.1f}% vs Umbral 30%",
                delta_color="inverse"
            )
        with col_m2:
            st.metric(
                label="Sobreprecio Total Anual",
                value=f"{sobreprecio_total_pct:.2f}%",
                delta=f"{TECHO_COLONES_REGULAR - sobreprecio_total_pct:.2f}% bajo Techo BCCR",
                delta_color="normal"
            )

        # Gráfico de barras de Capacidad de Pago
        df_cap = pd.DataFrame({
            "Rubro": ["Gastos Previos", "Nueva Cuota Mensual", "Ingreso Remanente"],
            "Monto (₡)": [c_gas, cuota_mensual, max(0, c_ing - gasto_total_con_credito)],
            "Color": ["#ef4444", "#F5B700", "#10b981"]
        })
        fig_cap = px.bar(
            df_cap, x="Rubro", y="Monto (₡)", color="Rubro",
            color_discrete_map={"Gastos Previos": "#ef4444", "Nueva Cuota Mensual": "#F5B700", "Ingreso Remanente": "#10b981"},
            title=f"Distribución del Ingreso Mensual del Deudor (₡{c_ing:,.0f})"
        )
        fig_cap.add_hline(y=c_ing * 0.30, line_dash="dash", line_color="#F5B700", annotation_text="Tope Prudencial 30%")
        fig_cap.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(19, 29, 49, 0.7)",
            font_color="#ffffff",
            showlegend=False,
            height=280,
            margin=dict(l=10, r=10, t=40, b=10)
        )
        st.plotly_chart(fig_cap, width="stretch")

        # Evaluación inmediata
        if prop_gasto_fijo_pct > LIMITE_GASTO_FIJO_MAX:
            st.markdown(
                f"""
                <div class="warning-box">
                    <strong>⚠️ Alerta de Capacidad de Pago (Morales Castro):</strong><br>
                    El cliente destina el <strong>{prop_gasto_fijo_pct:.1f}%</strong> de sus ingresos a gastos fijos y servicio de deudas, superando el límite máximo prudencial del <strong>30%</strong>.<br>
                    <em>Bajo criterios estándar del banco, esta operación debe ser rechazada o reestructurada (ej. exigiendo mayor enganche o alargando plazos).</em>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="success-box">
                    <strong>✅ Cumple Capacidad Cuantitativa:</strong><br>
                    Los gastos fijos representan el <strong>{prop_gasto_fijo_pct:.1f}%</strong> del ingreso, dentro del margen seguro (&le; 30%).
                </div>
                """,
                unsafe_allow_html=True
            )

    st.divider()

    # Ejercicio Feynman de Demostración
    st.markdown(
        """
        <div class="feynman-box">
            <h4 style="color:#F5B700; margin-top:0;">🧠 Reto del Método de Feynman:</h4>
            <p>
                <em>"Imagínate que eres un tutor en una mesa redonda de estudio. Explícale paso a paso a un compañero de primer año cuál es la diferencia exacta entre evaluar la capacidad de pago cualitativa (carácter y condiciones del negocio) y la cuantitativa (flujo de caja), asegurándote de no usar tecnicismos bancarios complejos."</em>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    p2_fey = st.text_area(
        "Tu explicación pedagógica sin tecnicismos:",
        value=st.session_state.p2_feynman,
        height=110,
        placeholder="Piensa en cómo le prestarías dinero a un amigo: una cosa es saber si gana suficiente salario (números), y otra muy distinta si acostumbra pagar a tiempo o si tiene malos hábitos (carácter)..."
    )
    st.session_state.p2_feynman = p2_fey

    if st.button("Confirmar Comprensión de la Demostración", key="btn_p2"):
        if len(p2_fey.strip().split()) < 20:
            st.error("⚠️ Tu respuesta debe tener al menos 20 palabras explicando la diferencia cualitativa vs cuantitativa.")
        else:
            st.session_state.p2_completed = True
            st.session_state.scores["demostracion"] = 25
            st.success("Demostración completada con éxito. Procede a la pestaña de Aplicación.")

# ==============================================================================
# PESTAÑA 3: FASE DE APLICACIÓN
# ==============================================================================
with tab3:
    st.markdown('<span class="stage-badge">FASE 3: APLICACIÓN PRÁCTICA</span>', unsafe_allow_html=True)
    st.subheader("Comité de Crédito Simulado & Prueba de Estrés Regulatorio")

    st.markdown(
        """
        **Rol Asignado:** Eres miembro titular del Comité de Crédito de un banco comercial costarricense.
        Debes emitir un dictamen vinculante sobre el expediente recibido y justificar tu decisión frente a la normativa vigente.
        """
    )

    # Presentación del Caso Práctico
    st.markdown(
        """
        <div class="metric-card">
            <h4 style="color:#F5B700; margin-top:0;">📁 Expediente de Solicitud N° 2026-CR-084</h4>
            <ul>
                <li><strong>Solicitante:</strong> Persona física con salario mensual formal de ₡100.000.</li>
                <li><strong>Gastos fijos existentes:</strong> ₡38.000 mensuales en otros compromisos (38% de sus ingresos, ya supera el 30% prudencial).</li>
                <li><strong>Monto del artículo solicitado:</strong> ₡200.000.</li>
                <li><strong>Garantía ofrecida:</strong> Ofrece un terreno rústico valorado en ₡3.000.000 (Colateral excepcional con cobertura de 15 a 1).</li>
                <li><strong>Propuesta comercial de ventas:</strong> Financiamiento a 12 meses con sobreprecio de 18.66% anual y un enganche sugerido inicial de 30% (₡60.000).</li>
                <li><strong>Normativa aplicable:</strong> Ley 7472, Ley de Usura 9859 (Techo BCCR: 34.50%) y Acuerdo CONASSIF 14-21 (provisiones por deudor con debilidad de pago).</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_dec1, col_dec2 = st.columns([1, 1])

    with col_dec1:
        st.markdown("#### 🗳️ Decisión del Comité")
        decision_options = [
            "Aprobar el crédito sin cambios: El colateral de ₡3.000.000 protege plenamente al banco frente a cualquier impago.",
            "Rechazar el crédito: El cliente ya destina el 38% a gastos fijos y la cuota lo sobreendeudaría gravemente.",
            "Aprobación condicionada a reestructuración: Exigir mayor enganche (ej. 50%+) o garantía adicional de pago inmediato para bajar la cuota a un nivel tolerable."
        ]
        p3_dec = st.radio(
            "¿Cuál es tu voto como analista de riesgo?",
            decision_options,
            index=0 if st.session_state.p3_decision is None else decision_options.index(st.session_state.p3_decision) if st.session_state.p3_decision in decision_options else 0
        )
        st.session_state.p3_decision = p3_dec

    with col_dec2:
        st.markdown("#### 🔧 Ajustes Propuestos (Si aplica)")
        p3_eng = st.slider("Nuevo Enganche Exigido (%)", 20.0, 80.0, float(st.session_state.p3_enganche_propuesto), step=5.0)
        st.session_state.p3_enganche_propuesto = p3_eng
        
        # Cálculo de la cuota ajustada
        pago_ini_ajustado = 200000 * (p3_eng / 100.0)
        saldo_ajustado = 200000 - pago_ini_ajustado
        sobreprecio_ajustado = saldo_ajustado * 0.1866
        nueva_cuota_ajustada = (saldo_ajustado + sobreprecio_ajustado) / 12.0
        nuevo_gasto_total = 38000 + nueva_cuota_ajustada
        nuevo_ratio_gasto = (nuevo_gasto_total / 100000.0) * 100.0
        
        st.info(f"Con enganche de {p3_eng:.0f}%: Cuota = ₡{nueva_cuota_ajustada:,.0f}/mes. Ratio final de compromisos = {nuevo_ratio_gasto:.1f}%.")

    st.markdown("#### 📝 Justificación Técnica y Regulatoria de tu Voto")
    p3_just = st.text_area(
        "Expón los fundamentos económicos y prudenciales de tu dictamen (mínimo 50 palabras):",
        value=st.session_state.p3_justification,
        height=110,
        placeholder="Aborda: ¿Puede el colateral reemplazar la capacidad de pago del flujo de caja? ¿Qué dice CONASSIF 14-21 sobre ejecutar garantías versus solvencia continua? ¿Incurre el banco en costos de estimación preventiva?"
    )
    st.session_state.p3_justification = p3_just

    # Ejercicio Feynman de Fase 3
    st.markdown(
        """
        <div class="feynman-box">
            <h4 style="color:#F5B700; margin-top:0;">🧠 Reto del Método de Feynman:</h4>
            <p>
                <em>"Escribe una narrativa corta de 5 líneas donde le expliques a la junta directiva de un banco por qué la solicitud de un cliente con un excelente colateral (garantía real) pero con un flujo de caja inestable debe ser rechazada bajo los criterios de supervisión prudencial."</em>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    p3_fey = st.text_area(
        "Tu narrativa para la Junta Directiva (Método Feynman):",
        value=st.session_state.p3_feynman,
        height=110,
        placeholder="Señores directores: Un banco no es una empresa de bienes raíces ni una casa de empeño. Cobrar rematando un terreno cuesta años de juicios y no paga los sueldos a fin de mes..."
    )
    st.session_state.p3_feynman = p3_fey

    # Motor Socrático de Validación
    if st.button("Someter Decisión al Comité Evaluador Socrático", key="btn_p3"):
        w_just = len(p3_just.strip().split())
        w_fey = len(p3_fey.strip().split())

        if w_just < 20 or w_fey < 20:
            st.error("⚠️ La justificación y el ejercicio Feynman requieren al menos 20 palabras cada uno.")
        else:
            st.session_state.p3_completed = True
            st.session_state.scores["aplicacion"] = 25

            if "Aprobar el crédito sin cambios" in p3_dec:
                st.markdown(
                    """
                    <div class="warning-box">
                        <strong>⚠️ Intervención Socrática del Supervisor:</strong><br>
                        ¡Cuidado con la trampa del colateral! Bajo el <strong>Acuerdo CONASSIF 14-21</strong> y las buenas prácticas prudenciales, 
                        <strong>el crédito se paga con flujos futuros de efectivo, no con la liquidación forzosa de garantías</strong>. 
                        Ejecutar un terreno rústico toma entre 2 y 5 años de litigio judicial, genera costos de mantenimiento y obliga al banco a constituir estimaciones contracíclicas inmediatas que castigan el capital institucional.
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif "Rechazar el crédito" in p3_dec:
                st.markdown(
                    """
                    <div class="success-box">
                        <strong>✅ Postura Prudencial Ortodoxa:</strong><br>
                        Has priorizado la regla básica de Morales Castro y CONASSIF: el cliente ya exhibe un 38% de endeudamiento inicial, 
                        por lo que añadir más deuda agrava su insolvencia. Sin embargo, reflexiona: ¿es posible salvar la operación bancaria 
                        si el cliente liquida por su cuenta parte de sus activos o aporta un enganche del 60%+?
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    """
                    <div class="success-box">
                        <strong>✅ Visión de Estructuración y Gestión Activa de Riesgo:</strong><br>
                        Identificaste que el problema no es el colateral, sino el servicio mensual de la deuda. Al exigir mayor enganche 
                        se amortigua el saldo insoluto a un monto cuya cuota no ahogue el flujo de caja del deudor.
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# ==============================================================================
# PESTAÑA 4: FASE DE INTEGRACIÓN
# ==============================================================================
with tab4:
    st.markdown('<span class="stage-badge">FASE 4: INTEGRACIÓN Y TRANSFERENCIA</span>', unsafe_allow_html=True)
    st.subheader("Foro de Crítica Cruzada y Defensa Oral Viva (Mastery Check)")

    st.markdown(
        """
        En esta etapa final, consolidas tus conocimientos preparándote para la **defensa oral sincrónica de 2 minutos** 
        frente al profesor y compañeros de clase, evaluando además una perspectiva contraria.
        """
    )

    # Debate de Posturas Contrapuestas
    st.markdown(
        """
        <div class="metric-card">
            <h4 style="color:#F5B700; margin-top:0;">👥 Foro de Crítica Cruzada: Postura de tu Colega</h4>
            <p>
                <strong>Tesis presentada por un compañero de clase:</strong><br>
                <em>"El Banco Central debería fijar una tasa máxima del 10% anual para todos los créditos sin excepción. 
                De esta forma, ningún costarricense pagará intereses elevados y se erradicará la pobreza financiera de golpe."</em>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    p4_critica = st.text_area(
        "Refuta o matiza la postura de tu colega utilizando los conceptos de sobreprecio de Morales Castro y la Ley 9859:",
        value=st.session_state.p4_peer_feedback,
        height=100,
        placeholder="Explica qué sucedería con los gastos operativos del banco si la tasa se fija al 10%, y qué opciones le quedarían a quienes piden montos pequeños..."
    )
    st.session_state.p4_peer_feedback = p4_critica

    # Ejercicio Feynman de Defensa Oral
    st.markdown(
        """
        <div class="feynman-box">
            <h4 style="color:#F5B700; margin-top:0;">🧠 Reto del Método de Feynman (Defensa Oral de 2 Minutos - Mastery Viva):</h4>
            <p>
                <em>"Prepara tu defensa oral de 2 minutos para explicarnos: ¿Cómo se relacionan las tasas máximas de interés del BCCR con la estabilidad del sistema financiero y por qué un error en la evaluación del riesgo de crédito destruye el patrimonio de una entidad? Explícalo como si se lo contaras a un familiar en la mesa de tu casa."</em>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    p4_oral = st.text_area(
        "Guion de tu Defensa Oral (2 minutos):",
        value=st.session_state.p4_feynman_oral,
        height=120,
        placeholder="Hola mamá/papá: Imagínate que el banco presta el dinero que los ahorrantes le confiaron. Si prestamos a personas que no pueden pagar solo porque prometen un interés altísimo..."
    )
    st.session_state.p4_feynman_oral = p4_oral

    # Pregunta Estratégica de Cierre
    st.markdown(
        """
        <div class="socratic-box">
            <h4 style="color:#38bdf8; margin-top:0;">💡 Pregunta Estratégica de Cierre (Síntesis Macro-Micro):</h4>
            <p>
                <em>"Si el Banco Central de Costa Rica (BCCR) decide elevar la Tasa de Política Monetaria (TPM) para contener la inflación, provocando que la tasa activa ponderada del mercado aumente un 3%, pero los gastos operativos del departamento de crédito de un banco se mantienen constantes, ¿cómo se reconfigura la frontera de exclusión crediticia para un deudor cuyo límite de gasto fijo roza el 30% bajo el tope legal fijado por la Ley N° 9859?"</em>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    p4_cierre = st.text_area(
        "Tu análisis de cierre:",
        value=st.session_state.p4_feynman_cierre,
        height=110,
        placeholder="Al subir la TPM, el costo del dinero se eleva. Para el cliente que ya está al 30%..."
    )
    st.session_state.p4_feynman_cierre = p4_cierre

    if st.button("Finalizar Integración y Consolidar Sesión", key="btn_p4"):
        w_crit = len(p4_critica.strip().split())
        w_oral = len(p4_oral.strip().split())
        w_cierre = len(p4_cierre.strip().split())

        if w_crit < 15 or w_oral < 20 or w_cierre < 15:
            st.error("⚠️ Por favor completa los 3 campos de reflexión con argumentos sustantivos antes de finalizar.")
        else:
            st.session_state.p4_completed = True
            st.session_state.scores["integracion"] = 25
            st.success("🎉 ¡Excelente trabajo! Has completado el ciclo pedagógico completo. Ve a la pestaña 'Resumen & Exportación' para descargar tu informe.")

# ==============================================================================
# PESTAÑA 5: RESUMEN Y EXPORTACIÓN DEL REPORTE FINAL
# ==============================================================================
with tab5:
    st.markdown('<span class="stage-badge">RESUMEN CONSOLIDADO DE LA SESIÓN</span>', unsafe_allow_html=True)
    st.subheader("Informe de Desempeño y Portafolio de Pensamiento Crítico")

    total_score = sum(st.session_state.scores.values())

    col_res1, col_res2, col_res3, col_res4 = st.columns(4)
    with col_res1:
        st.metric("1. Activación", f"{st.session_state.scores['activacion']}/25 pts")
    with col_res2:
        st.metric("2. Demostración", f"{st.session_state.scores['demostracion']}/25 pts")
    with col_res3:
        st.metric("3. Aplicación", f"{st.session_state.scores['aplicacion']}/25 pts")
    with col_res4:
        st.metric("4. Integración", f"{st.session_state.scores['integracion']}/25 pts")

    st.markdown(f"### Calificación Consolidada: **{total_score} / 100 puntos**")
    
    # Barra de progreso visual
    st.progress(total_score / 100.0)

    # Vista previa del reporte en formato Markdown
    reporte_md = f"""# REPORTE DE SESIÓN: PENSAMIENTO CRÍTICO EN ORIENTACIÓN DEL CRÉDITO
**Universidad Internacional de las Américas (U.I.A.)**
**Cátedra de Análisis de Crédito y Finanzas (ACF) - Semana 4**

---
### 👤 DATOS DEL ESTUDIANTE
- **Nombre:** {st.session_state.student_name if st.session_state.student_name else "No indicado"}
- **Carné:** {st.session_state.student_id if st.session_state.student_id else "No indicado"}
- **Calificación Consolidada:** {total_score} / 100 pts
- **Fecha de Registro:** Ciclo 2026 - Sesión Sincrónica

---
### 1. FASE DE ACTIVACIÓN COGNITIVA (Merrill & Feynman)
- **Hipótesis Seleccionada:** {st.session_state.p1_choice}
- **Justificación Económica:**
> {st.session_state.p1_justification}
- **Analogía Cotidiana (Método Feynman - Mercado de Frutas / Gota a Gota):**
> {st.session_state.p1_feynman}

---
### 2. FASE DE DEMOSTRACIÓN (Morales Castro & Regulación BCCR)
- **Parámetros Evaluados:**
  - Ingreso del Deudor: ₡{st.session_state.p2_cliente_ingreso:,.0f}
  - Gastos Fijos Previos: ₡{st.session_state.p2_cliente_gastos:,.0f} ({(st.session_state.p2_cliente_gastos / st.session_state.p2_cliente_ingreso)*100:.1f}%)
  - Monto del Financiamiento: ₡{st.session_state.p2_precio_contado:,.0f}
  - Enganche Evaluado: {st.session_state.p2_enganche_pct:.0f}%
- **Explicación Feynman (Cualitativo vs Cuantitativo sin tecnicismos):**
> {st.session_state.p2_feynman}

---
### 3. FASE DE APLICACIÓN (Comité de Crédito & Supervisión Prudencial)
- **Voto del Estudiante en el Comité:** {st.session_state.p3_decision}
- **Enganche Propuesto:** {st.session_state.p3_enganche_propuesto:.0f}%
- **Justificación Técnica y Regulatoria (CONASSIF 14-21 / Colateral vs Flujo):**
> {st.session_state.p3_justification}
- **Narrativa para la Junta Directiva (Método Feynman):**
> {st.session_state.p3_feynman}

---
### 4. FASE DE INTEGRACIÓN (Defensa Oral & Contraste de Políticas)
- **Crítica Cruzada a Tesis de Topes Artificiales:**
> {st.session_state.p4_peer_feedback}
- **Guion de Defensa Oral de 2 Minutos (Mastery Viva):**
> {st.session_state.p4_feynman_oral}
- **Síntesis Estratégica de Cierre (Efecto TPM BCCR vs Ley 9859):**
> {st.session_state.p4_feynman_cierre}

---
### 🏁 DICTAMEN FORMATIVO DEL TUTOR INTELIGENTE
- **Rigor Conceptual:** Demuestra dominio en la separación entre garantías reales y capacidad efectiva de servicio de la deuda.
- **Competencia Crítica:** Comprende las consecuencias no deseadas de los techos a tasas de interés en la exclusión financiera informal.
"""

    with st.expander("👁️ Vista Previa del Reporte Consolidado", expanded=True):
        st.markdown(reporte_md)

    st.markdown("#### 📥 Descarga de Evidencia para el Portafolio")
    st.download_button(
        label="📥 Descargar Reporte Consolidado (.md)",
        data=reporte_md,
        file_name=f"Reporte_ACF_Semana4_{st.session_state.student_name.replace(' ', '_') if st.session_state.student_name else 'Estudiante'}.md",
        mime="text/markdown"
    )
