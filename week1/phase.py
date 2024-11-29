import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

# Parameters
g = 9.81  # Gravity
l = 1.0   # Length of the pendulum
b = 0.2   # Damping coefficient

# Pendulum equations
def pendulum(state, t, g, l, b):
    theta, omega = state
    dtheta_dt = omega
    domega_dt = -(b * omega) - (g / l) * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Time points
t = np.linspace(0, 20, 1000)

# Initial conditions
state0 = [np.pi / 4, 0]  # Small displacement

# Solve ODE
states = odeint(pendulum, state0, t, args=(g, l, b))

# Setup the figure
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Animated Phase Space of a Damped Pendulum")
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-5, 5)
ax.set_xlabel("Angular Displacement (θ)")
ax.set_ylabel("Angular Velocity (dθ/dt)")
ax.grid()

# Initialize line
line, = ax.plot([], [], lw=2)

# Initialize the animation
def init():
    line.set_data([], [])
    return line,

# Update function for animation
def update(frame):
    line.set_data(states[:frame, 0], states[:frame, 1])
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=20)

plt.show()
