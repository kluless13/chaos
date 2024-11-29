import numpy as np
import matplotlib.pyplot as plt

# Logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Generate data for the map
def generate_logistic_map(r, x0, n):
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, n):
        x[i] = logistic_map(r, x[i-1])
    return x

# Parameters
r_values = [2.5, 3.2, 3.5, 3.9]  # Different growth rates
x0 = 0.5  # Initial population
n = 100  # Number of iterations

# Plotting
plt.figure(figsize=(12, 8))
for r in r_values:
    x = generate_logistic_map(r, x0, n)
    plt.plot(range(n), x, label=f'r = {r}')

plt.title('Logistic Map for Different Growth Rates')
plt.xlabel('Iteration (n)')
plt.ylabel('Population (x)')
plt.legend()
plt.grid()
plt.show()
