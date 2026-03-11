import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# Constants (normalized)
G = 1.0
M = 1.0
S = np.array([0.0, 0.0, 1.0])   # spin along z
a = 5.0                           # orbital radius
i = np.radians(30)                # inclination from equatorial plane

# ── Orbit: parametric position & velocity ───────────────────────────────────
N = 40
phi = np.linspace(0, 2*np.pi, N, endpoint=False)

X_orb = a * np.cos(phi)
Y_orb = a * np.sin(phi) * np.cos(i)
Z_orb = a * np.sin(phi) * np.sin(i)

v_mag = np.sqrt(G * M / a)
Vx_orb = -v_mag * np.sin(phi)
Vy_orb =  v_mag * np.cos(phi) * np.cos(i)
Vz_orb =  v_mag * np.cos(phi) * np.sin(i)

# ── 3D grid of field points ──────────────────────────────────────────────────
gx_ = np.linspace(-7, 7, 8)
gy_ = np.linspace(-7, 7, 8)
gz_ = np.linspace(-7, 7, 8)
Xg, Yg, Zg = np.meshgrid(gx_, gy_, gz_)

Rg = np.sqrt(Xg**2 + Yg**2 + Zg**2)
Rg[Rg < 1.0] = 1e-6   # mask out origin

rxg = Xg/Rg; ryg = Yg/Rg; rzg = Zg/Rg

# At grid points, use local circular-speed approximation for v (azimuthal)
v_grid = np.sqrt(G * M / Rg)
# azimuthal velocity in xy-plane: v = v_mag * phi_hat = v_mag*(-sinφ, cosφ, 0)
phi_g = np.arctan2(Yg, Xg)
Vxg = -v_grid * np.sin(phi_g)
Vyg =  v_grid * np.cos(phi_g)
Vzg =  np.zeros_like(Vxg)

# g field on grid
gm_g = G * M / Rg**2
gxg = -gm_g * rxg;  gyg = -gm_g * ryg;  gzg = -gm_g * rzg

# H field on grid
Sdotrg = S[0]*rxg + S[1]*ryg + S[2]*rzg
Hp_g = 4*G / Rg**3
Hxg = Hp_g*(3*Sdotrg*rxg - S[0])
Hyg = Hp_g*(3*Sdotrg*ryg - S[1])
Hzg = Hp_g*(3*Sdotrg*rzg - S[2])

# v × H on grid
vxHxg = Vyg*Hzg - Vzg*Hyg
vxHyg = Vzg*Hxg - Vxg*Hzg
vxHzg = Vxg*Hyg - Vyg*Hxg

Fxg = gxg + vxHxg;  Fyg = gyg + vxHyg;  Fzg = gzg + vxHzg
Fmg = np.sqrt(Fxg**2 + Fyg**2 + Fzg**2)
Fmg[Fmg == 0] = 1e-9

Fxg_n = Fxg/Fmg;  Fyg_n = Fyg/Fmg;  Fzg_n = Fzg/Fmg

# ── Orbital force (same as before) ──────────────────────────────────────────
R_orb = a
rx_o = X_orb/R_orb; ry_o = Y_orb/R_orb; rz_o = Z_orb/R_orb
gm_o = G*M/R_orb**2
gxo = -gm_o*rx_o; gyo = -gm_o*ry_o; gzo = -gm_o*rz_o
Sdotro = S[0]*rx_o + S[1]*ry_o + S[2]*rz_o
Hp_o = 4*G/R_orb**3
Hxo = Hp_o*(3*Sdotro*rx_o - S[0])
Hyo = Hp_o*(3*Sdotro*ry_o - S[1])
Hzo = Hp_o*(3*Sdotro*rz_o - S[2])
vxHxo = Vy_orb*Hzo - Vz_orb*Hyo
vxHyo = Vz_orb*Hxo - Vx_orb*Hzo
vxHzo = Vx_orb*Hyo - Vy_orb*Hxo
Fxo = gxo+vxHxo; Fyo = gyo+vxHyo; Fzo = gzo+vxHzo
Fmo = np.sqrt(Fxo**2+Fyo**2+Fzo**2)
Fxo_n = Fxo/Fmo; Fyo_n = Fyo/Fmo; Fzo_n = Fzo/Fmo

# ── Combined magnitude range for single colourbar ───────────────────────────
all_mag = np.concatenate([Fmg.ravel(), Fmo])
F_mag = all_mag   # used for colourbar range

# Normalise for arrow direction
Fx_n = Fxo_n;  Fy_n = Fyo_n;  Fz_n = Fzo_n

# ── Plot ─────────────────────────────────────────────────────────────────────
cmap  = plt.cm.inferno
cnorm = Normalize(vmin=np.percentile(all_mag, 5),
                  vmax=np.percentile(all_mag, 95))

fig = plt.figure(figsize=(11, 9))
ax  = fig.add_subplot(111, projection='3d')

# ── Grid field arrows (smaller, more transparent) ───────────────────────────
xf = Xg.ravel(); yf = Yg.ravel(); zf = Zg.ravel()
fxf = Fxg_n.ravel(); fyf = Fyg_n.ravel(); fzf = Fzg_n.ravel()
mf  = Fmg.ravel()
cols_grid = cmap(cnorm(mf))

for xi, yi, zi, ux, uy, uz, col in zip(xf, yf, zf, fxf, fyf, fzf, cols_grid):
    ax.quiver(xi, yi, zi, ux, uy, uz,
              length=0.38, normalize=False,
              color=col, linewidth=0.5, arrow_length_ratio=0.25, alpha=0.6)

# Orbit path
ax.plot(X_orb, Y_orb, Z_orb, color='cyan', linewidth=1.5,
        linestyle='--', alpha=0.8, label='Orbit path (i=30°)')

# ── Orbital force arrows (larger, fully opaque) ─────────────────────────────
cols_orb = cmap(cnorm(Fmo))
for xi, yi, zi, ux, uy, uz, col in zip(X_orb, Y_orb, Z_orb,
                                         Fxo_n, Fyo_n, Fzo_n, cols_orb):
    ax.quiver(xi, yi, zi, ux, uy, uz,
              length=0.6, normalize=False,
              color=col, linewidth=1.2, arrow_length_ratio=0.3)

# Central body
ax.scatter(0, 0, 0, s=180, color='orangered', zorder=10, label='Central body')

# Spin axis indicator
ax.quiver(0, 0, -4, 0, 0, 8, color='royalblue', linewidth=1.5,
          arrow_length_ratio=0.1, label=r'Spin axis $\mathbf{S}$')

# Colourbar
sm = ScalarMappable(cmap=cmap, norm=cnorm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, shrink=0.55, pad=0.1)
cbar.set_label(r'$|\mathbf{F}|/m$ magnitude', fontsize=11)

ax.set_xlabel('X');  ax.set_ylabel('Y');  ax.set_zlabel('Z')
ax.set_title(
    '\n'
    '\n'
    r'$m\,\dfrac{d^2\vec{r}}{dt^2} = m\vec{g} + m\,(\vec{v}\times\vec{H})$'
    
    r' Satellite orbit  $i = 30°$  ',
    fontsize=11
)
ax.legend(fontsize=9, loc='upper left')

plt.tight_layout()
plt.show()
