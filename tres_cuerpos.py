import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D

# Constante gravitacional universal
G = 1  # Para simplificar, usamos G = 1 en unidades arbitrarias

# Definir las masas y condiciones iniciales (posición y velocidad)
m1, m2, m3 = 1.0, 1.0, 1.0
r1 = np.array([-1.0, 0.0, 0.0])  # Posición inicial del cuerpo 1
r2 = np.array([1.0, 0.0, 0.0])   # Posición inicial del cuerpo 2
r3 = np.array([0.0, 1.0, 0.0])   # Posición inicial del cuerpo 3

v1 = np.array([0.0, -0.5, 0.1])  # Velocidad inicial del cuerpo 1
v2 = np.array([0.0, 0.5, -0.1])  # Velocidad inicial del cuerpo 2
v3 = np.array([0.5, 0.0, 0.0])   # Velocidad inicial del cuerpo 3

# Función para calcular las derivadas
def derivs(t, y):
    r1, r2, r3, v1, v2, v3 = y[:3], y[3:6], y[6:9], y[9:12], y[12:15], y[15:18]
    
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
x1, y1, z1 = sol.y[0], sol.y[1], sol.y[2]
x2, y2, z2 = sol.y[3], sol.y[4], sol.y[5]
x3, y3, z3 = sol.y[6], sol.y[7], sol.y[8]

# Animación
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Simulación del Problema de los 3 Cuerpos en 3D")

line1, = ax.plot([], [], [], 'ro-', markersize=5, label='Cuerpo 1')
line2, = ax.plot([], [], [], 'go-', markersize=5, label='Cuerpo 2')
line3, = ax.plot([], [], [], 'bo-', markersize=5, label='Cuerpo 3')
trail1, = ax.plot([], [], [], 'r-', alpha=0.5)
trail2, = ax.plot([], [], [], 'g-', alpha=0.5)
trail3, = ax.plot([], [], [], 'b-', alpha=0.5)
ax.legend()

# Añadir texto para mostrar la distancia entre los cuerpos
text = ax.text2D(0.05, 0.95, "", transform=ax.transAxes)

def update(frame):
    line1.set_data(x1[:frame], y1[:frame])
    line1.set_3d_properties(z1[:frame])
    line2.set_data(x2[:frame], y2[:frame])
    line2.set_3d_properties(z2[:frame])
    line3.set_data(x3[:frame], y3[:frame])
    line3.set_3d_properties(z3[:frame])
    trail1.set_data(x1[:frame], y1[:frame])
    trail1.set_3d_properties(z1[:frame])
    trail2.set_data(x2[:frame], y2[:frame])
    trail2.set_3d_properties(z2[:frame])
    trail3.set_data(x3[:frame], y3[:frame])
    trail3.set_3d_properties(z3[:frame])
    
    # Calcular las distancias entre los cuerpos
    d12 = np.linalg.norm([x1[frame] - x2[frame], y1[frame] - y2[frame], z1[frame] - z2[frame]])
    d13 = np.linalg.norm([x1[frame] - x3[frame], y1[frame] - y3[frame], z1[frame] - z3[frame]])
    d23 = np.linalg.norm([x2[frame] - x3[frame], y2[frame] - y3[frame], z2[frame] - z3[frame]])
    
    # Actualizar el texto con las distancias
    text.set_text(f'Distancias:\nCuerpo 1-2: {d12:.2f}\nCuerpo 1-3: {d13:.2f}\nCuerpo 2-3: {d23:.2f}')
    
    return line1, line2, line3, trail1, trail2, trail3, text

ani = FuncAnimation(fig, update, frames=len(t_eval), interval=20, blit=True)
plt.show()