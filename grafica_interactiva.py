import numpy as np
import matplotlib.pyplot as plt

# 1. Parámetros obtenidos del modelo MLE
beta = 1.57392
eta = 726.378
t_propuesto = 110.05
t_actual = 365.0

# 2. Definición de la Función de Confiabilidad R(t) usando NumPy
def reliability(t, beta, eta):
    return np.exp(-(t / eta)**beta)

# 3. Creación del vector de tiempo (de 0 a 1000 días para ver el ciclo completo)
t_espacio = np.linspace(0, 1000, 500)
r_valores = reliability(t_espacio, beta, eta)

# 4. Cálculo de puntos críticos
r_propuesto = reliability(t_propuesto, beta, eta) # Debería ser ~0.95
r_actual = reliability(t_actual, beta, eta)       # Riesgo actual

# 5. Generación de la Gráfica
plt.figure(figsize=(10, 6))
plt.plot(t_espacio, r_valores, label='Modelo Weibull (MLE)', color='blue', lw=2)

# Línea de referencia R=0.95 (Tu objetivo)
plt.axhline(y=0.95, color='green', linestyle='--', alpha=0.6)
plt.axvline(x=t_propuesto, color='green', linestyle='--', label=f'Propuesto: {t_propuesto:.1f} días (R=95%)')

# Línea de referencia Intervalo Actual (365 días)
plt.axvline(x=t_actual, color='red', linestyle=':', label=f'Actual: {t_actual} días (R={r_actual*100:.1f}%)')

# Estética y Etiquetas para la Tesis
plt.title('Curva de Confiabilidad R(t) - Controladores de Temperatura', fontsize=14)
plt.xlabel('Tiempo de Operación (Días)', fontsize=12)
plt.ylabel('Confiabilidad R(t)', fontsize=12)
plt.ylim(0, 1.05)
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.legend()

# Mostrar resultados numéricos en consola también
print(f"--- Análisis Comparativo ---")
print(f"Confiabilidad a 365 días (Actual): {r_actual*100:.2f}%")
print(f"Confiabilidad a 110 días (Propuesta): {r_propuesto*100:.2f}%")
print(f"Delta de Riesgo mitigado: {(r_propuesto - r_actual)*100:.2f}%")

plt.show()