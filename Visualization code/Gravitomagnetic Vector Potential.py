import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

G = 1.0
S = np.array([0, 0, 1])

x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)
z = np.linspace(-5, 5, 10)

X, Y, Z = np.meshgrid(x, y, z)

R = np.sqrt(X**2 + Y**2 + Z**2)
R[R == 0] = 1e-6

Bx = S[1]*Z - S[2]*Y
By = S[2]*X - S[0]*Z
Bz = S[0]*Y - S[1]*X

Bx = (2*G / R**3) * Bx
By = (2*G / R**3) * By
Bz = (2*G / R**3) * Bz

# Raw magnitude (before normalization) — this is what we colour by
magnitude = np.sqrt(Bx**2 + By**2 + Bz**2).ravel()

# Flatten
x_f  = X.ravel();  y_f  = Y.ravel();  z_f  = Z.ravel()
bx_f = Bx.ravel(); by_f = By.ravel(); bz_f = Bz.ravel()

# Normalise directions
nm = np.sqrt(bx_f**2 + by_f**2 + bz_f**2)
nm[nm == 0] = 1
bx_n = bx_f / nm
by_n = by_f / nm
bz_n = bz_f / nm

# Colour map: inferno (black → red → yellow → white)
cmap  = plt.cm.inferno
vmin, vmax = magnitude.min(), magnitude.max()
cnorm  = Normalize(vmin=vmin, vmax=vmax)
colors = cmap(cnorm(magnitude))

fig = plt.figure(figsize=(9, 8))
ax  = fig.add_subplot(111, projection='3d')

for xi, yi, zi, ux, uy, uz, col in zip(x_f, y_f, z_f,
                                        bx_n, by_n, bz_n, colors):
    ax.quiver(xi, yi, zi, ux, uy, uz,
              length=0.45, normalize=False,
              color=col, linewidth=0.7, arrow_length_ratio=0.3)

sm = ScalarMappable(cmap=cmap, norm=cnorm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, shrink=0.6, pad=0.1)
cbar.set_label(r'$|\boldsymbol{\beta}|$ magnitude', fontsize=11)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gravitational Vector Potential  β\n'
             r'$\boldsymbol{\beta} = \frac{2G}{r^3}(\mathbf{S} \times \hat{r})$',
             fontsize=11)

plt.tight_layout()
plt.show()
