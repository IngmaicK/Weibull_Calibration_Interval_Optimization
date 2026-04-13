# Optimización de Intervalos de Calibración Mediante el Modelo de Weibull

**Repositorio oficial del código fuente para tesis de Maestría.**
*Autor: Miguel Ramirez*

## 📌 Descripción del Proyecto
Este repositorio contiene los scripts desarrollados en Python para analizar la confiabilidad metrológica de controladores de temperatura en la industria de dispositivos médicos. Utiliza Análisis de Datos de Vida (Life Data Analysis) y Estimación por Máxima Verosimilitud (MLE) para calcular parámetros de degradación y proponer intervalos de calibración optimizados basados en riesgo.

## 🛠️ Archivos Principales
* `analisis_mle_interactive.ipynb`: Cuaderno principal con el cálculo de los parámetros de forma ($\beta$) y escala ($\eta$) de Weibull.
* `Curva_Supervivencia_Riesgo_Metrologico.ipynb`: Generación de la gráfica de confiabilidad $R(t)$ y cruce del umbral del 95% (110 días).
* `Probability_Plot_Weibull_CDF.ipynb`: Gráfico de probabilidad y validación de bondad de ajuste.

## 🚀 Tecnologías y Librerías
* Python 3.x
* Pandas (Procesamiento de datos)
* Reliability (Ajuste de distribuciones y MLE)
* Matplotlib / Seaborn (Visualización de datos)

## 📖 Cómo citar este trabajo
Si este código le resulta útil para investigaciones académicas o implementaciones industriales, por favor cite la tesis original:
> *[Ramirez], Miguel. (2026). Optimización de Intervalos de Calibración Mediante el Modelo de Weibull y Análisis de Confiabilidad en la Industria de Dispositivos Médicos. CETYS Universidad.*