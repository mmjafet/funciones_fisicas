import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parámetros del MAS
A = 5        # Amplitud (máximo desplazamiento)
f = 0.5      # Frecuencia en Hz
omega = 2 * np.pi * f  # Frecuencia angular (rad/s)
phi = 0      # Fase inicial
num_coils = 15  # Número de espiras del resorte
t = np.linspace(0, 10, 200)  # Tiempo

# Crear la figura
fig, ax = plt.subplots(figsize=(7, 6))
ax.set_xlim(-A - 2, A + 2)
ax.set_ylim(-A - 2, A + 2)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Movimiento Armónico Simple (MAS)")

# Dibujar la masa
mass, = ax.plot([], [], 'ro', markersize=12)  # Masa roja

# Función para dibujar un resorte realista
def draw_spring(y_start, y_end, num_coils=15):
    """Dibuja un resorte entre y_start y y_end con espiras realistas."""
    num_points = 100
    y = np.linspace(y_start, y_end, num_points)
    x_spring = 0.3 * np.sin(np.linspace(0, num_coils * 2 * np.pi, num_points))
    return x_spring, y

# Línea inicial del resorte
spring_x, spring_y = draw_spring(-A, A, num_coils)
spring_line, = ax.plot(spring_x, spring_y, 'k', lw=2)

# Mostrar ecuación del MAS
eq_text = ax.text(-A - 1.5, A + 1, 
                  r"$x(t) = A \cos(\omega t + \phi)$", 
                  fontsize=14, color='black', bbox=dict(facecolor='white', alpha=0.8))

# Mostrar valores en tiempo real
val_text = ax.text(-A - 1.5, A - 1, "", fontsize=14, color='blue', bbox=dict(facecolor='white', alpha=0.8))

# Función de actualización de la animación
def update(frame):
    x_pos = A * np.cos(omega * t[frame] + phi)  # Posición de la masa
    mass.set_data([0], [x_pos])  # Posición de la masa

    # Dibujar resorte con nueva posición
    spring_x, spring_y = draw_spring(-A, x_pos, num_coils)
    spring_line.set_data(spring_x, spring_y)

    # Actualizar el texto con valores dinámicos
    val_text.set_text(f"x(t) = {x_pos:.2f} m")
    
    return mass, spring_line, val_text

# Crear animación
ani = animation.FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)

plt.show()
