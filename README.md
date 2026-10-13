# 🎓 Laboratorio de Pensamiento Crítico: Orientación del Crédito y Regulación de Usura
### Universidad Internacional de las Américas (U.I.A.)
**Escuela de Economía — Cátedra de Análisis de Crédito y Finanzas (ACF)**  
*Semana 4: Orientación del Crédito, Tasas Máximas y Usura en Costa Rica*

---

## 📖 1. Descripción General del Proyecto y Propósito

Este proyecto consiste en una aplicación web interactiva desarrollada en Python con **Streamlit**, diseñada con un enfoque de ingeniería de software educativo y didáctica universitaria para estudiantes de primer ingreso de la carrera de Economía.

El propósito fundamental de la plataforma es **estimular el pensamiento crítico genuino**, alejando al estudiantado de la memorización pasiva y la repetición ciega de fórmulas. La aplicación modela la tensión real existente entre las políticas microfinancieras de colocación comercial (manual de Morales Castro) y las restricciones macroprudenciales del Estado costarricense (Ley de Promoción de la Competencia N° 7472, Ley contra la Usura N° 9859, lineamientos del BCCR y normativa CONASSIF 14-21).

Bajo una arquitectura pedagógica basada en los **4 Principios de Instrucción de David Merrill** y la técnica de divulgación conceptual del **Método de Feynman**, la herramienta obliga al alumno a interpretar datos, evaluar riesgos de solvencia, defender decisiones crediticias en un comité simulado y prever las consecuencias no deseadas de la regulación de precios (como la exclusión financiera hacia prestamistas informales *'gota a gota'*).

---

## ✨ 2. Características Principales Implementadas

La plataforma articula un recorrido secuencial interactivo con control dinámico de estado (`st.session_state`):

1. **Identidad Visual UIA & Diseño Premium:**
   - Interfaz en *Dark Mode* profesional con contrastes en negro carbón (`#0B0F19`), azul marino institucional (`#1E3A8A`) y acentos en amarillo dorado (`#F5B700`), combinando con el logo oficial de la UIA.
   - Componentes estilo *glassmorphism*, métricas visuales y bloques de alerta socrática.

2. **Panel Lateral de Contexto y Gestión Estudiantil:**
   - Captura del nombre y carné del estudiante.
   - Resumen exhaustivo de fuentes normativas primarias (BCCR, CONASSIF, MEIC) y metodológicas.
   - Indicador de progreso acumulativo en tiempo real del *Mastery Check*.

3. **Módulo 1: Fase de Activación (Sondeo de Creencias y Sesgos):**
   - Pregunta detonante sobre el impacto real de los topes legales de tasa de interés en prestatarios vulnerables.
   - Ejercicio Feynman: Analogía del mercado de frutas o feria del agricultor para explicar la contracción de la oferta formal de crédito.
   - Retroalimentación formativa inmediata sin respuestas predeterminadas.

4. **Módulo 2: Fase de Demostración (Simulador Dinámico de Morales Castro & BCCR):**
   - Desglose cuantitativo del sobreprecio:
     $$\text{Sobreprecio} = \left(\frac{\text{Gastos Anuales Depto. Crédito}}{\text{Ventas Anuales a Crédito}}\right) + \text{Tasa de Interés Financiera}$$
   - Cálculo automático de cuotas, saldo insoluto y cobertura del umbral prudencial del 30% del gasto fijo sobre el ingreso.
   - Gráficos interactivos en **Plotly** contrastando la carga financiera del deudor contra el techo semestral de usura del BCCR.
   - Ejercicio Feynman: Distinción entre capacidad de pago cuantitativa (flujo de caja) y cualitativa (carácter y modelo de negocio).

5. **Módulo 3: Fase de Aplicación (Comité de Crédito Simulado & Prueba de Estrés):**
   - Resolución del caso práctico real: cliente con ₡100.000 de ingreso, endeudamiento previo del 38% y colateral de ₡3.000.000 (cobertura 15:1).
   - Toma de decisiones vinculante: Aprobación, Rechazo o Reestructuración mediante incremento del enganche.
   - Motor socrático: Alerta preventiva sobre la *"trampa del colateral"* bajo el **Acuerdo CONASSIF 14-21** (el crédito se repaga con flujos de caja operativos, no liquidando activos en juicio).

6. **Módulo 4: Fase de Integración (Foro de Crítica Cruzada y Defensa Viva):**
   - Refutación argumentada ante la tesis de fijar tasas arbitrarias al 10%.
   - Preparación de la defensa oral sincrónica de 2 minutos (*Mastery Viva*).
   - Pregunta estratégica de síntesis económica: impacto de aumentos en la Tasa de Política Monetaria (TPM) sobre la frontera de exclusión financiera.

7. **Módulo 5: Resumen & Portafolio de Evaluación:**
   - Consolidación de respuestas y puntaje acumulado (hasta 100 puntos).
   - **Botón único de exportación:** Descarga inmediata del informe consolidado en formato Markdown (`.md`) para el portafolio docente.

---

## 💻 3. Requisitos Técnicos

- **Sistema Operativo:** Windows 10/11, macOS, o Linux.
- **Versión de Python:** Python **3.10** o superior (probado y optimizado en Python 3.13).
- **Librerías Requeridas:**
  - `streamlit>=1.40.0`
  - `plotly>=5.20.0`
  - `pandas>=2.2.0`
  - `numpy>=2.0.0`
  - `pillow>=10.0.0`
  - `altair>=5.0.0`

