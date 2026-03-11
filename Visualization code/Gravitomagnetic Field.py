import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

G = 1.0
S = np.array([0.0, 0.0, 1.0])

r     = np.linspace(1, 5, 6)
theta = np.linspace(0, np.pi, 12)
phi   = np.linspace(0, 2*np.pi, 12)

R, TH, PH = np.meshgrid(r, theta, phi)

X = R * np.sin(TH) * np.cos(PH)
Y = R * np.sin(TH) * np.sin(PH)
Z = R * np.cos(TH)

rx = X / R
ry = Y / R
rz = Z / R

Sdotr = S[0]*rx + S[1]*ry + S[2]*rz

Hx = (2*G / R**3) * (3*Sdotr*rx - S[0])
Hy = (2*G / R**3) * (3*Sdotr*ry - S[1])
Hz = (2*G / R**3) * (3*Sdotr*rz - S[2])

# Magnitude at each point
magnitude = np.sqrt(Hx**2 + Hy**2 + Hz**2)

# Flatten everything
x_f  = X.ravel();  y_f  = Y.ravel();  z_f  = Z.ravel()
hx_f = Hx.ravel(); hy_f = Hy.ravel(); hz_f = Hz.ravel()
mag  = magnitude.ravel()

# Normalize directions (keep arrows same length; color encodes magnitude)
norm_mag = np.sqrt(hx_f**2 + hy_f**2 + hz_f**2)
norm_mag[norm_mag == 0] = 1
hx_n = hx_f / norm_mag
hy_n = hy_f / norm_mag
hz_n = hz_f / norm_mag

# Map magnitude → colour (hot colormap: black-red-yellow-white)
cmap = plt.cm.plasma
vmin, vmax = mag.min(), mag.max()
cnorm = Normalize(vmin=vmin, vmax=vmax)
colors = cmap(cnorm(mag))   # (N, 4) RGBA array

fig = plt.figure(figsize=(9, 8))
ax  = fig.add_subplot(111, projection='3d')

# Draw each arrow individually so it can carry its own colour
for xi, yi, zi, ux, uy, uz, col in zip(x_f, y_f, z_f,
                                        hx_n, hy_n, hz_n, colors):
    ax.quiver(xi, yi, zi, ux, uy, uz,
              length=0.45, normalize=False,
              color=col, linewidth=0.8, arrow_length_ratio=0.3)

# Colourbar
sm = ScalarMappable(cmap=cmap, norm=cnorm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, shrink=0.6, pad=0.1)
cbar.set_label(r'$|\mathbf{H}|$ magnitude', fontsize=11)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gravitomagnetic Field  H\n'
             r'$\mathbf{H} = \frac{2G}{r^3}[3(\mathbf{S}\cdot\hat{r})\hat{r} - \mathbf{S}]$',
             fontsize=11)

plt.tight_layout()
plt.show()
