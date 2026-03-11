import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11
M = 5.972e24

r = np.linspace(1e6, 1e8, 500)

V = -G * M / r

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(r, V, label=r'$V(r) = -\dfrac{GM}{r}$', linewidth=2, color='green')

ax.set_xlabel("Distance r (m)", fontsize=11)
ax.set_ylabel("Gravitational Potential V (J/kg)", fontsize=11)
ax.set_title("Gravitational Potential vs Distance", fontsize=13)
ax.legend(fontsize=13)
ax.grid(True)

plt.tight_layout()
plt.show()
