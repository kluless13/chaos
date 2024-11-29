import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
sigma = 10.0
beta = 8.0 / 3.0
rho = 28.0

# Lorenz system equations
def lorenz(state, t):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Time points
t = np.linspace(0, 25, 10000)

# Initial conditions
state0 = [1.0, 1.0, 1.0]

# Solve ODE
states = odeint(lorenz, state0, t)

# Setting up the figure and 3D axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection='3d')

# Initialize lines for the attractor
line, = ax.plot([], [], [], lw=0.8)

# Initialize the axis limits
ax.set_xlim((-30, 30))
ax.set_ylim((-30, 30))
ax.set_zlim((0, 50))
ax.set_title('Lorenz Attractor (Animated)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Function to update the plot
def update(num):
    line.set_data(states[:num, 0], states[:num, 1])
    line.set_3d_properties(states[:num, 2])
    return line,

# Animation
ani = FuncAnimation(fig, update, frames=range(1, len(states), 100), interval=20, blit=True)

plt.show()
