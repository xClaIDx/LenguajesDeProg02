import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# ================================
# 1️⃣ Datos originales
# ================================
placebo = np.array([6, 8, 4, 8, 5, 6, 5, 6, 4, 5])
tratamiento = np.array([5, 6, 4, 5, 3, 6, 6, 2, 2, 6])

# ================================
# 2️⃣ Cálculo de diferencias
# ================================
d = placebo - tratamiento
n = len(d)
df = n - 1

# Estadísticos
d_mean = d.mean()
s_d = d.std(ddof=1)
t_calc = d_mean / (s_d / np.sqrt(n))

# Nivel de significancia (cola derecha)
alpha = 0.05
t_crit = t.ppf(1 - alpha, df)
p_value_one_sided = t.sf(t_calc, df)

# ================================
# 3️⃣ Gráfico de distribución t
# ================================
x = np.linspace(-4, 4, 1000)
y = t.pdf(x, df)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f'Distribución t (df={df})', color='blue')

# Zona no rechazo
plt.fill_between(x, y, 0, where=(x < t_crit), color='lightblue', alpha=0.5, label='No rechazo H₀')

# Zona rechazo
plt.fill_between(x, y, 0, where=(x >= t_crit), color='salmon', alpha=0.6, label='Zona de rechazo H₀')

# Líneas verticales
plt.axvline(t_crit, color='red', linestyle='--', linewidth=2, label=f't crítico = {t_crit:.3f}')
plt.axvline(t_calc, color='green', linestyle='--', linewidth=2, label=f't calculado = {t_calc:.3f}')

# ================================
# 4️⃣ Personalizar gráfico
# ================================
plt.title(f'Prueba t unilateral (cola derecha)\n'
          f't_calc = {t_calc:.3f}  |  p = {p_value_one_sided:.4f}')
plt.xlabel('t')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# ================================
# 5️⃣ Mostrar resultados numéricos
# ================================
print("📊 RESULTADOS DE LA PRUEBA T (UNILATERAL):")
print(f"Media de diferencias: {d_mean:.3f}")
print(f"Desviación estándar: {s_d:.3f}")
print(f"t calculado: {t_calc:.3f}")
print(f"t crítico (α = 0.05): {t_crit:.3f}")
print(f"p-valor (one-sided): {p_value_one_sided:.4f}")

# Conclusión
if t_calc > t_crit:
    print("\n✅ Se rechaza H₀: El tratamiento reduce significativamente el eczema.")
else:
    print("\n❌ No se rechaza H₀: No hay evidencia suficiente de mejora.")