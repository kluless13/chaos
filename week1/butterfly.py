import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

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

# Plotting
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(121, projection='3d')
ax.plot(states[:, 0], states[:, 1], states[:, 2])
ax.set_title('Lorenz Attractor')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Sensitivity to initial conditions
state1 = [1.0001, 1.0, 1.0]  # Slightly different initial condition
states1 = odeint(lorenz, state1, t)

# Plot the difference over time
ax2 = fig.add_subplot(122)
difference = np.sqrt(np.sum((states - states1)**2, axis=1))
ax2.plot(t, difference)
ax2.set_title('Divergence Over Time')
ax2.set_xlabel('Time')
ax2.set_ylabel('Difference')

plt.tight_layout()
plt.show()