---

## 🛠️ 4. Instrucciones de Instalación Paso a Paso

### Paso 1: Clonar el Repositorio
Abre tu terminal (PowerShell, Bash o CMD) y descarga el proyecto:
```bash
git clone https://github.com/randallnunezsancho-netizen/S4ACF.git
cd S4ACF
```

### Paso 2: Crear y Activar un Entorno Virtual (Recomendado)
- **En Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **En macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Paso 3: Instalar Dependencias
```bash
pip install -r S4ACF/requirements.txt
```

---

## 🚀 5. Guía de Uso con Ejemplos Básicos

### Ejecución Local del Servidor
Con el entorno virtual activado y ubicado en la carpeta del proyecto, ejecuta:
```bash
streamlit run S4ACF/app.py
```
El navegador se abrirá automáticamente en la dirección:
👉 `http://localhost:8501`

### Ejemplo de Flujo de Trabajo en Clase:
1. **Registro:** Introduce tu nombre completo y carné en la barra lateral.
2. **Activación:** Lee el dilema de partida de la Ley de Usura, selecciona tu hipótesis y describe la analogía del vendedor de feria en el recuadro Feynman.
3. **Simulación:** Ajusta los controles del simulador en la Fase 2:
   - *Ingreso:* ₡100.000
   - *Gastos Previos:* ₡38.000
   - *Enganche:* Desliza del 30% al 55% para observar cómo la cuota mensual disminuye y el ratio de gastos totales se sitúa por debajo del límite crítico.
4. **Comité:** Emite tu veredicto ante el caso de estudio y revisa el comentario que arroja el evaluador socrático según tu decisión.
5. **Descarga:** En la pestaña *"Resumen & Exportación"*, pulsa **"📥 Descargar Reporte Consolidado (.md)"** para guardar la evidencia de tu sesión sincrónica.

---

## 📂 6. Estructura del Proyecto

```text
S4ACF/
├── .gitignore                                           # Configuración de exclusión para Git
├── README.md                                            # Documentación técnica y pedagógica oficial
│
└── S4ACF/                                               # Directorio principal de la aplicación
    ├── app.py                                           # Código fuente integral en Streamlit
    ├── requirements.txt                                 # Dependencias del proyecto
    ├── Logo-oscuro- UIA.png                             # Logotipo institucional en tema oscuro
    ├── Especificacion de requisitos.md                  # Especificación de requisitos y marco pedagógico
    │
    ├── 1. Tasas y Leyes Financieras en tiempo real.pdf  # Ficha técnica de tasas BCCR y Ley 9859
    ├── 2. Ejercicio práctico_ Orientación del Crédito.pdf# Caso de estudio y consigna de comité
    ├── Credito y cobranzas [143-154].pdf                # Extracto Morales Castro Cap. 5
    ├── Planeamiento de lecturas ACF2026.pdf             # Programa temático y syllabus del curso
    ├── S4 - Ley 7472 Ley de promoción...pdf             # Texto normativo Ley 7472 / 9859
    ├── substack.com-Los 4 principios del diseño...pdf   # Fundamentos didácticos de David Merrill
    └── MasteryFlip-A_Guide_to_the_Future_of_Educcation.pdf # Metodología de clase invertida y Mastery Check
```

---

## 🧠 7. Interpretación de Resultados de Manera Pedagógica

| Métrica / Concepto | Umbral Normativo / Referencia | Interpretación Didáctica para el Estudiante de Economía |
| :--- | :--- | :--- |
| **Ratio de Gastos Fijos** | $\le 30\%$ del ingreso disponible | **Capacidad de Pago:** Morales Castro establece que comprometer más de un tercio de la renta fija en obligaciones recurrentes coloca al deudor en zona de insolvencia inminente frente a cualquier choque económico. |
| **Techo de Usura BCCR** | Ley 9859 (Art. 36 bis Ley 7472) | **Límite Legal:** Cobrar un sobreprecio superior a este tope anual constituye delito penal de usura. Si los costos de evaluar y colocar un crédito pequeño superan el techo, el banco debe rechazar la operación. |
| **Cobertura de Colateral** | Terreno ₡3.000.000 vs Crédito ₡200.000 | **Trampa de la Garantía (CONASSIF 14-21):** Un colateral no paga cuotas bancarias mes a mes. La ejecución judicial de garantías consume años y capital regulatorio; el criterio prudencial primordial siempre es el flujo de caja disponible. |
| **Tasa de Política Monetaria (TPM)** | Canal de Transmisión BCCR | Al endurecerse la política monetaria para frenar la inflación, se encarece el costo de captación de los bancos, comprimiendo el margen permitido por la ley de usura y expulsando a prestatarios de menores ingresos hacia la informalidad. |

---

## 📜 8. Licencia y Nota Educativa

### ⚠️ Nota Educativa e Institucional
> Este software y sus materiales anexos han sido creados exclusivamente con **fines académicos y pedagógicos** para la Cátedra de Análisis de Crédito y Finanzas de la Universidad Internacional de las Américas (U.I.A.).  
> Las simulaciones, parámetros y casos prácticos tienen propósito de entrenamiento analítico y no constituyen asesoría crediticia, contractual ni legal en el ejercicio financiero profesional.

### 📄 Licencia
Este proyecto se distribuye bajo la licencia **MIT**, permitiendo su uso, estudio y adaptación con fines formativos y de investigación académica.
