# Laboratorio de Pensamiento Crítico: Gestión de Riesgo Crediticio y Supervisión Basada en Riesgos (ACF - Semana 3)

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.50.0-FF4B4B.svg)](https://streamlit.io/)
[![Institución](https://img.shields.io/badge/Universidad-U.I.A.-0284C7.svg)](https://www.uia.ac.cr/)
[![Regulación](https://img.shields.io/badge/Normativa-SUGEF%2024--22-0D9488.svg)](https://www.sugef.fi.cr/)
[![Licencia](https://img.shields.io/badge/Licencia-Educativa%20Académica-green.svg)](#-licencia-y-nota-educativa)

Aplicación web interactiva desarrollada para la **Universidad Internacional de las Américas (U.I.A.)**, Escuela de Economía, para el curso de **Análisis de Crédito y Finanzas (ACF)** en su **Semana 3**. 

El software traduce marcos pedagógicos universitarios de pensamiento crítico en un entorno interactivo y socrático, articulando de manera cruzada la **evaluación del deudor individual a nivel micro** con la **regulación macroprudencial y la solvencia bancaria institucional**.

---

## 📌 Tabla de Contenidos
1. [Descripción General y Propósito Pedagógico](#-descripción-general-y-propósito-pedagógico)
2. [Marco Teórico y Normativo de Referencia](#-marco-teórico-y-normativo-de-referencia)
3. [Características Principales](#-características-principales)
4. [Estructura del Proyecto](#-estructura-del-proyecto)
5. [Requisitos Técnicos](#-requisitos-técnicos)
6. [Instalación Paso a Paso](#-instalación-paso-a-paso)
7. [Guía de Uso del Estudiante](#-guía-de-uso-del-estudiante)
8. [Interpretación Pedagógica de Resultados](#-interpretación-pedagógica-de-resultados)
9. [Licencia y Nota Educativa](#-licencia-y-nota-educativa)

---

## 🎯 Descripción General y Propósito Pedagógico

### Audiencia y Enfoque Didáctico
Esta herramienta está dirigida a estudiantes de **primer ingreso de la carrera de Economía** de la U.I.A. Su meta principal es erradicar la memorización pasiva y la repetición automática de fórmulas contables, guiando al estudiante hacia el razonamiento analítico riguroso.

### Restricción Cognitiva Aplicada
Bajo el diseño de ingeniería didáctica, **la aplicación no resuelve el problema por el alumno**. En su lugar, lo somete a situaciones de conflicto cognitivo donde debe:
* **Interpretar** estados financieros y entornos macroeconómicos adversos.
* **Evaluar** la diferencia crítica entre *liquidez inmediata* y *garantías ilíquidas*.
* **Inferir** los efectos de la política monetaria en la capacidad de repago familiar.
* **Justificar y contrastar** posturas ante comités de crédito y autoridades supervisoras.

---

## 📚 Marco Teórico y Normativo de Referencia

La aplicación integra de forma cruzada dos pilares doctrinales:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   ARQUITECTURA DEL RIESGO FINANCIERO                   │
├──────────────────────────────────┬─────────────────────────────────────┤
│   NIVEL MICRO (Evaluación Individual) │   NIVEL MACRO (Solvencia Sistémica)  │
│   Fuente: Morales Castro (pp. 27-36)  │   Fuente: Acuerdo SUGEF 24-22 (SBR) │
├──────────────────────────────────┼─────────────────────────────────────┤
│ 1. Conducta (Historial en buró)  │ 1. G - Calidad del Gobierno Corporativo │
│ 2. Capacidad (Flujo de caja neto)│ 2. R - Gestión Integral de Riesgos      │
│ 3. Capital (Apalancamiento)      │ 3. E - Evaluación Económico-Financiera │
│ 4. Colateral (Garantías reales)  │ 4. A - Ambiente de Cumplimiento Legal   │
│ 5. Condiciones (Ciclo económico) │ 5. C - Suficiencia de Capital Base      │
└──────────────────────────────────┴─────────────────────────────────────┘
```

* **Nivel Micro — Morales Castro (*Crédito y Cobranza*):** Explica la anatomía del riesgo crediticio del solicitante. Establece la regla fundamental: *la fuente primaria de pago SIEMPRE es el flujo de efectivo operativo generado por el deudor; las garantías (colateral) constituyen únicamente fuentes alternas o secundarias de mitigación ante el impago*.
* **Nivel Macroprudencial — Acuerdo SUGEF 24-22 (*Metodología GREAC*):** Reglamento de la Superintendencia General de Entidades Financieras de Costa Rica para calificar a intermediarios supervisados mediante la **Supervisión Basada en Riesgos (SBR)**. Clasifica a los intermediarios en **Grados de Normalidad (N1, N2, N3)** o **Grados de Irregularidad (IRR1, IRR2, IRR3)**, exigiendo planes de saneamiento o activando intervenciones institucionales cuando la solvencia patrimonial o la gobernanza se ven comprometidas.
* **Canales de Transmisión Macroeconómica:** Relación entre la Tasa de Política Monetaria (TPM) del Banco Central de Costa Rica (BCCR), la Tasa Básica Pasiva (TBP), el descalce cambiario en deudores no generadores de dólares y la erosión del ingreso disponible ante shocks de inflación y desempleo.

---

## ✨ Características Principales

La aplicación se estructura en 5 fases secuenciales según el diseño pedagógico:

### 1. Sidebar de Contexto e Identificación Institucional
* **Ficha del Estudiante:** Registro de Nombre, Carné Institucional y Grupo de la sesión sincrónica.
* **Barra de Progreso Dinámica:** Indicador en tiempo real del porcentaje de avance acumulado en la sesión.
* **Acreditación de Fuentes:** Badges y resumen de los principios didácticos del curso.

### 2. Fase 1: Raíces Analógicas & Rompe Hielo ("Término Trampa")
* **Modelos Mentales Intuitivos:** 
  * *La Analogía del Barco de Carga:* Contenedores bien amarrados (5 C individuales) vs. Casco agrietado y capitán imprudente (Fallas de gobernanza GREAC).
  * *La Analogía del Autobús de Pasajeros:* Pago del tiquete por el usuario vs. Mantenimiento del chasis y frenado de emergencia institucional.
* **Dinámica del Término Trampa:** Análisis de la afirmación provocadora:  
  > *"Si un banco comercial privado registra utilidades contables elevadas y 100% de cobertura hipotecaria, la SUGEF lo ubicará automáticamente en Normalidad N1."*
* **Retroalimentación Formativa Inmediata:** Contenedor de alto contraste que evalúa el razonamiento cualitativo sin anticipar respuestas mecánicas.

### 3. Fase 2: Bloque de Demostración y Exposición Sincrónica
* **Matriz Comparativa Micro vs. Macro:** Cuadros visuales interactivos de alto contraste que comparan los pilares de Morales Castro con los pilares GREAC de la SUGEF.
* **Pestañas de Canales de Transmisión:**
  * *TPM y Cuota Mensual:* Cómo las alzas de tasas elevan el indicador Cuota/Ingreso y deterioran la capacidad de pago.
  * *Descalce Cambiario:* Exposición de deudores que ganan en colones con pasivos en moneda extranjera.
  * *Escala Regulatoria:* Diferencias sustantivas entre Grados N1–N3 e Irregularidad IRR1–IRR3.

### 4. Fase 3: Módulo de Pensamiento Crítico — Estudio de Caso (Case Method)
Desarrollado bajo la estructura formal de **5 puntos**:
1. **Título del Case Study:** *El Dilema de Banco Promotor: La Ilusión de las Utilidades Contables, el Espejismo de la Hipoteca y el Choque Supervisor GREAC*.
2. **Objetivos de Aprendizaje:** Identificación de trade-offs entre rentabilidad de corto plazo y solvencia a mediano plazo.
3. **Contexto del Caso:** Entidad con crecimiento del 35% en créditos de consumo respaldados con hipotecas al 120%, enfrentando aumentos de TPM y deudores vulnerables.
4. **Planteamiento del Problema o Desafío Central:** Cuestionamientos de los inspectores de la SUGEF, costos y plazos de cobro judicial (36 a 60 meses), iliquidez de los inmuebles adjudicados y riesgo de caer en Grado IRR2.
5. **Guía de Investigación y Posicionamiento:** Preguntas de reflexión abierta donde el estudiante debe defender su postura económica por escrito.

### 5. Fase 4: Laboratorio de Simulación y Toma de Decisiones
* **Parámetros de Estrés Financiero:** Sliders interactivos para modelar incrementos en la TPM (0 a 6 puntos porcentuales) y depreciación del colón (0% a 30%).
* **Motor Reactivo de Impacto:** Cálculo en tiempo real de la tasa de morosidad proyectada, el coeficiente de suficiencia patrimonial (%) y la calificación GREAC resultante.
* **Role-Play Socrático:** El estudiante asume un rol (*Oficial Inspector SUGEF*, *Director Comercial*, o *Auditor Independiente*) y emite un dictamen técnico justificado para el Comité de Riesgos.

### 6. Fase 5: Comprobación de Maestría, Método Feynman & Exportación
* **Reto del Método Feynman:** Explicar con sencillez cristalina a una persona sin formación financiera por qué un banco lleno de garantías hipotecarias puede quebrar si sus clientes no tienen flujo de caja mensual.
* **Pregunta Estratégica Fiduciaria:** Articulación del deber de proteger los depósitos del público frente a la presión comercial de los accionistas.
* **Persistencia Integral de Datos:** Uso exhaustivo de `st.session_state` para consolidar todas las respuestas del alumno.
* **Generador de Reporte Oficial (.md):** Botón único de exportación que compila el expediente académico completo del alumno con su calificación formativa (0 a 100), rúbrica cualitativa de competencias y retroalimentación de la sesión.

---

## 📂 Estructura del Proyecto

```plaintext
S3ACF/
├── app.py                                            # Aplicación principal en Streamlit
├── Instrucciones.txt                                 # Prompt pedagógico y requerimientos de diseño didáctico
├── README.md                                         # Documentación técnica y pedagógica oficial
├── S3 - SUGEF 24-22 (v2 1° de enero de 2023).pdf     # Fuente regulatoria oficial: Acuerdo SUGEF 24-22
├── S3 Credito y cobranzas [40-49].pdf                # Fuente teórica micro: Morales Castro (Las 5 C)
└── S3ACF - Crédito y Cobranza - Gemini Notebook.pdf  # Fuente didáctica: Analogías, debates y dinámicas
```

---

## 💻 Requisitos Técnicos

* **Sistema Operativo:** Windows 10/11, macOS o Linux.
* **Lenguaje:** Python 3.10 o superior (Verificado en Python 3.13.7).
* **Dependencias Principales:**
  * `streamlit >= 1.50.0`
* **Módulos estándar de Python requeridos:** `datetime`, `json` (incluidos en la instalación base de Python).
* **Dependencias opcionales (para lectura automatizada de fuentes):**
  * `pypdf >= 5.0.0`
  * `pymupdf >= 1.25.0`

---

## 🚀 Instalación Paso a Paso

### 1. Clonar el repositorio
Abre una terminal (PowerShell en Windows o Bash en Linux/macOS) y clona el proyecto:

```bash
git clone https://github.com/randallnunezsancho-netizen/S3ACF.git
cd S3ACF
```

### 2. Crear y activar un entorno virtual (Recomendado)
Para aislar las dependencias del proyecto:

* **En Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```

* **En macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar dependencias
Instala Streamlit con el gestor de paquetes `pip`:

```bash
pip install streamlit
```

*(Opcional: Si deseas manipular y extraer texto de los documentos PDF de soporte)*:
```bash
pip install pypdf pymupdf
```

### 4. Ejecutar la aplicación
Inicia el servidor local de Streamlit:

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador web predeterminado en la dirección:
`http://localhost:8501`

---

## 📖 Guía de Uso del Estudiante

1. **Ingreso y Registro:**  
   En la barra lateral izquierda (Sidebar), escribe tu **Nombre completo** y **Carné institucional**. Esto habilitará la trazabilidad para tu informe final.
2. **Exploración Analógica (Pestaña 1):**  
   Lee las analogías del *Barco de Carga* y el *Autobús*. Responde a la afirmación del *Término Trampa*, escribe tu justificación técnica y haz clic en **"Evaluar mi Razonamiento del Término Trampa"**.
3. **Revisión de Demostración (Pestaña 2):**  
   Analiza la matriz de **Las 5 C** frente a la **Metodología GREAC**. Revisa los canales de transmisión macroeconómica hacia la cartera de crédito.
4. **Resolución del Caso de Estudio (Pestaña 3):**  
   Lee el caso de **Banco Promotor S.A.** Responde a las tres preguntas analíticas y presiona **"Guardar y Evaluar Respuestas del Caso"** para recibir retroalimentación formativa de la IA.
5. **Laboratorio de Simulación (Pestaña 4):**  
   Ajusta los sliders de TPM y tipo de cambio. Observa cómo cambia la suficiencia patrimonial y la calificación regulatoria. Selecciona tu rol, elige una opción de política y redacta tu dictamen técnico. Haz clic en **"Emitir Dictamen Oficial de Simulación"**.
6. **Comprobación de Maestría y Descarga (Pestaña 5):**  
   Completa el reto del *Método Feynman* y responde a la *Pregunta Estratégica de Cierre*. Haz clic en **"Calificar Sesión y Generar Reporte Consolidado"**.  
   Una vez evaluado tu desempeño, presiona el botón **"📥 Descargar Reporte Consolidado (.md)"** para guardar tu archivo oficial y entregarlo en el campus virtual.

---

## 🧠 Interpretación Pedagógica de Resultados

### Indicadores Financieros de la Simulación
* **Tasa de Morosidad Proyectada (%):** Representa el porcentaje de la cartera en atraso mayor a 90 días. Aumentos en la TPM reducen el flujo neto libre del deudor, forzando la entrada en mora independientemente de que el crédito cuente con garantías reales.
* **Suficiencia Patrimonial Estimada (%):** Proporción del capital base del banco frente a sus activos ponderados por riesgo. El mínimo regulatorio en Costa Rica es de **10.0%**. Si el coeficiente cae por debajo de este umbral, el banco entra en causal de **Irregularidad Financiera (IRR1 a IRR3)**.
* **La Ilusión del Colateral:** Un banco no puede liquidar hipotecas para cubrir retiros diarios de depósitos en ventanilla. El proceso judicial de remate toma años y genera costos legales significativos. Por ende, **el colateral nunca reemplaza la capacidad de pago**.

### Rúbrica de Evaluación Cualitativa
El algoritmo de evaluación formativa examina cuatro dimensiones clave:
1. **Pensamiento Crítico y Discernimiento de Riesgo:** Capacidad de refutar la suficiencia de las garantías estáticas ante shocks macroeconómicos.
2. **Dominio Normativo SUGEF 24-22 (GREAC):** Manejo de los pilares de Gobierno Corporativo, Gestión de Riesgos y Capital Base.
3. **Aplicación del Modelo Morales Castro (5 C):** Reconocimiento del flujo de caja como fuente primaria y el colateral como fuente alterna.
4. **Responsabilidad Fiduciaria y Ética Financiera:** Comprensión de que los bancos administran recursos ajenos (depósitos de los ahorrantes) y tienen un deber de prudencia ante el riesgo sistémico.

---

## ⚖️ Licencia y Nota Educativa

### Declaración de Fines Exclusivamente Académicos
> **AVISO EDUCATIVO:**  
> Este software y sus contenidos asociados fueron diseñados de manera exclusiva con fines pedagógicos y de formación universitaria para los cursos de la **Escuela de Economía de la Universidad Internacional de las Américas (U.I.A.)**.  
> Los escenarios, entidades simuladas (ej. *Banco Promotor S.A.*) y ejercicios de simulación son modelos didácticos estructurados para estimular el pensamiento crítico de los estudiantes y no constituyen asesoría financiera, legal, auditoría oficial ni recomendaciones vinculantes de inversión.

### Licencia de Uso
Este proyecto se distribuye bajo la licencia **MIT** con fines educativos y de investigación académica. Se permite el uso, estudio y modificación del código fuente para actividades de enseñanza sin fines de lucro, manteniendo siempre el crédito a la Cátedra de Economía de la U.I.A. y a las fuentes bibliográficas citadas.
