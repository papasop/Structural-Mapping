# 🔷 K = 1/2 as a Structural Mapping of the Critical Line ℜ(s) = 1/2

> A phase-geometric perspective on the Riemann Hypothesis via entropy coupling  
> **Author**: Y.Y.N. Li (2025)  
> **Status**: Research Prototype · Peer Review Ready

---

## 🧠 Summary

This project numerically demonstrates that the **structural ratio**  
\[
K(n) = \frac{d \log|\phi(n)|}{d \log H(n)} \approx \frac{1}{2}
\]  
acts as a *structural mapping* of the Riemann zeta function’s **critical line** ℜ(s) = 1/2.

We construct a geometric phase function:
\[
\phi(n) = \tau_n = \frac{\pi}{2} - \arctan(c \cdot \gamma_n)
\]
where γₙ is the imaginary part of the *n*-th Riemann zero, and c is automatically optimized.

The resulting coupling between φ(n) and entropy  
\[
H(n) = \log(1 + \phi(n)^2)
\]
yields K(n) values sharply centered at 0.5 (σ ≈ 3e−5), forming a square-root law of entropy–structure coupling.

---

## 📁 Files

| File | Description |
|------|-------------|
| `verify_K_half.py` | Main script for computing φ(n), H(n), and K(n) from ζ(s) zeros |
| `README.md`        | This file |
| `figures/`         | Plots and images generated during the run (optional) |

---

## 📦 Requirements

```bash
pip install numpy matplotlib scipy mpmath













https://doi.org/10.5281/zenodo.16271076
K = 1/2 as a Structural Mapping of the Critical Line ℜ(s) = 1/2: Verification via Phase Geometry
Creators
