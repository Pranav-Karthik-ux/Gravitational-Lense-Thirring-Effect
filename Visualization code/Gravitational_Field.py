import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11
M = 5.972e24

# Polar grid
r = np.linspace(2, 10, 15)              # avoid r = 0
theta = np.linspace(0, 2*np.pi, 30)

R, T = np.meshgrid(r, theta)

# Convert to Cartesian positions
X = R * np.cos(T)
Y = R * np.sin(T)

# Gravitational field magnitude
g = -G*M/ R**2

# Field components
gx = g * np.cos(T)
gy = g * np.sin(T)

# Rescale for visualization
gx /= np.max(np.abs(gx))
gy /= np.max(np.abs(gy))


# Plot
plt.figure(figsize=(6,6))
plt.quiver(X, Y, gx, gy)
plt.scatter(0, 0)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gravitational Field (Quiver Plot)")
plt.axis("equal")
plt.grid('on')
plt.show()
