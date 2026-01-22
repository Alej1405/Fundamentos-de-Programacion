import matplotlib.pyplot as plt
import numpy as np

# Datos inventados: Calificaciones de estudiantes por mes
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
calificaciones = [7.5, 8.2, 7.9, 8.5, 8.8, 9.1]
estudiantes = [15, 18, 16, 19, 21, 22]

# Crear figura con dos subgráficas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Gráfica 1: Línea - Evolución de calificaciones
ax1.plot(meses, calificaciones, marker='o', color='blue', linewidth=2, markersize=8)
ax1.set_title('Evolución de Calificaciones por Mes', fontsize=14, fontweight='bold')
ax1.set_xlabel('Mes', fontsize=12)
ax1.set_ylabel('Calificación Promedio', fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.set_ylim(7, 10)

# Gráfica 2: Barras - Cantidad de estudiantes
colores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F']
ax2.bar(meses, estudiantes, color=colores, alpha=0.7, edgecolor='black')
ax2.set_title('Cantidad de Estudiantes por Mes', fontsize=14, fontweight='bold')
ax2.set_xlabel('Mes', fontsize=12)
ax2.set_ylabel('Número de Estudiantes', fontsize=12)
ax2.grid(True, alpha=0.3, axis='y')

# Ajustar el espaciado
plt.tight_layout()

# Mostrar la gráfica
plt.show()