import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11
c = 299792458

M = 5.972e24
R = 6.371e6
omega = 7.292115e-5
I = 0.33 * M * R**2
S = I * omega

a = 7e6
e = 0.01
i = np.radians(60)

Omega_LT = 2 * G * S / (c**2 * a**3 * (1 - e**2)**1.5)

theta = np.linspace(0, 2 * np.pi, 400)
r = a * (1 - e**2) / (1 + e * np.cos(theta))

fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111, projection='3d')

delta_deg = 30
delta_rad = np.radians(delta_deg)
seconds_per_step = delta_rad / Omega_LT
years_per_step = seconds_per_step / (3600 * 24 * 365.25)

time_steps = [0, 1, 2, 3, 4]

# gradient colors
colors = plt.cm.Greens(np.linspace(0.35, 0.9, len(time_steps)))

for idx, t in enumerate(time_steps):
    Omega = np.radians(delta_deg * t)

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    y_i = y * np.cos(i)
    z_i = y * np.sin(i)

    xp = x * np.cos(Omega) - y_i * np.sin(Omega)
    yp = x * np.sin(Omega) + y_i * np.cos(Omega)
    zp = z_i

    elapsed_years = t * years_per_step
    if elapsed_years >= 1e6:
        time_str = f"{elapsed_years/1e6:.2f} Myr"
    elif elapsed_years >= 1e3:
        time_str = f"{elapsed_years/1e3:.2f} kyr"
    else:
        time_str = f"{elapsed_years:.1f} yr"

    ax.plot(
        xp, yp, zp,
        linewidth=2,
        color=colors[idx],
        label=f"t = {time_str}  |  Ω = {delta_deg*t}°"
    )

ax.scatter(0, 0, 0, s=100, color='black', zorder=10, label='Earth')

ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_zlabel("Z (m)")
ax.set_title("Lense–Thirring Orbital Precession")
ax.legend(fontsize=8)

plt.tight_layout()
plt.show()
