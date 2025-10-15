import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# 1. Parámetros de la prueba de hipótesis
df = 15  # Grados de libertad (n-2)
alpha_sig = 0.05  # Nivel de significancia
t_calc = 54.27  # Estadístico t calculado

# 2. Encontrar el valor crítico para una prueba de cola derecha
t_crit = stats.t.ppf(1 - alpha_sig, df)

# 3. Preparar los datos para la curva de distribución
# Graficamos un rango estándar para ver la forma de la distribución
x = np.linspace(-5, 5, 500)
y = stats.t.pdf(x, df)

# 4. Crear el gráfico
plt.figure(figsize=(12, 7))
plt.plot(x, y, label=f'Distribución t (gl={df})')

# 5. Sombrear la zona de rechazo
x_rejection = np.linspace(t_crit, 5, 100)
y_rejection = stats.t.pdf(x_rejection, df)
plt.fill_between(x_rejection, y_rejection, color='red', alpha=0.5, label=f'Zona de Rechazo (α = {alpha_sig})')

# 6. Añadir línea para el valor crítico
plt.axvline(t_crit, color='red', linestyle='--', label=f'Valor Crítico = {t_crit:.3f}')

# 7. Anotar el valor t calculado (que está fuera de escala)
plt.annotate(f't calculado = {t_calc}\n(Muy lejos en esta dirección)', 
             xy=(4.5, 0.02), 
             xytext=(0, 0.15),
             arrowprops=dict(facecolor='green', shrink=0.05, width=2, headwidth=8),
             fontsize=12,
             color='green',
             ha='center')

# 8. Añadir títulos y etiquetas
plt.title('Prueba de Hipótesis para la Pendiente (β)')
plt.xlabel('Valor t')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.grid(True)
plt.ylim(bottom=0)

# 9. Mostrar el gráfico
plt.show()