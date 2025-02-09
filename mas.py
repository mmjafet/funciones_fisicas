import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parámetros
A = 5       # Amplitud
omega = 2   # Frecuencia angular
phi = 0     # Fase inicial
t = np.linspace(0, 10, 100)  # Tiempo

# Crear la figura
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-A - 1, A + 1)
ax.set_ylim(-A - 1, A + 1)
ax.set_xticks([])
ax.set_yticks([])

# Dibujar el resorte y la masa
line, = ax.plot([], [], 'b', lw=2)  # Línea que representa la trayectoria
mass, = ax.plot([], [], 'ro', markersize=10)  # Masa del péndulo

# Dibujar un resorte estilizado
def draw_spring(x):
    y = np.linspace(-A, x, 10)
    x_spring = np.sin(np.linspace(0, 4 * np.pi, len(y))) * 0.5
    return x_spring, y

spring_x, spring_y = draw_spring(A)
spring_line, = ax.plot(spring_x, spring_y, 'k', lw=2)

# Función de actualización de la animación
def update(frame):
    x_pos = A * np.cos(omega * t[frame] + phi)  # Posición de la masa
    mass.set_data(0, x_pos)  # Actualizar la posición de la masa
    line.set_data([0, 0], [-A, x_pos])  # Línea del resorte
    spring_x, spring_y = draw_spring(x_pos)  # Dibujar el resorte estirado
    spring_line.set_data(spring_x, spring_y)
    return mass, line, spring_line

# Crear animación
ani = animation.FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)
plt.show()
