# -*- coding: utf-8 -*-
"""
========================================================================================
UNIVERSIDAD INTERNACIONAL DE LAS AMÉRICAS (U.I.A.)
Escuela de Economía - Curso de Análisis de Crédito y Finanzas (ACF) - Semana 3
Aplicación Educativa de Pensamiento Crítico: Crédito, Cobranza y Supervisión Basada en Riesgos
Fuentes: Morales Castro (Las 5 C del Crédito) & Acuerdo SUGEF 24-22 (Metodología GREAC)
========================================================================================
"""

import streamlit as st
import datetime
import json

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="U.I.A. Economía | Pensamiento Crítico en Riesgo Crediticio",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# ESTILOS CSS PERSONALIZADOS (Diseño moderno, tipografía limpia, tarjetas y badges)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3, h4, .main-title {
        font-family: 'Outfit', sans-serif;
        letter-spacing: -0.02em;
    }
    
    .main-header {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #0F766E 100%);
        color: white;
        padding: 1.8rem 2.2rem;
        border-radius: 16px;
        margin-bottom: 1.8rem;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.1rem;
        font-weight: 700;
        color: #F8FAFC;
    }
    
    .main-header p {
        margin: 0.4rem 0 0 0;
        font-size: 1.0rem;
        color: #94A3B8;
    }
    
    .badge-uia {
        display: inline-block;
        background-color: #0284C7;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
    }

    .badge-sugef {
        display: inline-block;
        background-color: #0D9488;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 0.4rem;
    }

    .badge-morales {
        display: inline-block;
        background-color: #6366F1;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
    }

    .card {
        background: #1E293B !important;
        border: 1px solid #334155 !important;
        border-radius: 14px !important;
        padding: 1.6rem !important;
        margin-bottom: 1.4rem !important;
        box-shadow: 0 4px 15px -2px rgba(0, 0, 0, 0.4) !important;
        color: #F8FAFC !important;
    }
    .card h1, .card h2, .card h3 {
        color: #38BDF8 !important;
    }
    .card h4 {
        color: #E2E8F0 !important;
    }
    .card p, .card span, .card li, .card ol, .card ul, .card div {
        color: #CBD5E1 !important;
        line-height: 1.6 !important;
    }
    .card strong {
        color: #F8FAFC !important;
    }
    
    .card-dark {
        background: #0B1329 !important;
        border: 1px solid #334155 !important;
        border-radius: 14px !important;
        padding: 1.6rem !important;
        color: #F1F5F9 !important;
        margin-bottom: 1.4rem !important;
    }
    .card-dark h1, .card-dark h2, .card-dark h3 {
        color: #38BDF8 !important;
    }
    .card-dark p, .card-dark span, .card-dark strong {
        color: #F1F5F9 !important;
    }
    
    .card-accent {
        background: #022C22 !important;
        border: 1px solid #10B981 !important;
        border-left: 6px solid #10B981 !important;
        border-radius: 12px !important;
        padding: 1.4rem !important;
        margin: 1.2rem 0 !important;
    }
    .card-accent h1, .card-accent h2, .card-accent h3, .card-accent h4 {
        color: #6EE7B7 !important;
        margin-top: 0 !important;
    }
    .card-accent p, .card-accent span, .card-accent div, .card-accent strong, .card-accent em {
        color: #ECFDF5 !important;
        font-size: 1.05rem !important;
        line-height: 1.5 !important;
    }

    .card-warning {
        background: #2A1705 !important;
        border: 2px solid #F59E0B !important;
        border-left: 8px solid #F59E0B !important;
        border-radius: 12px !important;
        padding: 1.4rem 1.6rem !important;
        margin: 1.2rem 0 !important;
        box-shadow: 0 4px 15px -2px rgba(245, 158, 11, 0.25) !important;
    }
    .card-warning h1, .card-warning h2, .card-warning h3, .card-warning h4 {
        color: #FCD34D !important;
        margin-top: 0 !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
    }
    .card-warning p, .card-warning span, .card-warning div, .card-warning strong, .card-warning em {
        color: #FFFBEB !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        line-height: 1.65 !important;
    }

    .card-danger {
        background: #450A0A !important;
        border: 1px solid #EF4444 !important;
        border-left: 6px solid #EF4444 !important;
        border-radius: 12px !important;
        padding: 1.4rem !important;
        margin: 1.2rem 0 !important;
    }
    .card-danger h1, .card-danger h2, .card-danger h3, .card-danger h4 {
        color: #FCA5A5 !important;
        margin-top: 0 !important;
    }
    .card-danger p, .card-danger span, .card-danger div, .card-danger strong, .card-danger em {
        color: #FEF2F2 !important;
        font-size: 1.05rem !important;
        line-height: 1.5 !important;
    }

    .metric-chip {
        display: inline-block;
        background: #1E293B !important;
        color: #38BDF8 !important;
        border: 1px solid #0284C7 !important;
        border-radius: 8px !important;
        padding: 0.6rem 1rem !important;
        margin: 0.3rem !important;
        font-weight: 600 !important;
    }

    .metric-chip {
        display: inline-block;
        background: #F1F5F9;
        border: 1px solid #CBD5E1;
        border-radius: 8px;
        padding: 0.6rem 1rem;
        margin: 0.3rem;
        font-weight: 600;
    }

    .analogy-box {
        background: linear-gradient(135deg, #1E1B4B 0%, #312E81 100%);
        color: #E0E7FF;
        border-radius: 14px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid #4338CA;
    }

    .rubric-tag {
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        padding: 0.2rem 0.6rem;
        border-radius: 6px;
    }
    .rubric-excelente { background: #DCFCE7; color: #15803D; }
    .rubric-en-proceso { background: #FEF9C3; color: #854D0E; }
    .rubric-insuficiente { background: #FEE2E2; color: #991B1B; }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# INICIALIZACIÓN DE SESSION_STATE (Persistencia acumulativa de respuestas y sesión)
# -----------------------------------------------------------------------------
if "student_name" not in st.session_state:
    st.session_state.student_name = ""
if "student_id" not in st.session_state:
    st.session_state.student_id = ""
if "student_group" not in st.session_state:
    st.session_state.student_group = "Economía - Grupo 1 (Sincrónica)"

# Respuestas de Módulo 1: Rompe Hielo y Término Trampa
if "trampa_answer" not in st.session_state:
    st.session_state.trampa_answer = None
if "trampa_justification" not in st.session_state:
    st.session_state.trampa_justification = ""
if "trampa_feedback" not in st.session_state:
    st.session_state.trampa_feedback = None

# Respuestas de Módulo 3: Case Study Questions
if "case_q1" not in st.session_state:
    st.session_state.case_q1 = ""
if "case_q2" not in st.session_state:
    st.session_state.case_q2 = ""
if "case_q3" not in st.session_state:
    st.session_state.case_q3 = ""
if "case_feedback" not in st.session_state:
    st.session_state.case_feedback = None

# Respuestas de Módulo 4: Simulación de Comité / Decisiones
if "sim_role" not in st.session_state:
    st.session_state.sim_role = "Oficial Inspector SUGEF"
if "sim_tpm_delta" not in st.session_state:
    st.session_state.sim_tpm_delta = 2.5
if "sim_fx_deprec" not in st.session_state:
    st.session_state.sim_fx_deprec = 12.0
if "sim_policy_choice" not in st.session_state:
    st.session_state.sim_policy_choice = "Exigir saneamiento preventivo y constituir provisiones contracíclicas"
if "sim_argument" not in st.session_state:
    st.session_state.sim_argument = ""
if "sim_feedback" not in st.session_state:
    st.session_state.sim_feedback = None

# Respuestas de Módulo 5: Método Feynman y Pregunta Estratégica
if "feynman_explanation" not in st.session_state:
    st.session_state.feynman_explanation = ""
if "strategic_answer" not in st.session_state:
    st.session_state.strategic_answer = ""
if "final_score" not in st.session_state:
    st.session_state.final_score = 0
if "final_rubric" not in st.session_state:
    st.session_state.final_rubric = {}

# -----------------------------------------------------------------------------
# BARRA LATERAL (Sidebar de Contexto y Gestión del Estudiante)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown('<div class="badge-uia">U.I.A. • Escuela de Economía</div>', unsafe_allow_html=True)
    st.title("🏛️ Sesión Sincrónica S3")
    st.markdown("**Crédito, Cobranza y Supervisión Basada en Riesgos**")
    
    st.markdown("---")
    st.subheader("👤 Ficha del Estudiante")
    st.session_state.student_name = st.text_input(
        "Nombre completo:",
        value=st.session_state.student_name,
        placeholder="Ej. Sofía Vargas Murillo"
    )
    st.session_state.student_id = st.text_input(
        "Carné institucional:",
        value=st.session_state.student_id,
        placeholder="Ej. ECO-2026-0482"
    )
    st.session_state.student_group = st.selectbox(
        "Grupo / Modalidad:",
        ["Economía - Grupo 1 (Sincrónica)", "Economía - Grupo 2 (Sincrónica)", "Taller de Nivelación"],
        index=0
    )

    st.markdown("---")
    st.subheader("📚 Fuentes Académicas Base")
    st.markdown("""
    - <span class="badge-morales">Morales Castro</span> **Crédito y Cobranza (pp. 27-36):**
      *Las 5 C del Crédito, análisis del deudor y flujos netos.*
    - <span class="badge-sugef">SUGEF 24-22</span> **Reglamento Entidades Supervisadas:**
      *Supervisión Basada en Riesgos (SBR), Metodología GREAC y Grados de Irregularidad.*
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🎯 Principios Pedagógicos")
    st.caption("""
    - **Enfoque:** Pensamiento Crítico & Case Method.
    - **Restricción Cognitiva:** La app te desafía a contrastar variables macroeconómicas con microfinancieras; no te da respuestas prefabricadas.
    - **Fases:** Raíces analógicas ➔ Demostración ➔ Estudio de Caso ➔ Simulación ➔ Maestría Feynman.
    """)

    # Barra de progreso de la sesión
    completed_steps = 0
    total_steps = 5
    if st.session_state.student_name.strip() and st.session_state.student_id.strip():
        completed_steps += 1
    if st.session_state.trampa_justification.strip():
        completed_steps += 1
    if st.session_state.case_q1.strip() and st.session_state.case_q2.strip():
        completed_steps += 1
    if st.session_state.sim_argument.strip():
        completed_steps += 1
    if st.session_state.feynman_explanation.strip() and st.session_state.strategic_answer.strip():
        completed_steps += 1
    
    prog_pct = int((completed_steps / total_steps) * 100)
    st.markdown(f"**Progreso acumulado: {prog_pct}%**")
    st.progress(completed_steps / total_steps)

# -----------------------------------------------------------------------------
# ENCABEZADO PRINCIPAL
# -----------------------------------------------------------------------------
st.markdown("""
<div class="main-header">
    <span class="badge-uia">Universidad Internacional de las Américas • Cátedra de Economía</span>
    <h1>Laboratorio de Pensamiento Crítico: Gestión de Riesgo Crediticio</h1>
    <p>Supervisión Basada en Riesgos (SUGEF 24-22 • Metodología GREAC) frente a la Evaluación Individual del Deudor (Las 5 C de Morales Castro)</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# NAVEGACIÓN POR PESTAÑAS (Fases de la Didáctica Universitaria)
# -----------------------------------------------------------------------------
tabs = st.tabs([
    "🧭 1. Raíces Analógicas & Rompe Hielo",
    "📊 2. Demostración Sincrónica (Micro vs Macro)",
    "💼 3. Estudio de Caso Riguroso (Case Method)",
    "⚖️ 4. Simulación: Comité vs Inspección SUGEF",
    "🎓 5. Maestría, Método Feynman & Exportación"
])

# =============================================================================
# PESTAÑA 1: RAÍCES ANALÓGICAS & ROMPE HIELO
# =============================================================================
with tabs[0]:
    st.subheader("1. Raíces Analógicas: Entendiendo la Solvencia sin Memorizar")
    st.markdown("""
    Para un economista en formación, la diferencia entre analizar a un **deudor individual** y evaluar la **solvencia de una entidad bancaria** 
    puede resultar abstracta. Utilizamos modelos analógicos para anclar el pensamiento intuitivo antes de pasar a la formulación técnica.
    """)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="analogy-box">
            <h3>🚢 La Analogía del Barco de Carga</h3>
            <p><strong>Nivel Micro (Las 5 C de Morales Castro):</strong> Cada contenedor individual representa un crédito otorgado. Nos aseguramos de que cada contenedor esté bien sellado, pesado y sujeto con cadenas (garantías y colaterales).</p>
            <p><strong>Nivel Macro (Metodología GREAC - SUGEF):</strong> Evalúa el barco completo:</p>
            <ul>
                <li>¿Tiene el capitán brújula y timoneles éticos? (<strong>G - Gobierno Corporativo</strong>)</li>
                <li>¿Funcionan los radares de tormenta? (<strong>R - Gestión de Riesgos</strong>)</li>
                <li>¿El casco tiene fugas de agua? (<strong>E - Evaluación Financiera</strong>)</li>
                <li>¿Se cumplen las leyes marítimas internacionales? (<strong>A - Ambiente Cumplimiento</strong>)</li>
                <li>¿Flota a una distancia segura de la línea de agua? (<strong>C - Capital Base</strong>)</li>
            </ul>
            <p><em>Un barco con contenedores perfectamente amarrados pero con un capitán negligente y casco fracturado, se hundirá de todos modos.</em></p>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div class="analogy-box" style="background: linear-gradient(135deg, #064E3B 0%, #065F46 100%); border-color: #059669;">
            <h3>🚌 La Analogía del Autobús de Pasajeros</h3>
            <p><strong>Nivel Micro:</strong> Verificar si cada pasajero tiene para pagar su tiquete y si lleva una maleta de respaldo como garantía.</p>
            <p><strong>Nivel Macro (Supervisión Prudencial):</strong> No basta con saber si los pasajeros pagaron el tiquete:</p>
            <ul>
                <li>¿Tiene el chofer licencia profesional y descanso adecuado?</li>
                <li>¿El motor recibe mantenimiento preventivo riguroso?</li>
                <li>¿La estructura soporta una frenada de emergencia en carretera mojada?</li>
            </ul>
            <p><strong>Lección Clave:</strong> La quiebra bancaria no se produce únicamente porque algunos deudores fallen; ocurre cuando la <strong>arquitectura institucional y la gobernanza</strong> fallan al absorber shocks sistémicos.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🧊 Dinámica de Rompe Hielo: El Término Trampa")
    st.markdown("""
    Analiza con rigor técnico la siguiente afirmación provocadora que suele confundir a profesionales no entrenados en Supervisión Basada en Riesgos:
    """)

    st.markdown("""
    <div class="card-warning" style="background: #2A1705 !important; border: 2px solid #F59E0B !important; border-left: 8px solid #F59E0B !important; border-radius: 12px !important; padding: 1.4rem 1.6rem !important;">
        <h4 style="margin-top:0; color: #FCD34D !important; font-size: 1.25rem !important; font-weight: 700 !important; letter-spacing: -0.01em;">⚠️ AFIRMACIÓN PROVOCADORA EN PANTALLA:</h4>
        <p style="font-size: 1.25rem !important; font-style: italic !important; margin-bottom: 0 !important; color: #FFFBEB !important; font-weight: 600 !important; line-height: 1.65 !important;">
        "Si un banco comercial privado en Costa Rica registra utilidades contables elevadas y toda su cartera de créditos de consumo cuenta con un 100% de cobertura en garantías hipotecarias reales, la SUGEF lo ubicará automáticamente en Grado de Normalidad N1."
        </p>
    </div>
    """, unsafe_allow_html=True)

    trampa_sel = st.radio(
        "¿Cuál es tu veredicto técnico preliminar?",
        ["Verdadero", "Falso"],
        index=0 if st.session_state.trampa_answer == "Verdadero" else (1 if st.session_state.trampa_answer == "Falso" else 0),
        key="radio_trampa"
    )
    st.session_state.trampa_answer = trampa_sel

    st.session_state.trampa_justification = st.text_area(
        "Fundamenta tu razonamiento económico y regulatorio (¿Por qué? Cita principios de la SUGEF 24-22 y la naturaleza de las garantías reales):",
        value=st.session_state.trampa_justification,
        placeholder="Explica qué evalúa la SUGEF según el marco GREAC, la diferencia entre utilidad contable presente y riesgo prospectivo, y por qué las garantías no garantizan liquidez inmediata...",
        height=130
    )

    if st.button("Evaluar mi Razonamiento del Término Trampa", key="btn_eval_trampa"):
        user_text = st.session_state.trampa_justification.lower()
        has_length = len(user_text.strip()) >= 50
        mentions_governance = any(w in user_text for w in ["gobierno", "gobernanza", "greac", "gestión", "riesgo", "prospectiv"])
        mentions_liquidity_or_guarantee = any(w in user_text for w in ["iliquid", "ejecución", "judicial", "capacidad de pago", "fuente primaria", "ahorrantes", "fiduciar"])
        
        if trampa_sel == "Falso":
            if has_length and (mentions_governance or mentions_liquidity_or_guarantee):
                st.session_state.trampa_feedback = {
                    "type": "success",
                    "title": "¡Excelente rigor analítico!",
                    "detail": "Has identificado con precisión la trampa cognitiva. Bajo el Acuerdo SUGEF 24-22, la supervisión NO es estática ni contable. Aunque existan colaterales al 100% y utilidades presentes, si el Gobierno Corporativo (G) es imprudente, o la fuente primaria de pago de los deudores colapsa, la entidad puede caer en Grados de Irregularidad (IRR1, IRR2 o IRR3). Las garantías son una fuente secundaria costosa y lenta de liquidar."
                }
            else:
                st.session_state.trampa_feedback = {
                    "type": "warning",
                    "title": "Veredicto correcto, pero requiere mayor profundidad técnica",
                    "detail": "Tu elección (FALSO) es acertada, pero tu justificación debe incorporar conceptos clave de la normativa: ¿Qué pasa con el tiempo de ejecución judicial de una hipoteca? ¿Qué estipula la metodología GREAC sobre la calidad de la alta gerencia y la evaluación prospectiva de la cartera?"
                }
        else:
            st.session_state.trampa_feedback = {
                "type": "danger",
                "title": "Alerta cognitiva: Has caído en el paradigma contable tradicional",
                "detail": "La afirmación es FALSA. La historia financiera y la SUGEF demuestran que un banco puede colapsar teniendo utilidades contables y colaterales registrados si carece de liquidez y gobernanza ética. El Acuerdo SUGEF 24-22 migró precisamente del viejo modelo CAMELS hacia la Supervisión Basada en Riesgos (GREAC) para no depender ciegamente de garantías estáticas."
            }

    if st.session_state.trampa_feedback:
        fb = st.session_state.trampa_feedback
        if fb["type"] == "success":
            st.markdown(f'<div class="card-accent"><strong>{fb["title"]}</strong><p>{fb["detail"]}</p></div>', unsafe_allow_html=True)
        elif fb["type"] == "warning":
            st.markdown(f'<div class="card-warning"><strong>{fb["title"]}</strong><p>{fb["detail"]}</p></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="card-danger"><strong>{fb["title"]}</strong><p>{fb["detail"]}</p></div>', unsafe_allow_html=True)

# =============================================================================
# PESTAÑA 2: DEMOSTRACIÓN SINCRÓNICA (MICRO VS MACRO)
# =============================================================================
with tabs[1]:
    st.subheader("2. Exposición y Demostración Sincrónica: La Arquitectura del Riesgo")
    st.markdown("""
    En esta sección contrastamos de manera cruzada los dos pilares normativos de nuestra sesión:
    **Nivel Micro** (Morales Castro: evaluación del solicitante) vs. **Nivel Macroprudencial** (SUGEF 24-22: calificación de la entidad).
    """)

    st.markdown("""
    <div style="display: flex; gap: 10px; margin-bottom: 15px; flex-wrap: wrap;">
        <span class="metric-chip">🔍 Nivel Micro: 5 C del Crédito</span>
        <span class="metric-chip">🏛️ Nivel Macro: Metodología GREAC</span>
        <span class="metric-chip">📉 Transmisión: TPM, Tipo de Cambio & Desempleo</span>
        <span class="metric-chip">🛡️ Responsabilidad Fiduciaria: Protección del Ahorrante</span>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <h3 style="color: #818CF8 !important; margin-top:0;">📋 Nivel Micro: Las 5 C del Crédito (Morales Castro)</h3>
            <p>Se enfoca en la probabilidad de incumplimiento de un deudor específico antes y durante el desembolso:</p>
            <ol>
                <li><strong>Conducta (Calidad Moral):</strong> Historial en el buró crediticio (últimos 24 meses), veracidad de la información y cumplimiento de contratos.</li>
                <li><strong>Capacidad de Pago:</strong> Análisis cuantitativo de ventas netas, márgenes y generación de <em>flujo de efectivo neto</em> (fuente primaria de repago).</li>
                <li><strong>Capital (Apalancamiento):</strong> Nivel de recursos propios invertidos en la firma frente a deuda con terceros.</li>
                <li><strong>Colateral (Garantías):</strong> Prendas, hipotecas o fideicomisos como <em>fuente secundaria o alterna</em> en caso de quiebra.</li>
                <li><strong>Condiciones:</strong> Sensibilidad del cliente al ciclo económico, sector de actividad y contexto del país.</li>
            </ol>
            <div style="background: rgba(99, 102, 241, 0.18) !important; border: 1px solid #6366F1 !important; padding: 12px !important; border-radius: 8px !important; font-size: 0.9rem !important; color: #E0E7FF !important;">
                <strong style="color: #FFFFFF !important;">Regla de oro de Morales Castro:</strong> Un crédito nunca debe otorgarse basándose únicamente en el colateral; la fuente primaria de pago SIEMPRE debe ser el flujo operativo.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3 style="color: #2DD4BF !important; margin-top:0;">🏛️ Nivel Macro: Metodología GREAC (Acuerdo SUGEF 24-22)</h3>
            <p>Califica la solidez estructural y gobernanza del intermediario financiero bajo 5 pilares estratégicos:</p>
            <ol>
                <li><strong>G - Gobierno Corporativo:</strong> Calidad de la Junta Directiva, ética, transparencia y límites contra la toma imprudente de riesgos.</li>
                <li><strong>R - Gestión de Riesgos:</strong> Capacidad técnica para identificar, medir, mitigar y monitorear riesgos (crédito, liquidez, mercado, TI).</li>
                <li><strong>E - Evaluación Económico-Financiera:</strong> Calidad real de los activos, morosidad, cobertura de provisiones y rentabilidad genuina.</li>
                <li><strong>A - Ambiente de Cumplimiento:</strong> Apego estricto al marco legal, prevención de legitimación de capitales y mandatos de supervisión.</li>
                <li><strong>C - Capital Base y Suficiencia:</strong> Patrimonio neto disponible y coeficiente de suficiencia patrimonial para absorber pérdidas no esperadas.</li>
            </ol>
            <div style="background: rgba(13, 148, 136, 0.18) !important; border: 1px solid #0D9488 !important; padding: 12px !important; border-radius: 8px !important; font-size: 0.9rem !important; color: #CCFBF1 !important;">
                <strong style="color: #FFFFFF !important;">Mapeo de Solvencia:</strong> Clasifica en <strong>Normalidad (N1, N2, N3)</strong> o en <strong>Irregularidad (IRR1, IRR2, IRR3)</strong>, pudiendo desencadenar planes obligatorios de saneamiento o intervención judicial.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("⚡ Canales de Transmisión Macroeconómica hacia la Cartera de Crédito")
    st.markdown("""
    Explore cómo variables agregadas de la economía costarricense estresan simultáneamente el nivel micro y el nivel macro:
    """)

    tab_m1, tab_m2, tab_m3 = st.tabs([
        "📈 Tasa de Política Monetaria (TPM) y Cuota",
        "💵 Tipo de Cambio y Deudores No Generadores",
        "⚖️ Grados de Irregularidad (IRR1 a IRR3)"
    ])

    with tab_m1:
        st.markdown("""
        #### El Impacto de una Subida en la TPM del Banco Central
        - **Mecanismo:** Ante presiones inflacionarias, el BCCR eleva la TPM. Esto encarece el fondeo interbancario y traslada el alza hacia la **Tasa Básica Pasiva (TBP)** y las tasas activas de préstamos a tasa variable.
        - **Efecto Micro:** Se incrementa la cuota mensual del deudor sin que sus ingresos aumenten. La **segunda C (Capacidad de pago)** se estrangula, elevando el indicador Cuota/Ingreso por encima de umbrales sostenibles (ej. > 45%).
        - **Efecto Macro (SUGEF):** La cartera entra en mora temprana (> 30 y > 90 días). Si el banco no constituyó reservas prospectivas, debe castigar utilidades para dotar estimaciones por deterioro, erosionando el pilar **C (Capital Base)**.
        """)

    with tab_m2:
        st.markdown("""
        #### Deudores en Moneda Extranjera No Generadores de Divisas
        - **Mecanismo:** Personas u hogares que perciben sus ingresos en Colones (CRC) pero contratan deudas en Dólares (USD) atraídos por tasas nominales más bajas.
        - **Efecto Micro:** Si ocurre una depreciación imprevista del colón, el servicio de la deuda se incrementa automáticamente en moneda local (descalce de monedas).
        - **Efecto Macro (SUGEF):** El Acuerdo SUGEF 24-22 exige ponderar con mayor requerimiento de capital estos créditos debido al riesgo cambiario crediticio implícito. Si el banco concentró su cartera en este segmento sin coberturas, el pilar **R (Gestión de Riesgos)** es calificado con nota deficiente.
        """)

    with tab_m3:
        st.markdown("""
        #### Escala de Severidad del Acuerdo SUGEF 24-22
        Las entidades supervisadas se ubican en alguna de las siguientes categorías según la evaluación GREAC:
        """)
        c_n1, c_irr = st.columns(2)
        with c_n1:
            st.markdown("""
            **Grados de Normalidad:**
            - **Normalidad 1 (N1):** Entidad financieramente sólida, gestión y gobierno altamente efectivos. Debilidades operativas mínimas.
            - **Normalidad 2 (N2):** Desempeño adecuado, pero exhibe debilidades que si no se atienden podrían deteriorar su perfil patrimonial.
            - **Normalidad 3 (N3):** Debilidades relevantes en gestión de riesgos o rentabilidad; requiere plan de acción correctivo formal.
            """)
        with c_irr:
            st.markdown("""
            **Grados de Irregularidad (Riesgo Sistémico):**
            - **Irregularidad 1 (IRR1):** Deterioro moderado en suficiencia de capital o fallas graves de control interno.
            - **Irregularidad 2 (IRR2):** Debilidad severa en suficiencia patrimonial o gobierno corporativo no confiable. Plan de saneamiento mandatorio.
            - **Irregularidad 3 (IRR3):** Inviabilidad financiera inminente o insolvencia. Causal legal directa de **intervención institucional** para salvaguardar a los depositantes.
            """)

# =============================================================================
# PESTAÑA 3: ESTUDIO DE CASO RIGUROSO (CASE METHOD)
# =============================================================================
with tabs[2]:
    st.markdown("""
    <div class="card" style="border-top: 4px solid #0284C7 !important;">
        <span class="badge-uia">Metodología Pedagógica: Case Method</span>
        <h2 style="color: #F8FAFC !important; margin: 0.3rem 0;">1) Título del Case Study</h2>
        <h3 style="color: #38BDF8 !important; margin-top:0;">El Dilema de Banco Promotor: La Ilusión de las Utilidades Contables, el Espejismo de la Hipoteca y el Choque Supervisor GREAC</h3>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🎯 2) Objetivos de Aprendizaje del Caso", expanded=True):
        st.markdown("""
        1. **Desarrollar Pensamiento Crítico Económico:** Diferenciar de manera analítica entre la rentabilidad contable inmediata de una colocación crediticia agresiva y el riesgo sistémico de solvencia a mediano plazo.
        2. **Aplicar Modelos Teóricos Cruzados:** Contrastar la evaluación individual del deudor (*Las 5 C de Morales Castro*) con la supervisión prudencial institucional (*Acuerdo SUGEF 24-22 y marco GREAC*).
        3. **Evaluar Compensaciones (Trade-Offs):** Ponderar el conflicto entre la presión de los accionistas por maximizar el margen financiero de corto plazo y el deber fiduciario de proteger los ahorros del público.
        """)

    with st.expander("📖 3) Contexto del Caso Institucional", expanded=True):
        st.markdown("""
        Durante los últimos 24 meses, **Banco Promotor S.A.** (banco privado supervisado por la SUGEF) experimentó un crecimiento interanual del **35% en su cartera de créditos de consumo y tarjetas de crédito**.
        
        Para justificar esta expansión acelerada ante su Comité de Auditoría, la Gerencia Comercial estableció una política: **exigir garantías hipotecarias abiertas con cobertura del 120% del monto financiado** sobre segundas propiedades o viviendas familiares de los solicitantes. 
        
        Las cifras contables más recientes muestran utilidades netas récord y una morosidad histórica aparentemente baja (1.6%). Sin embargo, el entorno macroeconómico experimentó un cambio de ciclo:
        - El Banco Central elevó la **Tasa de Política Monetaria (TPM) en 350 puntos base**, encareciendo los créditos indexados a tasa variable.
        - Un **28% de la cartera de consumo colocada fue otorgada en dólares a deudores asalariados que perciben sus ingresos en colones** (no generadores de divisas).
        - La inflación acumulada erosionó el salario real disponible de las familias de clase media.
        """)

    with st.expander("⚡ 4) Planteamiento del Problema o Desafío Central", expanded=True):
        st.markdown("""
        Una misión de supervisión *in situ* de la SUGEF acaba de concluir su informe preliminar bajo la metodología **GREAC**. Los inspectores señalan graves hallazgos:
        
        1. **Debilidad en la 2da C (Capacidad de Pago):** Banco Promotor relajó el análisis de flujo neto proyectado, asumiendo que "mientras exista hipoteca inscrita, el banco no puede perder".
        2. **Fallas en el Pilar G (Gobierno Corporativo):** La Junta Directiva vinculó los bonos salariales de la alta gerencia únicamente al volumen de colocación de créditos, sin métricas ajustadas por riesgo crediticio.
        3. **Iliquidez del Colateral:** La ejecución judicial de una hipoteca en los tribunales de Costa Rica tarda entre 36 y 60 meses, incurre en costas legales, depreciación del inmueble y no genera flujo líquido para pagar a los ahorrantes que retiran sus depósitos día a día.
        
        **El Desafío:** La SUGEF amenaza con reclasificar a Banco Promotor de **Normalidad N1** directamente a **Irregularidad IRR2**, exigiéndole constituir provisiones extraordinarias por ₡12.000 millones y detener de inmediato el pago de dividendos a sus accionistas.
        """)

    with st.expander("🔬 5) Guía de Investigación y Posicionamiento Estudiantil", expanded=True):
        st.markdown("""
        Analiza los fragmentos de Morales Castro (pp. 27-36: *Fuentes primarias vs alternas de pago, análisis de flujo neto y factores de seguimiento*) 
        y los Lineamientos del Acuerdo SUGEF 24-22 (Anexo I: *Calidad del Gobierno Corporativo y requerimientos de solvencia*). 
        
        Responde a las siguientes tres interrogantes fundamentales para fijar tu postura económica:
        """)

    st.markdown("### ✍️ Respuestas del Estudiante al Caso de Estudio")

    col_q1, col_q2 = st.columns(2)
    with col_q1:
        st.session_state.case_q1 = st.text_area(
            "Pregunta 1: ¿Por qué la garantía hipotecaria al 120% NO subsana la falta de flujo de caja neto del deudor frente a la subida de la TPM?",
            value=st.session_state.case_q1,
            placeholder="Analiza la diferencia entre fuente primaria y alterna de pago según Morales Castro, la iliquidez del activo y el tiempo de cobro judicial...",
            height=140
        )
    with col_q2:
        st.session_state.case_q2 = st.text_area(
            "Pregunta 2: ¿Qué falla de Gobierno Corporativo (Pilar G de SUGEF 24-22) cometió la Junta Directiva de Banco Promotor?",
            value=st.session_state.case_q2,
            placeholder="Reflexiona sobre los incentivos perversos de la gerencia, la gestión prudencial de riesgos vs rentabilidad de corto plazo...",
            height=140
        )

    st.session_state.case_q3 = st.text_area(
        "Pregunta 3: Como asesor económico, ¿qué trade-off enfrenta el banco entre repartir dividendos a los accionistas o recapitalizarse para evitar caer en Grado IRR2?",
        value=st.session_state.case_q3,
        placeholder="Evalúa el costo de oportunidad, el deber fiduciario ante los depositantes, la absorción de pérdidas y la estabilidad del sistema financiero...",
        height=120
    )

    if st.button("Guardar y Evaluar Respuestas del Caso", key="btn_eval_case"):
        t1 = st.session_state.case_q1.strip()
        t2 = st.session_state.case_q2.strip()
        t3 = st.session_state.case_q3.strip()
        
        if len(t1) < 40 or len(t2) < 40 or len(t3) < 40:
            st.session_state.case_feedback = {
                "type": "warning",
                "text": "Tus respuestas son demasiado breves o esquemáticas. Para alcanzar nivel universitario en Economía, profundiza en el análisis técnico de cada pregunta antes de enviar tu posición final."
            }
        else:
            # Análisis semántico formativo
            k_primary = any(w in t1.lower() for w in ["primaria", "flujo", "iliquid", "tiempo", "ejecución", "judicial", "secundaria"])
            k_gov = any(w in t2.lower() for w in ["incentivo", "bono", "directiva", "riesgo", "fiduciar", "corto plazo", "ética"])
            k_tradeoff = any(w in t3.lower() for w in ["ahorrante", "capital", "patrimonio", "solvencia", "provisión", "depósito"])

            score_sub = sum([k_primary, k_gov, k_tradeoff])
            if score_sub == 3:
                st.session_state.case_feedback = {
                    "type": "success",
                    "text": "Excelente articulación económica. Has conectado la incapacidad de transformar ladrillos e hipotecas en liquidez inmediata (fuente secundaria de Morales Castro) con los fallos de gobernanza y la erosión patrimonial bajo el marco GREAC de la SUGEF."
                }
            else:
                st.session_state.case_feedback = {
                    "type": "info",
                    "text": "Respuestas registradas en sesión. Has abordado elementos esenciales, pero te recomendamos reforzar la interconexión entre la iliquidez judicial de las garantías y el mandato fiduciario de proteger a los ahorrantes."
                }

    if st.session_state.case_feedback:
        cf = st.session_state.case_feedback
        if cf["type"] == "success":
            st.markdown(f'<div class="card-accent"><strong>Retroalimentación Formativa:</strong><p>{cf["text"]}</p></div>', unsafe_allow_html=True)
        elif cf["type"] == "warning":
            st.markdown(f'<div class="card-warning"><strong>Atención Requerida:</strong><p>{cf["text"]}</p></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="card-accent" style="border-left-color: #0284C7;"><strong>Retroalimentación Formativa:</strong><p>{cf["text"]}</p></div>', unsafe_allow_html=True)

# =============================================================================
# PESTAÑA 4: SIMULACIÓN DE COMITÉ VS INSPECCIÓN SUGEF
# =============================================================================
with tabs[3]:
    st.subheader("4. Laboratorio de Toma de Decisiones y Simulación de Estrés")
    st.markdown("""
    En esta fase experimental interactiva, pondrás a prueba la resiliencia del modelo económico de Banco Promotor ante shocks macroeconómicos.
    Simula la sesión del **Comité de Riesgos** y asume un rol protagónico para emitir tu dictamen técnico.
    """)

    sim_col1, sim_col2 = st.columns([1, 1])

    with sim_col1:
        st.markdown("#### 🎛️ Parámetros del Entorno de Estrés")
        st.session_state.sim_tpm_delta = st.slider(
            "Incremento en Tasa de Política Monetaria (TPM) [Puntos Porcentuales]:",
            min_value=0.0,
            max_value=6.0,
            value=float(st.session_state.sim_tpm_delta),
            step=0.5,
            help="Simula el endurecimiento monetario del BCCR para frenar la inflación."
        )

        st.session_state.sim_fx_deprec = st.slider(
            "Depreciación imprevista del Tipo de Cambio (CRC/USD) [%]:",
            min_value=0.0,
            max_value=30.0,
            value=float(st.session_state.sim_fx_deprec),
            step=2.0,
            help="Afecta directamente la cuota de los deudores en dólares que ganan colones."
        )

        st.session_state.sim_role = st.selectbox(
            "Selecciona tu Rol en el Debate:",
            [
                "Oficial Inspector SUGEF (Enfoque Prudencial & Supervisión Basada en Riesgos)",
                "Director Comercial / Comité de Crédito (Enfoque de Negocio & Maximización de Margen)",
                "Auditor Independiente (Defensa Fiduciaria de los Depositantes)"
            ],
            index=0
        )

        st.session_state.sim_policy_choice = st.radio(
            "Decisión Estratégica Inmediata a Someter a Votación:",
            [
                "Opción A: Suspender reparto de dividendos, constituir ₡12.000M en provisiones y reestructurar deudas sin costo a deudores vulnerables.",
                "Opción B: Mantener el ritmo comercial, confiar en la ejecución masiva de garantías hipotecarias y solicitar una prórroga a la SUGEF.",
                "Opción C: Vender la cartera de consumo con descuento a un fondo externo y concentrar los recursos en títulos del Gobierno."
            ]
        )

    with sim_col2:
        st.markdown("#### 📊 Impacto Proyectado en la Entidad")
        # Cálculo pedagógico reactivo
        stress_score = (st.session_state.sim_tpm_delta * 1.8) + (st.session_state.sim_fx_deprec * 0.9)
        base_mora = 1.6
        projected_mora = round(base_mora + (stress_score * 0.45), 2)
        base_suficiencia = 12.8 # %
        projected_suficiencia = round(max(5.5, base_suficiencia - (stress_score * 0.32)), 2)
        
        if projected_suficiencia >= 11.5:
            calif_greac = "Normalidad 1 (N1)"
            status_box = "card-accent"
            status_text = "Entidad dentro de límites de tolerancia regulatoria."
        elif projected_suficiencia >= 10.0:
            calif_greac = "Normalidad 2 / 3 (N2/N3)"
            status_box = "card-warning"
            status_text = "Alerta: Fragilidad patrimonial incipiente; requiere plan correctivo."
        elif projected_suficiencia >= 8.0:
            calif_greac = "Irregularidad 1 (IRR1)"
            status_box = "card-warning"
            status_text = "Alerta Grave: Déficit de capital y necesidad de aporte de socios."
        else:
            calif_greac = "Irregularidad 2 / 3 (IRR2 / IRR3)"
            status_box = "card-danger"
            status_text = "Peligro Crítico: Causal de Intervención Administrativa por SUGEF."

        st.markdown(f"""
        <div class="{status_box}">
            <h4 style="margin-top:0;">Calificación Estimada GREAC: <strong>{calif_greac}</strong></h4>
            <p style="margin-bottom:5px;"><strong>Morosidad Proyectada:</strong> {projected_mora}% (Partiendo de 1.6%)</p>
            <p style="margin-bottom:5px;"><strong>Suficiencia Patrimonial Estimada:</strong> {projected_suficiencia}% (Mínimo legal regulatorio: 10.0%)</p>
            <p style="margin-bottom:0; font-size: 0.9rem;"><em>{status_text}</em></p>
        </div>
        """, unsafe_allow_html=True)

        st.info("""
        💡 **Nota Técnica de Aula:** Observe cómo el descalce cambiario y el alza de tasas deterioran simultáneamente la liquidez de los deudores (micro) 
        y el coeficiente de suficiencia de capital del banco (macro), demostrando que el colateral no evita el deterioro de los activos.
        """)

    st.markdown("---")
    st.subheader("🗣️ Dictamen Argumentativo del Estudiante")
    st.session_state.sim_argument = st.text_area(
        f"Como {st.session_state.sim_role}, redacta tu dictamen técnico fundamentando por qué tu decisión es la correcta y cómo responde ante la metodología GREAC:",
        value=st.session_state.sim_argument,
        placeholder="Defiende tu posición combinando la responsabilidad fiduciaria, el destino del capital de los ahorrantes y la inviabilidad de esperar a la ejecución judicial...",
        height=150
    )

    if st.button("Emitir Dictamen Oficial de Simulación", key="btn_eval_sim"):
        arg_text = st.session_state.sim_argument.strip()
        if len(arg_text) < 50:
            st.session_state.sim_feedback = {
                "status": "warning",
                "msg": "Tu dictamen carece de extensión analítica suficiente. Presenta argumentos basados en la normativa SUGEF 24-22 y las 5 C de Morales Castro."
            }
        else:
            if "Opción A" in st.session_state.sim_policy_choice:
                st.session_state.sim_feedback = {
                    "status": "success",
                    "msg": "Dictamen alineado con la Supervisión Basada en Riesgos. Priorizar la constitución de provisiones contracíclicas y sacrificar dividendos inmediatos protege el Capital Base (Pilar C) y honra el principio de Responsabilidad Fiduciaria ante los ahorrantes."
                }
            elif "Opción B" in st.session_state.sim_policy_choice:
                st.session_state.sim_feedback = {
                    "status": "danger",
                    "msg": "Dictamen de alto riesgo moral. Confiar en la ejecución hipotecaria en un escenario de mora creciente genera iliquidez operativa masiva y probablemente precipite la reclasificación del banco hacia IRR2 o IRR3 por parte de la SUGEF."
                }
            else:
                st.session_state.sim_feedback = {
                    "status": "info",
                    "msg": "Decisión de mercado no convencional. Vender cartera castigada traslada pérdidas directas inmediatas al balance patrimonial, lo que exige evaluar si el capital restante puede amortiguar el descuento aplicado."
                }

    if st.session_state.sim_feedback:
        sf = st.session_state.sim_feedback
        if sf["status"] == "success":
            st.markdown(f'<div class="card-accent"><strong>Evaluación del Dictamen:</strong><p>{sf["msg"]}</p></div>', unsafe_allow_html=True)
        elif sf["status"] == "danger":
            st.markdown(f'<div class="card-danger"><strong>Evaluación del Dictamen:</strong><p>{sf["msg"]}</p></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="card-warning"><strong>Evaluación del Dictamen:</strong><p>{sf["msg"]}</p></div>', unsafe_allow_html=True)

# =============================================================================
# PESTAÑA 5: MAESTRÍA, MÉTODO FEYNMAN & EXPORTACIÓN
# =============================================================================
with tabs[4]:
    st.subheader("5. Comprobación de Maestría: Explicación Feynman & Síntesis Fiduciaria")
    st.markdown("""
    Para consolidar el aprendizaje, demostramos dominio traduciendo conceptos abstractos en explicaciones de claridad cristalina 
    y respondiendo a la pregunta estratégica de cierre.
    """)

    st.markdown("""
    <div class="card-dark">
        <h3 style="color: #38BDF8; margin-top:0;">🧠 Reto Feynman: La Prueba de la Simplicidad</h3>
        <p style="font-size: 1.05rem; margin-bottom: 0;">
        "Explica con tus propias palabras (como si le hablaras a un familiar sin conocimientos financieros) 
        por qué un banco repleto de hipotecas inscritas sobre casas de lujo puede quebrar si sus clientes se quedan sin empleo o sus salarios no alcanzan para pagar la cuota mensual."
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.session_state.feynman_explanation = st.text_area(
        "Tu Explicación Método Feynman (Claridad, metáforas sencillas y rigor de fondo):",
        value=st.session_state.feynman_explanation,
        placeholder="Ejemplo: Si un depositante va mañana a retirar sus ahorros a ventanilla, el banco no puede pagarle con un pedazo de ladrillo o una pared...",
        height=130
    )

    st.markdown("---")
    st.markdown("""
    <div class="card-dark" style="border-color: #0D9488;">
        <h3 style="color: #2DD4BF; margin-top:0;">❓ Pregunta Estratégica de Cierre</h3>
        <p style="font-size: 1.05rem; margin-bottom: 0;">
        ¿Cómo se articula el principio de <strong>responsabilidad fiduciaria</strong> de una entidad financiera con la diferencia conceptual entre la evaluación del deudor individual (las 5 C de Morales Castro) y la calificación institucional bajo la metodología GREAC (Acuerdo SUGEF 24-22)? 
        ¿Qué consecuencias tiene para la estabilidad del sistema financiero costarricense que una Junta Directiva priorice la colocación comercial sobre los límites prudenciales?
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.session_state.strategic_answer = st.text_area(
        "Tu Respuesta Estratégica de Cierre (Rigor teórico y normativo):",
        value=st.session_state.strategic_answer,
        placeholder="Analiza la protección del dinero ajeno (depósitos del público), el deber legal de la Junta Directiva y la prevención del contagio sistémico...",
        height=150
    )

    st.markdown("---")
    st.subheader("📋 Consolidación y Generación del Reporte Académico")

    # Botón para calificar y consolidar
    if st.button("📊 Calificar Sesión y Generar Reporte Consolidado", type="primary", key="btn_consolidar"):
        # Verificación de completitud
        missing_fields = []
        if not st.session_state.student_name.strip():
            missing_fields.append("Nombre del Estudiante")
        if not st.session_state.student_id.strip():
            missing_fields.append("Carné del Estudiante")
        if not st.session_state.trampa_justification.strip():
            missing_fields.append("Justificación del Término Trampa (Pestaña 1)")
        if not st.session_state.case_q1.strip() or not st.session_state.case_q2.strip():
            missing_fields.append("Respuestas al Caso de Estudio (Pestaña 3)")
        if not st.session_state.sim_argument.strip():
            missing_fields.append("Dictamen de la Simulación (Pestaña 4)")
        if not st.session_state.feynman_explanation.strip():
            missing_fields.append("Explicación Feynman (Pestaña 5)")
        if not st.session_state.strategic_answer.strip():
            missing_fields.append("Pregunta Estratégica de Cierre (Pestaña 5)")

        if missing_fields:
            st.error(f"Faltan secciones por completar antes de generar el reporte final: {', '.join(missing_fields)}")
        else:
            # Algoritmo de evaluación por rúbrica
            score = 70 # Base por completitud rigurosa
            
            # Criterio 1: Calidad conceptual Micro vs Macro
            t_all = (st.session_state.trampa_justification + " " + st.session_state.case_q1 + " " + st.session_state.strategic_answer).lower()
            if any(k in t_all for k in ["primaria", "flujo de efectivo", "fuente secundaria", "iliquid"]):
                score += 10
            if any(k in t_all for k in ["fiduciar", "ahorrante", "depositante", "gobierno corporativo"]):
                score += 10
            if any(k in t_all for k in ["greac", "sugef", "irregularidad", "capital base", "sbr"]):
                score += 10
            
            st.session_state.final_score = min(score, 100)

            # Rúbrica formativa detallada
            st.session_state.final_rubric = {
                "Pensamiento Crítico y Discernimiento de Riesgo": "Excelente" if score >= 90 else "Adecuado",
                "Dominio Normativo SUGEF 24-22 (GREAC)": "Excelente" if "greac" in t_all or "sugef" in t_all else "En Desarrollo",
                "Aplicación de Modelo Morales Castro (5 C)": "Excelente" if "flujo" in t_all or "capacidad" in t_all else "Adecuado",
                "Responsabilidad Fiduciaria y Ética Financiera": "Excelente" if "fiduciar" in t_all or "ahorrante" in t_all else "Adecuado"
            }
            st.success("¡Sesión evaluada con éxito! Revisa la retroalimentación y descarga tu informe oficial.")

    # Si ya se evaluó, mostrar resumen y botón de descarga
    if st.session_state.final_score > 0:
        st.markdown(f"""
        <div class="card-accent" style="margin-top: 20px;">
            <h3 style="margin-top:0; color: #166534;">🎉 Calificación Global Obtenida: {st.session_state.final_score} / 100</h3>
            <p><strong>Estudiante:</strong> {st.session_state.student_name} | <strong>Carné:</strong> {st.session_state.student_id}</p>
            <p><strong>Programa:</strong> Licenciatura en Economía • U.I.A. • Semana 3 Sincrónica</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 📑 Rúbrica de Desempeño Cualitativo:")
        col_r1, col_r2 = st.columns(2)
        with col_r1:
            for k, v in list(st.session_state.final_rubric.items())[:2]:
                st.markdown(f"- **{k}:** <span class='rubric-tag rubric-excelente'>{v}</span>", unsafe_allow_html=True)
        with col_r2:
            for k, v in list(st.session_state.final_rubric.items())[2:]:
                st.markdown(f"- **{k}:** <span class='rubric-tag rubric-excelente'>{v}</span>", unsafe_allow_html=True)

        # Generación de informe consolidado descargable
        timestamp_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report_content = f"""# UNIVERSIDAD INTERNACIONAL DE LAS AMÉRICAS (U.I.A.)
## Escuela de Economía • Cátedra de Crédito y Finanzas
### REPORTE CONSOLIDADO DE SESIÓN SINCRÓNICA - SEMANA 3
**Fecha y Hora de Generación:** {timestamp_now}

---
### 1. DATOS DE IDENTIFICACIÓN DEL ESTUDIANTE
- **Nombre Completo:** {st.session_state.student_name}
- **Carné Universitario:** {st.session_state.student_id}
- **Grupo:** {st.session_state.student_group}
- **Calificación Formativa Global:** {st.session_state.final_score} / 100

---
### 2. RÚBRICA DE EVALUACIÓN DE COMPETENCIAS
{chr(10).join([f"- **{k}:** {v}" for k, v in st.session_state.final_rubric.items()])}

---
### 3. FASE 1: DINÁMICA DE ROMPE HIELO Y TÉRMINO TRAMPA
- **Afirmación:** 'Si un banco comercial registra altas utilidades contables y 100% cobertura hipotecaria, SUGEF lo ubica en Normalidad N1.'
- **Veredicto del Estudiante:** {st.session_state.trampa_answer}
- **Justificación Técnica:**
{st.session_state.trampa_justification}
- **Retroalimentación Emitida:**
{st.session_state.trampa_feedback.get('detail', 'Sin retroalimentación') if st.session_state.trampa_feedback else 'Aprobado'}

---
### 4. FASE 3: ESTUDIO DE CASO (CASE METHOD) - BANCO PROMOTOR
- **Pregunta 1 (Garantía hipotecaria vs Flujo de caja frente a TPM):**
{st.session_state.case_q1}

- **Pregunta 2 (Fallas de Gobierno Corporativo - Pilar G):**
{st.session_state.case_q2}

- **Pregunta 3 (Trade-off de dividendos vs Capitalización y solvencia):**
{st.session_state.case_q3}

- **Retroalimentación Formativa del Caso:**
{st.session_state.case_feedback.get('text', 'Sin comentarios') if st.session_state.case_feedback else 'Aprobado'}

---
### 5. FASE 4: SIMULACIÓN DE ESTRÉS Y DICTAMEN DE COMITÉ
- **Rol Asumido:** {st.session_state.sim_role}
- **Incremento de TPM Simulado:** +{st.session_state.sim_tpm_delta} pp
- **Depreciación Cambiaria Simulada:** +{st.session_state.sim_fx_deprec}%
- **Decisión de Política Elegida:** {st.session_state.sim_policy_choice}
- **Dictamen Argumentativo del Estudiante:**
{st.session_state.sim_argument}

---
### 6. FASE 5: COMPROBACIÓN DE MAESTRÍA & MÉTODO FEYNMAN
- **Explicación Feynman (Analogía simple de quiebra con hipotecas):**
{st.session_state.feynman_explanation}

- **Pregunta Estratégica de Cierre (Responsabilidad Fiduciaria, GREAC vs 5 C):**
{st.session_state.strategic_answer}

---
### 7. DICTAMEN FORMATIVO DE LA IA PEDAGÓGICA
El estudiante demuestra una comprensión sólida al abandonar la visión puramente contable del crédito y adoptar la perspectiva de la Supervisión Basada en Riesgos (SBR). Se destaca la articulación de la fuente primaria de pago (flujo de caja neto) por encima de la fuente alterna (garantías ilíquidas), así como el reconocimiento de la responsabilidad fiduciaria que vincula la gestión bancaria con la protección de los depositantes de la economía costarricense.

================================================================================
Fin del Reporte Consolidado • Universidad Internacional de las Américas
================================================================================
"""

        clean_filename = f"Reporte_S3_UIA_{(st.session_state.student_id or 'estudiante').replace(' ', '_')}.md"

        st.download_button(
            label="📥 Descargar Reporte Consolidado (.md)",
            data=report_content.encode("utf-8"),
            file_name=clean_filename,
            mime="text/markdown",
            type="primary"
        )
        st.caption("Guarde este archivo y entréguelo en el entorno virtual de aprendizaje de la U.I.A. como evidencia de su trabajo sincrónico.")

# -----------------------------------------------------------------------------
# PIE DE PÁGINA INSTITUCIONAL
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748B; font-size: 0.85rem; padding: 1.5rem 0;">
    <strong>Universidad Internacional de las Américas (U.I.A.)</strong> • Escuela de Economía<br>
    Cátedra de Análisis de Crédito y Finanzas • Aplicación de Pensamiento Crítico Sincrónica S3<br>
    Desarrollado bajo estándares pedagógicos universitarios y grounding estricto en SUGEF 24-22 y Morales Castro.
</div>
""", unsafe_allow_html=True)
