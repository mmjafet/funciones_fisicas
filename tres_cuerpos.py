import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Constante gravitacional universal
G = 1  # Para simplificar, usamos G = 1 en unidades arbitrarias

# Definir las masas y condiciones iniciales (posición y velocidad)
m1, m2, m3 = 1.0, 1.0, 1.0
r1 = np.array([-1.0, 0.0])  # Posición inicial del cuerpo 1
r2 = np.array([1.0, 0.0])   # Posición inicial del cuerpo 2
r3 = np.array([0.0, 1.0])   # Posición inicial del cuerpo 3

v1 = np.array([0.0, -0.5])  # Velocidad inicial del cuerpo 1
v2 = np.array([0.0, 0.5])   # Velocidad inicial del cuerpo 2
v3 = np.array([0.5, 0.0])   # Velocidad inicial del cuerpo 3

# Función para calcular las derivadas
def derivs(t, y):
    r1, r2, r3, v1, v2, v3 = y[:2], y[2:4], y[4:6], y[6:8], y[8:10], y[10:12]
    
    def accel(rA, rB, rC, mB, mC):
        rAB = rB - rA
        rAC = rC - rA
        a = G * mB * rAB / np.linalg.norm(rAB)**3 + G * mC * rAC / np.linalg.norm(rAC)**3
        return a
    
    a1 = accel(r1, r2, r3, m2, m3)
    a2 = accel(r2, r1, r3, m1, m3)
    a3 = accel(r3, r1, r2, m1, m2)
    
    return np.concatenate([v1, v2, v3, a1, a2, a3])

# Resolver ecuaciones de movimiento
y0 = np.concatenate([r1, r2, r3, v1, v2, v3])
t_span = (0, 10)
t_eval = np.linspace(0, 10, 500)
sol = solve_ivp(derivs, t_span, y0, t_eval=t_eval)

# Extraer las trayectorias
x1, y1 = sol.y[0], sol.y[1]
x2, y2 = sol.y[2], sol.y[3]
x3, y3 = sol.y[4], sol.y[5]

# Animación
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Simulación del Problema de los 3 Cuerpos")

line1, = ax.plot([], [], 'ro-', markersize=5, label='Cuerpo 1')
line2, = ax.plot([], [], 'go-', markersize=5, label='Cuerpo 2')
line3, = ax.plot([], [], 'bo-', markersize=5, label='Cuerpo 3')
trail1, = ax.plot([], [], 'r-', alpha=0.5)
trail2, = ax.plot([], [], 'g-', alpha=0.5)
trail3, = ax.plot([], [], 'b-', alpha=0.5)
ax.legend()

def update(frame):
    line1.set_data(x1[frame], y1[frame])
    line2.set_data(x2[frame], y2[frame])
    line3.set_data(x3[frame], y3[frame])
    trail1.set_data(x1[:frame], y1[:frame])
    trail2.set_data(x2[:frame], y2[:frame])
    trail3.set_data(x3[:frame], y3[:frame])
    return line1, line2, line3, trail1, trail2, trail3

ani = FuncAnimation(fig, update, frames=len(t_eval), interval=20, blit=True)
plt.show()
