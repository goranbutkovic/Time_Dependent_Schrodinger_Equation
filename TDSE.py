import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.linalg import eigh_tridiagonal

# -------------------------
# Grid 
# -------------------------
Nx = 301
dx = 1 / (Nx - 1)
dt = 1e-7
x = np.linspace(0, 1, Nx)

# ------------------------------------------
# Početni uvjeti (stanje) valne funkcije 
# ------------------------------------------

# 1.) Stacionarno stanje (stacionarno stanje za potencijal čestice u kutiji):

#psi0 = np.sqrt(2) * np.sin(4*np.pi * x)                     


# 2.) Linearna kombijacija stacionarnih stanja kao početni uvjet: 

# psi0 = np.sqrt(2) * (np.sin(np.pi * x) +
#                      np.sin(2*np.pi * x) + 
#                      np.sin(4*np.pi * x) +
#                      np.sin(6*np.pi * x) +
#                      np.sin(8*np.pi * x) +
#                      np.sin(10*np.pi * x)              
#                     )


# 3.) Gaussian valni paket: 

# psi0 = np.exp(-200*(x-0.8)**2) * np.sin(np.pi*x)

# NORMALIZACIJA

#psi0 /= np.sqrt(np.trapz(np.abs(psi0)**2, x))  


# -----------------------------------------------------------------
# Potencijali 
# -----------------------------------------------------------------

### Jama

# def V(x):
#     mu, sigma = 1/2, 1/20
#     return -1e4 * np.exp(-(x - mu)**2 / (2 * sigma**2))

### Potencijal čestica u kutiji V = 0

# def V(x):
#     return np.zeros_like(x)

### Harmonijski oscilator

# def V(x):
#     x0 = 0.5        # center of the oscillator
#     k = 1e4         # stiffness (adjust as needed)
#     return 0.5 * k * (x - x0)**2

### Barijera

# def V(x):
#     V0 = 1e4        # height of the barrier
#     x_start = 0.29  # start of the barrier
#     x_end   = 0.51  # end of the barrier
#     return V0 * ((x >= x_start) & (x <= x_end))

# Visualize potential (optional)
plt.figure(figsize=(8,3))
plt.plot(x, V(x))
plt.xlabel('$x$')
plt.ylabel('$V(x)$')
plt.tight_layout()

# -------------------------
# Eigenvalue problem
# -------------------------
d = 1/dx**2 + V(x)[1:-1]
e = -1/(2*dx**2) * np.ones(len(d)-1)

E, phi = eigh_tridiagonal(d, e)

#---------------------- I.) STACIONARNA STANJA HARMONIJSKOG OSCILATORA ------------------

# -----------------------------------------------------
# STACIONARNO STANJE
# ------------------

# n_state = 100  # ground state; 1 = first excited, etc.
# psi0 = np.pad(phi.T[n_state], (1,1), mode='constant')  # add boundary points
# psi0 /= np.sqrt(np.trapz(np.abs(psi0)**2, x))   

# ----------------------------------------------------------------------------
# LINEARNA KOMBINACIJA
# --------------------

# states_to_combine = [0, 1, 2]   # indices of eigenstates
# coefficients = [1.0, 0.5, 0.3]  # relative amplitudes

# # Construct initial wavefunction as linear combination
# psi0 = np.zeros_like(x)
# for n, c in zip(states_to_combine, coefficients):
#     psi_n = np.pad(phi.T[n], (1,1), mode='constant')  # add boundary points
#     psi0 += c * psi_n

# # Normalize
# psi0 /= np.sqrt(np.trapz(np.abs(psi0)**2, x))

#------------------------------------------------------------------

#---------------------- II.) STACIONARNA STANJA BARIJERE ------------------


# n_state = 1  # 0 = ground state, 1 = first excited, etc.

# psi0 = np.pad(phi.T[n_state], (1,1), mode='constant')  # add boundary points
# psi0 /= np.sqrt(np.trapz(np.abs(psi0)**2, x))          # normalize

#------------------------------------------------------------------


Nstates = 7000
E_js = E[:Nstates]
psi_js = np.pad(phi.T[:Nstates], [(0,0),(1,1)], mode='constant')

cs = psi_js @ psi0

def psi_m2(t):
    return psi_js.T @ (cs * np.exp(-1j * E_js * t))

# -------------------------
# Animation
# -------------------------
time_multiplier = 200

def animate(i):
    ln.set_data(x, np.abs(psi_m2(time_multiplier*i*dt))**2)
    time_text.set_text('t = {:.3f}'.format(time_multiplier*i*dt))
    return ln, time_text

fig, ax = plt.subplots(figsize=(8,4))

ln, = ax.plot([], [], 'b', lw=2, label='Eigenvalue method')

time_text = ax.text(
    0.65, 16, '',
    fontsize=15,
    bbox=dict(facecolor='white', edgecolor='black')
)

ax.set_xlim(0, 1)
ax.set_ylim(-1, 20)
ax.set_xlabel('$x/L$', fontsize=20)
ax.set_ylabel('$|\psi(x)|^2$', fontsize=20)
ax.legend()


ani = animation.FuncAnimation(
    fig,
    animate,
    frames=30000,
    interval = 0,
    blit=True
)

plt.show()
