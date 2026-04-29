import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from reliability.Fitters import Fit_Weibull_2P

# ==========================================
# 1. CONFIGURACIÓN DE RUTA
# ==========================================
# Asegúrate de que esta ruta apunte correctamente a tu archivo Excel
ruta = "../../data_drive/TesisII_R2/Fuentes_H_Calculo/SF-TTP-MTBF.xlsx"

print("--- Ejecutando Motor de Confiabilidad Weibull (MLE) ---")

try:
    # ==========================================
    # 2. CARGA Y LIMPIEZA DE DATOS
    # ==========================================
    df = pd.read_excel(ruta, engine='openpyxl')
    
    # Filtramos para tener solo intervalos con historial previo
    df_clean = df.dropna(subset=['Sum of Days_Since_Prev_Calibration']).copy()
    
    tiempos = df_clean['Sum of Days_Since_Prev_Calibration'].astype(float).values
    eventos = df_clean['SF_TTP'].astype(int).values
    
    fallas = tiempos[eventos == 1]
    censuras = tiempos[eventos == 0]

    # Preparamos la figura para el primer gráfico
    plt.figure(figsize=(8, 6))

    # ==========================================
    # 3. AJUSTE DEL MODELO (MLE)
    # ==========================================
    # show_probability_plot=True genera automáticamente la primera gráfica
    model = Fit_Weibull_2P(failures=fallas, right_censored=censuras, print_results=True, show_probability_plot=True)
    
    # ==========================================
    # 4. CÁLCULO DE INTERVALOS ÓPTIMOS
    # ==========================================
    t_95 = model.distribution.quantile(0.05) # 95% Confiabilidad (Life Science)
    t_85 = model.distribution.quantile(0.15) # 85% Confiabilidad (Estándar RP-1)
    
    # --- Impresión de Resultados en Consola ---
    print("\n" + "="*60)
    print(" RESUMEN TÉCNICO PARA CAPÍTULO 5 ".center(60, "="))
    print(f"Parámetro Beta (β): {model.beta:.5f}")
    print(f"Parámetro Alpha (η): {model.alpha:.3f} días")
    print(f"Log-Likelihood: {model.loglik:.2f}")
    print(f"Intervalo Optimizado (Confiabilidad 95%): {t_95:.2f} días")
    print(f"Intervalo Optimizado (Confiabilidad 85%): {t_85:.2f} días (Estándar RP-1)")
    print("="*60)

    # ==========================================
    # 5. VISUALIZACIÓN DE GRÁFICAS PARA TESIS
    # ==========================================
    
    # --- Gráfica 1: Gráfico de Probabilidad (Probability Plot) ---
    plt.title('Gráfico de Probabilidad de Weibull (MLE)')
    # IMPORTANTE: Al ejecutar, debes cerrar esta ventana emergente para ver la siguiente gráfica.
    plt.show() 

    # --- Gráfica 2: Curva de Supervivencia R(t) ---
    plt.figure(figsize=(10, 6))
    
    # Dibujamos la curva principal azul
    model.distribution.SF(label='Curva de Supervivencia R(t)', color='blue', linewidth=2)
    
    # Dibujamos las líneas de la Meta 95% (Life Science)
    plt.axhline(y=0.95, color='red', linestyle='--', alpha=0.7)
    plt.axvline(x=t_95, color='red', linestyle='--', alpha=0.7, label=f'Meta 95% ({t_95:.1f} días)')
    
    # Dibujamos las líneas de la Meta 85% (Estándar RP-1)
    plt.axhline(y=0.85, color='green', linestyle='--', alpha=0.7)
    plt.axvline(x=t_85, color='green', linestyle='--', alpha=0.7, label=f'Estándar 85% ({t_85:.1f} días)')
    
    # Formato y estilo de la gráfica
    plt.title('Curva de Supervivencia y Objetivos de Confiabilidad')
    plt.xlabel('Tiempo entre calibraciones (Días)')
    plt.ylabel('Probabilidad de Supervivencia / Confiabilidad')
    plt.legend(loc='lower left')
    plt.grid(True, linestyle=':', alpha=0.6)
    
    # Mostramos la segunda gráfica
    plt.show()

except Exception as e:
    print(f"❌ Error al procesar: {e}")