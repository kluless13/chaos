import numpy as np
import matplotlib.pyplot as plt

# Parameters
r_values = np.linspace(2.5, 4.0, 1000)  # Growth rate range
n_iterations = 1000  # Total number of iterations
last_iterations = 100  # Number of iterations to plot (to focus on steady state)
x0 = 0.5  # Initial population value

# Prepare bifurcation data
x = np.ones_like(r_values) * x0  # Initialize populations for all r
bifurcation_data = []

for i in range(n_iterations):
    x = r_values * x * (1 - x)  # Logistic map equation
    if i >= (n_iterations - last_iterations):  # Only save last iterations
        bifurcation_data.append(np.column_stack((r_values, x)))

bifurcation_data = np.concatenate(bifurcation_data)  # Combine all data

# Plot bifurcation diagram
plt.figure(figsize=(10, 7))
plt.plot(bifurcation_data[:, 0], bifurcation_data[:, 1], ',k', alpha=0.25)  # ',' is for small dots
plt.title('Bifurcation Diagram of the Logistic Map')
plt.xlabel('Growth Rate (r)')
plt.ylabel('Population (x)')
plt.grid()
plt.show()
