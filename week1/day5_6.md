### **Day 5-6: Nonlinear Dynamics and Phase Space**

---

### **Topics**

#### **1. What are Nonlinear Equations?**
Nonlinear equations are mathematical expressions where the relationship between variables is not proportional or additive. Unlike linear equations, which form straight lines, nonlinear equations describe curves, oscillations, and complex behaviors.

- **Linear System**: \( y = mx + c \)
  - Straightforward and proportional.
  - Small changes in input lead to predictable, proportional changes in output.

- **Nonlinear System**: \( y = ax^2 + bx + c \) or \( dx/dt = \sin(x) \)
  - Can include powers, exponential terms, trigonometric functions, or products of variables.
  - Small changes in input can lead to disproportionately large and unpredictable outputs.

---

#### **2. Nonlinear Dynamics**
Nonlinear dynamics is the study of systems governed by nonlinear equations. These systems often exhibit:

- **Oscillations**: Periodic or quasi-periodic motions.
- **Chaos**: Apparent randomness in deterministic systems.
- **Bifurcations**: Sudden changes in system behavior as parameters vary.

**Examples of Nonlinear Systems**:
- Weather systems (e.g., Lorenz attractor).
- Population growth (e.g., logistic map).
- Electrical circuits with feedback (e.g., Chua’s circuit).

---

#### **3. Phase Space**
**Phase space** is a geometric representation of all possible states of a system. Each point in the space corresponds to a specific state of the system, defined by variables like position and momentum.

- **Axes in Phase Space**:
  - For a single variable: Axes represent the variable and its rate of change (\(x, dx/dt\)).
  - For multiple variables: Axes represent all state variables (e.g., \(x, y, z\)).

**Trajectories**:
- A system's evolution is represented as a trajectory through phase space.
- **Attractors**: Points, loops, or shapes to which trajectories converge (e.g., fixed points, limit cycles, or strange attractors).

**Key Insights**:
- **Fixed Points**: Points where the system doesn’t change.
- **Stability**: Whether trajectories remain near or diverge from fixed points.

---

### **Activity: Plot Phase Space Diagrams**

#### **1. Simple Example: Pendulum Phase Space**

A pendulum's dynamics are governed by:
\[ \frac{d^2\theta}{dt^2} + \frac{g}{l} \sin(\theta) = 0 \]
Where:
- \( \theta \): Angular displacement.
- \( g \): Acceleration due to gravity.
- \( l \): Length of the pendulum.

We’ll visualize its phase space (\( \theta \) vs. \( d\theta/dt \)).

---

#### **Python Code for Phase Space of a Pendulum**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

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
initial_conditions = [
    [np.pi / 4, 0],  # Small displacement
    [np.pi / 2, 0],  # Larger displacement
    [np.pi, 0.5]     # Displacement and angular velocity
]

# Solve ODE and plot phase space
plt.figure(figsize=(8, 6))
for state0 in initial_conditions:
    states = odeint(pendulum, state0, t, args=(g, l, b))
    plt.plot(states[:, 0], states[:, 1], label=f'IC: {state0}')

# Customize plot
plt.title("Phase Space of a Damped Pendulum")
plt.xlabel("Angular Displacement (θ)")
plt.ylabel("Angular Velocity (dθ/dt)")
plt.grid()
plt.legend()
plt.show()
```

---

#### **2. Double Pendulum: Complex Nonlinear Dynamics**

The double pendulum exhibits chaotic motion. Its phase space is far more intricate, and you can plot it similarly by solving its coupled differential equations.

---

### **Reading Recommendations**

#### **Book**:
- **"Nonlinear Dynamics and Chaos" by Steven Strogatz**
  - **Why It’s Great**:
    - Explains nonlinear systems intuitively.
    - Covers topics like phase portraits, bifurcations, and chaos.
  - **Chapters to Start With**:
    - Chapter 1: Introduction to Nonlinear Dynamics.
    - Chapter 2: Phase Plane Analysis.

#### **Articles**:
- **"Introduction to Phase Space"** by Scholarpedia:
  - Explains phase space concepts with examples.
  - [Read here](http://www.scholarpedia.org/article/Phase_space)

- **"Nonlinear Dynamics in Real-World Systems"** by Physics Today:
  - Discusses applications in physics, engineering, and biology.
  - [Read here](https://physicstoday.scitation.org)

---

### **Learning Objectives for Day 5-6**
1. **Understand Nonlinearity**:
   - Grasp the behavior of nonlinear systems and how they differ from linear systems.
2. **Visualize Phase Space**:
   - Use Python to plot phase portraits for simple systems.
3. **Explore Applications**:
   - Reflect on how phase space and nonlinear dynamics apply to real-world problems.

---