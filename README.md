# Lense–Thirring Effect (Frame Dragging)

![Lense–Thirring Orbital Precession](Theory\Lense–Thirring Orbital Precession.png)

## Overview

The **Lense–Thirring effect** is a prediction of General Relativity where the rotation of a massive body drags the surrounding spacetime. This frame-dragging produces small deviations in the motion of nearby objects, leading to **orbital precession**.

This project studies gravitomagnetic effects of rotating masses using the **weak-field approximation** of Einstein's field equations and explores the analogy between **gravity and electromagnetism**.

---

## Weak Field Approximation

In weak gravitational fields, spacetime can be approximated as a small perturbation of flat spacetime.

$$g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$$

where

- $g_{\mu\nu}$ — spacetime metric  
- $\eta_{\mu\nu}$ — Minkowski metric  
- $h_{\mu\nu}$ — small perturbation due to gravity

---

## Gravitational Potential

![Scalar Potential](images/potential.png)

The Newtonian gravitational potential behaves similarly to the electric potential:

$$\Phi = -\frac{GM}{r}$$

---

## Gravitational Field

![Scalar Field](images/gravitational_field.png)

The gravitational acceleration is

$$\vec{g} = -\nabla\Phi$$

This represents the dominant force governing orbital motion.

---

## Gravitomagnetic Vector Potential

![Vector Potential](images/vector_potential.png)

A rotating mass produces a vector potential analogous to the magnetic vector potential:

$$\vec{\beta} = -4G\frac{\vec{S} \times \vec{r}}{r^{3}}$$

where

- $\vec{S}$ — angular momentum of the rotating body  
- $\vec{r}$ — position vector

---

## Gravitomagnetic Field

![Gravitomagnetic Field](images/gravitomagnetic_field.png)

Taking the curl of the vector potential produces the **gravitomagnetic field**:

$$\vec{H} = \nabla \times \vec{\beta}$$

This term contributes a relativistic correction to Newtonian gravity.

---

## Equation of Motion

The motion of a particle in this field becomes analogous to the Lorentz force equation:

$$m\frac{d^{2}\vec{r}}{dt^{2}} = m\vec{g} + m\left(\vec{v} \times \vec{H}\right)$$

This highlights the analogy between gravitational and electromagnetic fields.

---

## Orbital Precession

![Orbital Precession](images/precession.png)

The gravitomagnetic field causes the orbital angular momentum to precess:

$$\frac{d\vec{L}}{dt} = \vec{L} \times \vec{\Omega}_{LT}$$

where the Lense–Thirring precession rate is

$$\vec{\Omega}_{LT} = \frac{4G\vec{S}}{r^{3}}$$

---

## Experimental Verification

Satellite missions such as **LAGEOS** have measured the predicted frame-dragging effect caused by Earth's rotation.  
The predicted precession is approximately **31 milliarcseconds per year**, which closely matches observational measurements.

---

## Visualizations

The repository includes Python scripts that generate visualizations for:

- Gravitational potential
- Gravitational field
- Gravitomagnetic vector potential
- Gravitomagnetic field
- Lense–Thirring orbital precession
- Effective force field on an inclined satellite orbit

These simulations illustrate how relativistic corrections modify classical orbital motion.

---

## References

- Einstein, *The Foundation of the General Theory of Relativity* (1916)
- Lense & Thirring (1918)
- Misner, Thorne & Wheeler — *Gravitation*
- Ciufolini & Pavlis — Experimental confirmation of frame dragging
