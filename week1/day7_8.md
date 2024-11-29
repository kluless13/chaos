### **Day 7-8: Mathematical Foundations of Chaos**

---

### **Topics**

#### **1. Differential Equations**
Differential equations describe how a quantity changes over time or space. In chaos theory, they govern the behavior of dynamical systems and are used to model systems ranging from weather to population dynamics.

- **General Form**:
  \[
  \frac{dy}{dt} = f(y, t)
  \]
  Here, \(y\) is the dependent variable, \(t\) is the independent variable (often time), and \(f(y, t)\) is a function describing the rate of change.

- **Example: Logistic Growth**:
  \[
  \frac{dN}{dt} = rN(1 - \frac{N}{K})
  \]
  Where:
  - \(N\): Population size.
  - \(r\): Growth rate.
  - \(K\): Carrying capacity.

  This equation models population growth constrained by resources.

#### **2. Iteration**
Iteration involves repeatedly applying a function to its own output. It's a simple yet powerful way to generate chaotic behavior.

- **Example: Iterative Mapping**:
  \[
  x_{n+1} = f(x_n)
  \]
  Where \(f(x)\) is the function defining the system. Iteration is central to chaotic systems like the **logistic map**.

#### **3. Recursion**
Recursion is similar to iteration but uses self-referential definitions. It’s common in algorithmic and mathematical approaches to chaos.

- **Example: Recursive Logistic Map**:
  \[
  x_{n+1} = rx_n(1 - x_n)
  \]
  This defines each state \(x_{n+1}\) based on the previous state \(x_n\), creating the foundation for chaotic dynamics.

---

### **Activity: Solve Problems with the Logistic Map**

The **logistic map** models population growth in discrete time and exhibits chaos for certain parameter values.

**Equation**:
\[
x_{n+1} = rx_n(1 - x_n)
\]
Where:
- \(x_n\): Population size at step \(n\) (normalized to a range between 0 and 1).
- \(r\): Growth rate (parameter controlling behavior).

#### **Code Example: Visualizing the Logistic Map**

This code plots the dynamics of the logistic map for different values of \(r\):

```python
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
```

---

### **Interpretation**
1. **Behavior for Different \(r\)**:
   - \(r < 3\): Population stabilizes at a fixed point.
   - \(3 \leq r < 3.5\): Population oscillates between 2 values.
   - \(r > 3.5\): Chaotic behavior emerges with no apparent pattern.

2. **Bifurcations**:
   - As \(r\) increases, the system transitions from stability to chaos through bifurcations (splits in behavior).

#### **Advanced Activity: Plot the Bifurcation Diagram**

The bifurcation diagram shows how the logistic map behaves across a range of \(r\) values.

```python
# Parameters
r_values = np.linspace(2.5, 4.0, 1000)
n = 1000  # Number of iterations
last = 100  # Last iterations to plot
x0 = 0.5  # Initial value

# Generate bifurcation data
x = x0 * np.ones_like(r_values)
bifurcation = []

for i in range(n):
    x = r_values * x * (1 - x)
    if i >= (n - last):
        bifurcation.append(np.column_stack((r_values, x)))

bifurcation = np.concatenate(bifurcation)

# Plot bifurcation diagram
plt.figure(figsize=(10, 7))
plt.plot(bifurcation[:, 0], bifurcation[:, 1], ',k', alpha=0.25)
plt.title('Bifurcation Diagram of the Logistic Map')
plt.xlabel('Growth Rate (r)')
plt.ylabel('Population (x)')
plt.grid()
plt.show()
```

---

### **Reading Recommendations**

#### **Book**:
- **"Mathematical Models in Biology" by Leah Edelstein-Keshet**
  - **Chapters to Read**:
    - Population models and the logistic map.
    - Introduction to bifurcations and chaos.

#### **Articles**:
1. **"Chaos and Logistic Maps"** by Scholarpedia:
   - Explains the logistic map in detail and its relevance to chaos theory.
   - [Read here](http://www.scholarpedia.org/article/Logistic_map)

2. **"Bifurcation and Chaos in the Logistic Map"**:
   - Visual explanation of bifurcations leading to chaos.
   - [Read here](https://mathworld.wolfram.com/LogisticMap.html)

---

### **Learning Objectives**
1. Understand the mathematical tools that underpin chaos theory: differential equations, iteration, and recursion.
2. Explore the logistic map as a gateway to chaotic systems.
3. Develop hands-on skills by plotting and analyzing the behavior of the logistic map in Python.
