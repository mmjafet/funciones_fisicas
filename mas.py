import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parámetros
A = 5       # Amplitud
omega = 2   # Frecuencia angular
phi = 0     # Fase inicial
t = np.linspace(0, 10, 100)  # Tiempo

# Crear la figura
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-A-1, A+1)
line, = ax.plot([], [], 'b', lw=2, label="x(t) = A cos(ωt + ϕ)")
ax.legend()

# Función de actualización de la animación
def update(frame):
    x = A * np.cos(omega * t + phi)
    line.set_data(t[:frame], x[:frame])
    return line,

# Crear animación
ani = animation.FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)
plt.show()
