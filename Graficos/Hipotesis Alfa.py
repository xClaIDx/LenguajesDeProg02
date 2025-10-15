import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# 1. Parámetros de la prueba de hipótesis
df = 15  # Grados de libertad (n-2)
alpha_sig = 0.05  # Nivel de significancia
t_calc = -12.60  # Estadístico t calculado

# 2. Encontrar el valor crítico
# Usamos ppf (Percent Point Function), que es la inversa de la cdf
t_crit = stats.t.ppf(1 - alpha_sig, df)

# 3. Preparar los datos para la curva de distribución
# Creamos un rango de valores en el eje x para graficar la curva
x = np.linspace(-15, 15, 400)
# Calculamos los valores y correspondientes usando la Probability Density Function (PDF)
y = stats.t.pdf(x, df)

# 4. Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f'Distribución t (gl={df})')

# 5. Sombrear la zona de rechazo
# Creamos un rango de x solo para la zona de rechazo
x_rejection = np.linspace(t_crit, 15, 100)
y_rejection = stats.t.pdf(x_rejection, df)
plt.fill_between(x_rejection, y_rejection, color='red', alpha=0.5, label=f'Zona de Rechazo (α = {alpha_sig})')

# 6. Añadir líneas y anotaciones
plt.axvline(t_crit, color='red', linestyle='--', label=f'Valor Crítico = {t_crit:.3f}')
plt.axvline(t_calc, color='green', linestyle='-', lw=2, label=f't calculado = {t_calc:.2f}')
# Se añade una flecha y texto para mayor claridad
plt.annotate(f't = {t_calc}', 
             xy=(t_calc, 0.05), 
             xytext=(-10, 0.15),
             arrowprops=dict(facecolor='green', shrink=0.05),
             fontsize=12,
             color='green')


# 7. Añadir títulos y etiquetas
plt.title('Prueba de Hipótesis para el Intercepto (α)')
plt.xlabel('Valor t')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.grid(True)

# 8. Mostrar el gráfico
plt.show()
