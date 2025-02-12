import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Parámetros iniciales
g = 9.81  # Aceleración debida a la gravedad (m/s^2)
v_avion = 100  # Velocidad del avión (m/s)
h = 1000  # Altura del avión (m)
d = 2000  # Distancia horizontal al objetivo (m)

# Calcular el tiempo de caída
t_caida = np.sqrt(2 * h / g)

# Calcular la distancia horizontal recorrida durante la caída
d_caida = v_avion * t_caida

# Calcular el tiempo total de vuelo
t_total = d / v_avion

# Calcular la posición inicial del objeto
x0 = 0
y0 = 0
z0 = h

# Calcular la velocidad inicial del objeto
vx0 = v_avion
vy0 = 0
vz0 = 0

# Función para calcular la posición del objeto en el tiempo t
def posicion(t):
    x = x0 + vx0 * t
    y = y0 + vy0 * t
    z = z0 - 0.5 * g * t**2
    return x, y, z

# Crear la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, d)
ax.set_ylim(-d/2, d/2)
ax.set_zlim(0, h)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Caída Parabólica desde un Avión")

# Crear la línea de la trayectoria
line, = ax.plot([], [], [], 'bo-', markersize=5, label='Objeto')
ax.legend()

# Función de actualización para la animación
def update(frame):
    t = frame * t_total / 100
    x, y, z = posicion(t)
    line.set_data([x0, x], [y0, y])
    line.set_3d_properties([z0, z])
    return line,

# Crear la animación
ani = FuncAnimation(fig, update, frames=100, interval=100, blit=True)
plt.show()