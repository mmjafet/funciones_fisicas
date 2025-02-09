import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parámetros del MAS
A = 5       # Amplitud
omega = 2   # Frecuencia angular
phi = 0     # Fase inicial
num_coils = 15  # Número de espiras del resorte
t = np.linspace(0, 10, 100)  # Tiempo

# Crear la figura
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-A - 1, A + 1)
ax.set_ylim(-A - 1, A + 1)
ax.set_xticks([])
ax.set_yticks([])

# Dibujar la masa
mass, = ax.plot([], [], 'ro', markersize=10)  # Masa del péndulo

# Función para dibujar un resorte realista
def draw_spring(y_start, y_end, num_coils=15):
    """Dibuja un resorte entre y_start y y_end con una cantidad específica de espiras."""
    num_points = 100
    y = np.linspace(y_start, y_end, num_points)
    
    # Estructura del resorte con espiras
    x_spring = 0.3 * np.sin(np.linspace(0, num_coils * 2 * np.pi, num_points))
    
    return x_spring, y

# Línea inicial del resorte
spring_x, spring_y = draw_spring(-A, A, num_coils)
spring_line, = ax.plot(spring_x, spring_y, 'k', lw=2)

# Mostrar ecuación y valores dinámicos
eq_text = ax.text(-A, A, r"$x(t) = A \cos(\omega t + \phi)$", fontsize=12, color='black')
val_text = ax.text(-A, A - 1, "", fontsize=12, color='red')

# Función de actualización de la animación
def update(frame):
    x_pos = A * np.cos(omega * t[frame] + phi)  # Posición de la masa
    mass.set_data([0], [x_pos])  # Posición de la masa

    # Dibujar resorte con nueva posición
    spring_x, spring_y = draw_spring(-A, x_pos, num_coils)
    spring_line.set_data(spring_x, spring_y)

    # Actualizar el texto de valores
    val_text.set_text(f"x(t) = {x_pos:.2f} m")
    
    return mass, spring_line, val_text

# Crear animación
ani = animation.FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)

plt.show()
